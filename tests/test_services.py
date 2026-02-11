import pytest
import pandas as pd
import os
import requests
from datetime import datetime
from app.services.extractor.api_extractor import APIExtractor
from app.services.extractor.csv_extraction_command import CSVExtractionCommand
from app.services.cleaning.cleaning_nulls import CleaningNulls
from app.services.cleaning.cleaning_type import TypeCleaner
from app.services.cleaning.cleaning_outliers import OutlierCleaner
from app.services.cleaning.cleaner_pipeline import CleaningPipeline
from app.services.pipeline import MeteoPipeline

class TestAPIExtractor(APIExtractor):
    def get_data(self) -> pd.DataFrame:
        if self.raw_data is None:
             raise ValueError("No data")
        return pd.DataFrame([self.raw_data])

class TestExtractors:
    def test_api_extractor_init(self):
        extractor = TestAPIExtractor("dataset_id", "json")
        assert extractor.get_endpoint() == "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/dataset_id/exports/json"
        
        with pytest.raises(ValueError):
            TestAPIExtractor("id", "invalid_format")

    def test_api_extractor_filter(self):
        extractor = TestAPIExtractor("id")
        extractor.add_filter("col", ">", 10)
        assert extractor.filters == [("col", ">", 10)]
        
        with pytest.raises(ValueError):
            extractor.add_filter("col", "invalid", 10)

    def test_api_extractor_where(self):
        extractor = TestAPIExtractor("id")
        extractor.add_filter("num", ">", 10)
        extractor.add_filter("str", "=", "val")
        extractor.add_filter("date", "=", datetime(2023, 1, 1))
        
        where = extractor.build_where_clause()
        assert "num > 10" in where
        assert "str = 'val'" in where
        assert "date = date'2023-01-01'" in where

    def test_api_extractor_fetch_json(self, requests_mock, mock_api_response_json):
        extractor = TestAPIExtractor("id", "json")
        requests_mock.get(extractor.get_endpoint(), json=mock_api_response_json)
        
        data = extractor.fetch()
        assert data == mock_api_response_json
        
    def test_api_extractor_fetch_error(self, requests_mock):
        extractor = TestAPIExtractor("id")
        requests_mock.get(extractor.get_endpoint(), status_code=500)
        
        with pytest.raises(ConnectionError):
            extractor.fetch()

    def test_command_execution(self, requests_mock):
         cmd = CSVExtractionCommand("station_id")
         url = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/station_id/exports/csv"
         
         csv_content = "col1;col2\nval1;val2"
         requests_mock.get(url, text=csv_content)
         
         df = cmd.execute()
         assert isinstance(df, pd.DataFrame)
         assert not df.empty
         df = cmd.execute()
         assert isinstance(df, pd.DataFrame)
         assert not df.empty
         assert df.iloc[0]["col1"] == "val1"

    def test_csv_extractor_no_data(self):
        from app.services.extractor.csv_extractor import CSVExtractor
        extractor = CSVExtractor("id")
        with pytest.raises(ValueError):
            extractor.get_data()

    def test_api_extractor_date_filter_error(self):
        extractor = TestAPIExtractor("id")
        extractor.add_filter("date", "=", "not-a-date")
        where = extractor.build_where_clause()
        assert "date = 'not-a-date'" in where

    def test_api_extractor_date_obj(self):
        extractor = TestAPIExtractor("id")
        dt = datetime(2023, 10, 27)
        extractor.add_filter("date", "=", dt)
        where = extractor.build_where_clause()
        assert "date = date'2023-10-27'" in where

    def test_api_extractor_date_str_valid(self):
        extractor = TestAPIExtractor("id")
        extractor.add_filter("date", "=", "2023-10-27")
        where = extractor.build_where_clause()
        assert "date = date'2023-10-27'" in where

    def test_api_extractor_parquet_invalid(self, requests_mock):
        extractor = TestAPIExtractor("id", "parquet")
        requests_mock.get(extractor.get_endpoint(), content=b"parquet_content")
        data = extractor.fetch()
        assert data == b"parquet_content"

    def test_api_extractor_empty_filters(self):
         extractor = TestAPIExtractor("id")
         assert extractor.build_where_clause() is None


class TestCleaning:
    @pytest.fixture
    def dirty_df(self):
        data = {
            "temperature_en_degre_c": [20.5, None, 1000.0, 15.0],
            "humidite": [50.0, 60.0, None, 110.0], 
            "pression": [1013.0, 1012.0, 1011.0, 500.0],
            "date": ["2023-01-01", "invalid_date", "2023-01-02", "2023-01-03"]
        }
        return pd.DataFrame(data)

    def test_cleaning_nulls(self, dirty_df):
        cleaner = CleaningNulls(["temperature_en_degre_c", "humidite"])
        cleaned = cleaner.clean(dirty_df.copy())
        assert len(cleaned) == 2 

    def test_type_cleaner(self):
        df = pd.DataFrame({
            "temperature_en_degre_c": ["20.5", "invalid"],
            "humidite": ["50", "60.5"],
            "heure_de_paris": ["2023-01-01T12:00:00+00:00", "invalid"]
        })
        cleaner = TypeCleaner()
        cleaned = cleaner.clean(df)
        assert len(cleaned) == 1
        assert pd.api.types.is_float_dtype(cleaned["temperature_en_degre_c"])

    def test_outlier_cleaner(self):
        df = pd.DataFrame({
            "pression": [1013.0, 500.0, 1200.0, 900.0]
        })
        cleaner = OutlierCleaner()
        cleaned = cleaner.clean(df)
        assert len(cleaned) == 2
        assert 1013.0 in cleaned["pression"].values
        assert 900.0 in cleaned["pression"].values

    def test_cleaning_pipeline(self, dirty_df):
        pipeline = CleaningPipeline()
        pipeline.add(CleaningNulls(["temperature_en_degre_c"]))
        res = pipeline.run(dirty_df)
        assert len(res) == 3         

class TestPipeline:
    def test_pipeline_run(self, tmp_path, requests_mock):
        output_dir = tmp_path / "extracted"
        pipeline = MeteoPipeline(output_dir=str(output_dir))
        
        station_id = "test-station"
        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{station_id}/exports/csv"
        
        csv_content = (
            "heure_de_paris;station_id;nom_station;ville;temperature_en_degre_c;humidite;pression;direction_du_vecteur_de_vent_max_en_degres;direction_du_vecteur_vent_moyen;direction_du_vecteur_de_rafale_de_vent_max;force_moyenne_du_vecteur_vent;force_rafale_max;pluie;pluie_intensite_max\n"
            "2023-10-27T10:00:00+02:00;test-station;Test Station;Toulouse;20.0;50;1013.2;10;10;10;10;10;0;0"
        )
        
        requests_mock.get(url, text=csv_content)
        
        df = pipeline.run([station_id])
        
        assert not df.empty
        assert len(df) == 1
        assert "station_id" in df.columns
        assert df.iloc[0]["station_id"] == station_id
        
        files = list(output_dir.glob("*.csv"))
        assert len(files) == 1
        assert station_id in files[0].name

    def test_pipeline_no_data(self, tmp_path, requests_mock):
        output_dir = tmp_path / "extracted_empty"
        pipeline = MeteoPipeline(output_dir=str(output_dir))
        station_id = "test-empty"
        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{station_id}/exports/csv"
        
        requests_mock.get(url, text="header\n")
        
        requests_mock.get(url, text="") 
        
        requests_mock.get(url, text="h1;h2\n") 
        df = pipeline.run([station_id])
        assert df.empty
        
    def test_cleaner_missing_cols(self):
        df = pd.DataFrame({"a": [1]})
        cleaner = CleaningNulls(["b"]) 
        
        with pytest.raises(KeyError):
             cleaner.clean(df)
             
    def test_cleaner_types(self):
        with pytest.raises(ValueError):
            CleaningNulls("not-a-list")
        
        c = CleaningNulls(["col"])
        with pytest.raises(TypeError):
            c.clean("not-a-df")

    def test_type_cleaner_datetime_valid(self):
        df = pd.DataFrame({"date": ["2023-01-01"]})
        cleaner = TypeCleaner({"date": "datetime"})
        res = cleaner.clean(df)
        assert pd.api.types.is_datetime64_any_dtype(res["date"])

    def test_type_cleaner_prints(self, capsys):
        df = pd.DataFrame({"val": ["invalid"]})
        cleaner = TypeCleaner({"val": float})
        cleaner.clean(df)
        captured = capsys.readouterr()
        assert "ligne(s) supprimée(s)" in captured.out
        
    def test_type_cleaner_int(self):
        df = pd.DataFrame({"val": ["10", "invalid", "20.5"]})
        cleaner = TypeCleaner({"val": int})
        res = cleaner.clean(df)
        assert len(res) >= 1

    def test_type_cleaner_str(self):
        df = pd.DataFrame({"val": [123, "text"]})
        cleaner = TypeCleaner({"val": str})
        res = cleaner.clean(df)
        assert pd.api.types.is_string_dtype(res["val"]) or pd.api.types.is_object_dtype(res["val"])
        assert res.iloc[0]["val"] == "123"

    def test_type_cleaner_missing_col(self):
        df = pd.DataFrame({"a": [1]})
        cleaner = TypeCleaner({"b": int})
        res = cleaner.clean(df)
        assert len(res) == 1


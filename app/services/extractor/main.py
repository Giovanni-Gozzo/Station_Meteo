from app.services.extractor.csv_extractor import CSVExtractor
from app.services.extractor.json_extractor import JSONExtractor
from app.services.extractor.parquet_extractor import ParquetExtractor

if __name__ == "__main__":
    dataset_id = "24-station-meteo-colomiers-zi-enjacca"

    # print("=== Extraction CSV ===")
    # csv_extractor = CSVExtractor(dataset_id)
    # csv_extractor.fetch()
    # df_csv = csv_extractor.get_data()
    # print(df_csv.head())
    # print(df_csv.shape)
    #
    # print("\n=== Extraction JSON ===")
    # json_extractor = JSONExtractor(dataset_id)
    # json_extractor.fetch()
    # df_json = json_extractor.get_data()
    # print(df_json.head())
    # print(df_json.shape)
    #
    # print("\n=== Extraction Parquet ===")
    # parquet_extractor = ParquetExtractor(dataset_id)
    # parquet_extractor.fetch()
    # df_parquet = parquet_extractor.get_data()
    # print(df_parquet.head())
    # print(df_parquet.shape)


    extractor = ParquetExtractor(dataset_id)

    extractor.add_filter("heure_de_paris", ">", "2025-11-01")
    extractor.add_filter("heure_de_paris", "<", "2025-11-03")
    extractor.fetch()
    df = extractor.get_data()

    print(df.head())
    print(df.shape)

import os
from datetime import datetime, timedelta
from app.services.cleaning.cleaning_outliers import OutlierCleaner
from app.services.extractor.csv_extractor import CSVExtractor
from app.services.cleaning.cleaner_pipeline import CleaningPipeline
from app.services.cleaning.cleaning_nulls import CleaningNulls


def run_pipeline(dataset_ids):
    """Pipeline d’extraction, nettoyage et sauvegarde CSV pour plusieurs stations."""

    # Dossier de sortie
    output_dir = "../../data/extracted"
    os.makedirs(output_dir, exist_ok=True)

    now = datetime.utcnow()
    one_hour_ago = now - timedelta(hours=1)
    one_hour_ago_iso = one_hour_ago.strftime("%Y-%m-%dT%H:%M:%S")
    print(f"[INFO] Extraction des relevés depuis : {one_hour_ago_iso} (UTC)")

    for dataset_id in dataset_ids:
        print("\n===============================")
        print(f"[INFO] 📡 Station : {dataset_id}")

        try:
            # Extraction CSV
            extractor = CSVExtractor(dataset_id)
            extractor.add_filter("heure_de_paris", ">", one_hour_ago_iso)
            df = extractor.fetch()
            df = extractor.get_data()

            if df is None or df.empty:
                print(f"[⚠️] Aucune donnée brute pour {dataset_id}")
                continue

            print(f"[INFO] Colonnes disponibles : {df.columns}")

            # Nettoyage
            cleaning_pipeline = CleaningPipeline()
            cleaning_pipeline.add(
                CleaningNulls(columns=["temperature_en_degre_c", "humidite", "pression"])
            )
            cleaning_pipeline.add(OutlierCleaner())
            df = cleaning_pipeline.run(df)
            print(f"[🧹] Données nettoyées ({len(df)} lignes restantes).")

            # Sauvegarde CSV
            if not df.empty:
                timestamp = now.strftime("%Y%m%d_%H%M")
                filename = f"{dataset_id}_{timestamp}.csv"
                filepath = os.path.join(output_dir, filename)
                df.to_csv(filepath, index=False)
                print(f"[✅] Données sauvegardées : {filepath}")
                print(f"[INFO] Lignes extraites (après nettoyage) : {len(df)}")
            else:
                print(f"[⚠️] Aucune donnée valide à sauvegarder pour {dataset_id}")

        except Exception as e:
            print(f"[❌] Erreur pour {dataset_id} : {e}")


if __name__ == "__main__":
    import pandas as pd

    df_ids = pd.read_csv("../../data/meteo_ids.csv")
    DATASET_IDS = df_ids["dataset_id"].tolist()
    run_pipeline(DATASET_IDS)

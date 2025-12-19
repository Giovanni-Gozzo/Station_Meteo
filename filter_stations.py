import pandas as pd
import os
import sys
from datetime import datetime, timedelta
from app.services.extractor.csv_extractor import CSVExtractor
from app.config import CONFIG

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

def filter_stations():
    ids_file = os.path.join(CONFIG["DATA_DIR"], CONFIG["METEO_IDS_FILE"])
    print(f"Reading IDs from: {ids_file}")
    
    try:
        df = pd.read_csv(ids_file)
        all_ids = df["dataset_id"].tolist()
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    active_ids = []
    
    now = datetime.now()
    one_hour_ago_iso = (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
    now_iso = now.strftime("%Y-%m-%dT%H:%M:%S")
    
    print(f"Checking for data between {one_hour_ago_iso} and {now_iso}")

    for station_id in all_ids:
        print(f"Checking station: {station_id}...", end=" ", flush=True)
        try:
            extractor = CSVExtractor(station_id)
            extractor.add_filter("heure_de_paris", ">", one_hour_ago_iso)
            extractor.add_filter("heure_de_paris", "<", now_iso)
            
            # We just need to fetch and see if we get data
            # fetch() might raise an error if 404 or return empty
            try:
                data = extractor.fetch()
                # get_data returns a dataframe
                df_station = extractor.get_data()
                
                if df_station is not None and not df_station.empty:
                    print("ACTIVE ✅")
                    active_ids.append(station_id)
                else:
                    print("INACTIVE ❌ (Empty)")
            except Exception as e:
                print(f"INACTIVE ❌ (Error: {e})")
                
        except Exception as e:
             print(f"Error initializing extractor: {e}")

    print(f"\nFound {len(active_ids)} active stations out of {len(all_ids)}.")
    
    # Save to new file first
    new_df = pd.DataFrame({"dataset_id": active_ids})
    new_file = ids_file # Overwrite directly as requested
    
    # Backup original
    backup_file = ids_file + ".bak"
    df.to_csv(backup_file, index=False)
    print(f"Original list backed up to {backup_file}")
    
    new_df.to_csv(new_file, index=False)
    print(f"Updated list saved to {new_file}")

if __name__ == "__main__":
    filter_stations()

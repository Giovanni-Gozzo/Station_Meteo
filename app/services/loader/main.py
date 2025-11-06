import pandas as pd
from app.services.loader.loader_sqlite import SQLiteLoader

data = {
    "ville": ["Toulouse", "Colomiers", "Blagnac"],
    "temperature": [22.5, 25.1, 24.0],
    "humidite": [60, 55, 58]
}

df = pd.DataFrame(data)

print("=== Données à charger ===")
print(df)

loader = SQLiteLoader(db_path="../../../db/meteo.db")

loader.load(df, table_name="mesures_meteo")

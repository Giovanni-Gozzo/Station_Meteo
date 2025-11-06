import pandas as pd
from app.services.cleaning.cleaner_pipeline import CleaningPipeline
from app.services.cleaning.cleaning_nulls import CleaningNulls
from app.services.cleaning.cleaning_outliers import OutlierCleaner

# =============================
# 🔹 Jeu de données de test
# =============================
data = {
    "temperature": [22, -50, 18, 65, 30, None],
    "humidite": [50, 120, None, 70, 85, 40],
    "ville": ["Toulouse", "Colomiers", "Blagnac", "L'Union", "Tournefeuille", None]
}

df = pd.DataFrame(data)

print("=== Données initiales ===")
print(df)
print("\nNombre de lignes avant nettoyage :", len(df))

# =============================
# 🔹 Création du pipeline
# =============================
pipeline = CleaningPipeline()

# Étape 1 : Supprimer les lignes avec des nulls sur temperature / humidite
pipeline.add(CleaningNulls(columns=["temperature", "humidite"]))

# Étape 2 : Supprimer les valeurs aberrantes
pipeline.add(OutlierCleaner({
    "temperature": (-30, 60),
    "humidite": (0, 100)
}))

# =============================
# 🔹 Exécution du pipeline
# =============================
df_cleaned = pipeline.run(df)

print("\n=== Données nettoyées ===")
print(df_cleaned)
print("\nNombre de lignes après nettoyage :", len(df_cleaned))

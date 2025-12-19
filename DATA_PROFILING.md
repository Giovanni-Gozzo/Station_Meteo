# Documentation du Jeu de Données (Météo)

## Source
Données issues de l'OpenData de **Toulouse Métropole**.
API : `https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets`

## Structure des Données

Chaque enregistrement météo contient les champs suivants :

| Champ | Type | Description |
|-------|------|-------------|
| `heure_de_paris` | `datetime` | Date et heure de la mesure (Locale) |
| `station_id` | `string` | Identifiant unique de la station (ex: `33-..., 37-...`) |
| `nom_station` | `string` | Nom humain de la station |
| `ville` | `string` | Ville où se situe la station |
| `temperature_en_degre_c` | `float` | Température ambiante (°C) |
| `humidite` | `integer` | Taux d'humidité relative (%) |
| `pression` | `float` | Pression atmosphérique (hPa) |
| `pluie` | `float` | Cumul de pluie sur la période (mm) |
| `pluie_intensite_max` | `float` | Intensité maximale de pluie (mm/h) |
| `force_moyenne_du_vecteur_vent` | `float` | Vitesse moyenne du vent (km/h) |
| `force_rafale_max` | `float` | Vitesse maximale en rafale (km/h) |
| `direction_du_vecteur_vent_moyen` | `float` | Direction du vent moyen (degrés) |

## Qualité des Données

Le pipeline applique les nettoyages suivants :
1.  **Suppression des Nulls** : Si `temperature`, `humidite` ou `pression` est absent, la ligne est rejetée.
2.  **Typage** : Les champs numériques sont convertis en `float` ou `int`. Les dates ISO sont parsées.
3.  **Détection d'Outliers** : Les valeurs de pression aberrantes (hors [850, 1100] hPa) sont filtrées.

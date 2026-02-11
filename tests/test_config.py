import pytest
import os
from app.config import Configuration, CONFIG

def test_config_singleton():
    c1 = Configuration()
    c2 = Configuration()
    assert c1 is c2
    assert c1 is CONFIG

def test_config_get():
    assert CONFIG.get("DEFAULT_SORT") == "date"
    assert CONFIG.get("NON_EXISTENT", "default") == "default"
    assert CONFIG["DEFAULT_ORDER"] == "desc"

def test_config_values():
    assert "Station_Meteo" in CONFIG.DATA_DIR or "Data" in CONFIG.DATA_DIR
    assert CONFIG.METEO_IDS_FILE == "meteo_ids.csv"

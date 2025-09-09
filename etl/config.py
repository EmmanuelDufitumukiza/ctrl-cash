import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW_XML = DATA / "raw" / "momo.xml"
DB_PATH = DATA / "db.sqlite3"
PROCESSED_JSON = DATA / "processed" / "dashboard.json"
LOG_FILE = DATA / "logs" / "etl.log"

CATEGORIES = {
    "airtime": ["airtime"],
    "cash_power": ["cash power", "cashpower", "electricity"],
    "merchant": ["paid merchant", "merchant payment", "pos"],
    "p2p": ["received", "sent"],
    "withdrawal": ["withdrawal"],
    "deposit": ["deposit"],
    "bank": ["bank"],
    "fees": ["fee", "charge"],
    "other": []
}

TZ = os.getenv("TZ", "Africa/Kigali")

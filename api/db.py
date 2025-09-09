import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / "data" / "db.sqlite3"

def get_conn():
    return sqlite3.connect(str(DB))

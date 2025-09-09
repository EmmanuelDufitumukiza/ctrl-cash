import sqlite3
from pathlib import Path

DDL = '''
CREATE TABLE IF NOT EXISTS transactions (
  id TEXT PRIMARY KEY,
  ts TEXT,
  amount REAL,
  currency TEXT,
  direction TEXT,
  category TEXT,
  counterparty TEXT,
  description TEXT,
  raw_xml TEXT
);
'''

UPSERT = '''
INSERT INTO transactions(id, ts, amount, currency, direction, category, counterparty, description, raw_xml)
VALUES(?,?,?,?,?,?,?,?,?)
ON CONFLICT(id) DO UPDATE SET
  ts=excluded.ts,
  amount=excluded.amount,
  currency=excluded.currency,
  direction=excluded.direction,
  category=excluded.category,
  counterparty=excluded.counterparty,
  description=excluded.description,
  raw_xml=excluded.raw_xml;
'''

def connect(db_path: Path):
    conn = sqlite3.connect(str(db_path))
    return conn

def init_db(conn):
    cur = conn.cursor()
    cur.executescript(DDL)
    conn.commit()

def load(conn, records):
    cur = conn.cursor()
    for r in records:
        cur.execute(UPSERT, (
            r.get("id"),
            r.get("ts"),
            r.get("amount"),
            r.get("currency"),
            r.get("direction"),
            r.get("category"),
            r.get("counterparty"),
            r.get("description"),
            r.get("raw")
        ))
    conn.commit()

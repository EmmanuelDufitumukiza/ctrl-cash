from fastapi import FastAPI
from .db import get_conn
from pathlib import Path
import json

APP_ROOT = Path(__file__).resolve().parents[1]
DASH = APP_ROOT / "data" / "processed" / "dashboard.json"

app = FastAPI()

@app.get("/transactions")
def transactions(limit: int = 50):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, ts, amount, currency, direction, category, counterparty, description FROM transactions ORDER BY ts DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    keys = ["id","ts","amount","currency","direction","category","counterparty","description"]
    return [dict(zip(keys, r)) for r in rows]

@app.get("/analytics")
def analytics():
    if not DASH.exists():
        return {}
    return json.loads(DASH.read_text())

import re
from dateutil import parser
from datetime import timezone
import zoneinfo

PHONE_RE = re.compile(r"(?:\+?25)?0?7\d{8}")
AMOUNT_RE = re.compile(r"RWF\s*([\d,]+(?:\.\d+)?)", re.I)

def to_amount(text):
    m = AMOUNT_RE.search(text)
    if not m:
        return 0.0
    n = m.group(1).replace(",", "")
    try:
        return float(n)
    except:
        return 0.0

def to_direction(text):
    t = text.lower()
    if "received" in t:
        return "in"
    if "sent" in t or "paid" in t or "purchase" in t or "withdrawal" in t:
        return "out"
    return "unknown"

def to_counterparty(text):
    m = PHONE_RE.search(text)
    if m:
        p = m.group(0)
        p = p[-10:]
        return "+250" + p[1:]
    t = text
    if "to " in t:
        seg = t.split("to ",1)[1]
        seg = seg.split(".")[0]
        return seg.strip()
    return "unknown"

def to_timestamp(s, tz="Africa/Kigali"):
    try:
        dt = parser.parse(s)
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=zoneinfo.ZoneInfo(tz))
        return dt.astimezone(zoneinfo.ZoneInfo(tz))
    except:
        return None

def clean(records, tz="Africa/Kigali"):
    out = []
    for r in records:
        amt = to_amount(r["text"])
        dirn = to_direction(r["text"])
        cp = to_counterparty(r["text"])
        ts = to_timestamp(r["timestamp_raw"], tz)
        out.append({
            "id": r["message_id"],
            "ts": ts.isoformat() if ts else None,
            "amount": amt,
            "currency": "RWF",
            "direction": dirn,
            "counterparty": cp,
            "description": r["text"],
            "raw": r["raw"]
        })
    return out

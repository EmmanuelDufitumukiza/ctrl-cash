import argparse, json, logging
from pathlib import Path
from collections import defaultdict
from dateutil import parser as dateparser

from .config import RAW_XML, DB_PATH, PROCESSED_JSON, LOG_FILE, CATEGORIES, TZ
from .parse_xml import parse_xml
from .clean_normalize import clean
from .categorize import categorize
from .load_db import connect, init_db, load

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("etl")

def aggregate(records):
    totals_in = sum(r["amount"] for r in records if r["direction"] == "in")
    totals_out = sum(r["amount"] for r in records if r["direction"] == "out")
    by_cat = defaultdict(lambda: {"count":0,"total":0.0})
    monthly = defaultdict(float)
    counterparties = defaultdict(lambda: {"count":0,"total":0.0})
    for r in records:
        c = r.get("category") or "other"
        by_cat[c]["count"] += 1
        by_cat[c]["total"] += r.get("amount") or 0.0
        if r.get("ts"):
            dt = dateparser.isoparse(r["ts"])
            key = f"{dt.year}-{dt.month:02d}"
            monthly[key] += r.get("amount") or 0.0
        cp = r.get("counterparty") or "unknown"
        counterparties[cp]["count"] += 1
        counterparties[cp]["total"] += r.get("amount") or 0.0
    res = {
        "totals": {"incoming": totals_in, "outgoing": totals_out, "net": totals_in - totals_out},
        "by_category": [{"category": k, "count": v["count"], "total": v["total"]} for k,v in sorted(by_cat.items())],
        "monthly": [{"month": k, "total": v} for k,v in sorted(monthly.items())],
        "top_counterparties": sorted([{"counterparty": k, **v} for k,v in counterparties.items()], key=lambda x: x["total"], reverse=True)[:10]
    }
    return res

def run(xml_path: Path):
    log.info("start etl")
    raw = parse_xml(xml_path)
    log.info("parsed=%d", len(raw))
    cleaned = clean(raw, tz=TZ)
    log.info("cleaned=%d", len(cleaned))
    labeled = categorize(cleaned, CATEGORIES)
    log.info("categorized=%d", len(labeled))
    conn = connect(DB_PATH)
    init_db(conn)
    load(conn, labeled)
    log.info("loaded=%d", len(labeled))
    analytics = aggregate(labeled)
    PROCESSED_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED_JSON, "w") as f:
        json.dump(analytics, f, indent=2)
    log.info("exported json")
    return analytics

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--xml", type=str, default=str(RAW_XML))
    args = ap.parse_args()
    analytics = run(Path(args.xml))
    print(json.dumps(analytics, indent=2))

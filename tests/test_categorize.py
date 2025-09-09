from etl.categorize import categorize
from etl.parse_xml import parse_xml
from etl.clean_normalize import clean
from etl.config import CATEGORIES
from pathlib import Path

def test_categorize():
    raw = parse_xml(Path("data/raw/momo.xml"))
    out = clean(raw)
    labeled = categorize(out, CATEGORIES)
    assert "category" in labeled[0]

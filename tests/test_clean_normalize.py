from etl.clean_normalize import clean
from etl.parse_xml import parse_xml
from pathlib import Path

def test_clean():
    raw = parse_xml(Path("data/raw/momo.xml"))
    out = clean(raw)
    assert out[0]["amount"] >= 0
    assert out[0]["currency"] == "RWF"

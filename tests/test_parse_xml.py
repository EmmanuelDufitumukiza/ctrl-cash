from etl.parse_xml import parse_xml
from pathlib import Path

def test_parse_xml():
    recs = parse_xml(Path("data/raw/momo.xml"))
    assert len(recs) >= 5
    assert "text" in recs[0]

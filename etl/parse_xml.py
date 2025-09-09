from lxml import etree

def parse_xml(path):
    root = etree.parse(str(path)).getroot()
    records = []
    for m in root.findall(".//message"):
        mid = m.get("id") or ""
        date = m.get("date") or ""
        text = (m.findtext("text") or "").strip()
        records.append({
            "message_id": mid,
            "timestamp_raw": date,
            "text": text,
            "raw": etree.tostring(m, encoding="unicode")
        })
    return records

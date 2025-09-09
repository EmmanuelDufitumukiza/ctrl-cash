def categorize(records, categories):
    def pick(desc, direction):
        t = (desc or "").lower()
        for k, keys in categories.items():
            if k == "p2p":
                if "received" in t or "sent" in t:
                    return "p2p"
            else:
                for kw in keys:
                    if kw and kw in t:
                        return k
        if direction == "in":
            return "p2p"
        return "other"
    for r in records:
        r["category"] = pick(r.get("description"), r.get("direction"))
    return records

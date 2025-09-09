# MoMo SMS Analytics – Team Project

Analyze MoMo SMS XML, clean and categorize transactions, store in SQLite, and visualize on a simple frontend dashboard.

## Team  
- Team name: **Ctrl+Cash 💸**  
- Members:  
  - Emmanuel Dufitumukiza  
  - Muhoza Olivier Yvan

## Repo Setup
1. One member creates a GitHub repo and invites teammates as collaborators.
2. Clone and set up Python 3.10+.
3. Create a virtualenv and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and adjust paths if needed.

## Run ETL
```bash
bash scripts/run_etl.sh data/raw/momo.xml
```

## Export dashboard JSON (re-run analytics only)
```bash
bash scripts/export_json.sh
```

## Serve Frontend (static)
```bash
bash scripts/serve_frontend.sh
# open http://localhost:8000
```

## Optional API
```bash
uvicorn api.app:app --reload
# GET http://127.0.0.1:8000/transactions
# GET http://127.0.0.1:8000/analytics
```

## Project Structure
```
.
├── README.md
├── .env.example
├── requirements.txt
├── index.html
├── web/
│   ├── styles.css
│   ├── chart_handler.js
│   └── assets/
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── momo.xml
│   ├── processed/
│   │   └── dashboard.json
│   ├── db.sqlite3
│   └── logs/
│       ├── .gitkeep
│       └── etl.log
├── etl/
│   ├── __init__.py
│   ├── config.py
│   ├── parse_xml.py
│   ├── clean_normalize.py
│   ├── categorize.py
│   ├── load_db.py
│   └── run.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   └── schemas.py
├── scripts/
│   ├── run_etl.sh
│   ├── export_json.sh
│   └── serve_frontend.sh
└── tests/
    ├── test_parse_xml.py
    ├── test_clean_normalize.py
    └── test_categorize.py
```

## Architecture Diagram
**Diagram link:** <add-your-diagram-link>

## Scrum Board
**Board link:** <add-your-board-link>
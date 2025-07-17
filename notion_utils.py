import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_ultima_data_salva() -> str:
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {
        "sorts": [
            {
                "property": "Date/Hora",
                "direction": "descending"
            }
        ],
        "page_size": 1
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    results = response.json().get("results", [])
    if not results:
        return "2025-01-01"  # Valor inicial padrão se estiver vazio

    date_str = results[0]["properties"]["Date/Hora"]["date"]["start"]
    return datetime.strptime(date_str, "%Y-%m-%d").date().isoformat()
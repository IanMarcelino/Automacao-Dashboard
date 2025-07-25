import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def enviar_para_notion(dados: dict, data_str: str):
    """Envia os dados extraídos para o Notion com a data correspondente."""

    # Converte a data de "2025/07/16" para "2025-07-16"
    data_iso = data_str.replace("/", "-")

    # Trata valores do dict 'dados' de string para float e int
    deposito_raw = dados.get("Depósito") or "R$ 0,00"
    deposito_str = deposito_raw.replace("R$", "").replace(".", "").replace(",", ".").strip()
    try:
        deposito_float = float(deposito_str)
    except ValueError:
        deposito_float = 0.0
        
    try:
        registros = int(dados.get("Registros", 0) or 0)
    except ValueError:
        registros = 0

    try:
        ftds = int(dados.get("Primeiro depósito", 0) or 0)
    except ValueError:
        ftds = 0

    try:
        cliques = int(dados.get("Cliques", 0) or 0)
    except ValueError:
        cliques = 0

    payload = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Date/Hora": {
                "date": { "start": data_iso }
            },
            "Deposits amount": {
                "number": deposito_float
            },
            "Registrations": {
                "number": registros
            },
            "FTDs": {
                "number": ftds
            },
            "Visits (unique)": {
                "number": cliques
            },
            "btag": {
                "title": [
                    {
                        "text": {
                            "content": "123456"
                        }
                    }
                ]
            }
        }
    }
    try:
      response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload)
      if not response.ok:
        print("\n❌ ERRO 400 AO ENVIAR PARA NOTION")
        print("Status:", response.status_code)
        print("Resposta:", response.text)
        print("Payload enviado:", payload)
        response.raise_for_status()
      else:
        print(f"Dados enviados para Notion com sucesso! ({data_iso})")

    except requests.exceptions.RequestException as e:
      print("\n❌ Exceção na requisição ao Notion:")
      print("Erro:", str(e))
      print("Payload enviado:", payload)
     
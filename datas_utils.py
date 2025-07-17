import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

def gerar_datas_faltantes(ultima_data_str: str) -> list[str]:
    hoje = datetime.now().date()
    inicio = datetime.strptime(ultima_data_str, "%Y-%m-%d").date() + timedelta(days=1)
    return [(inicio + timedelta(days=i)).strftime("%Y/%m/%d") for i in range((hoje - inicio).days)]
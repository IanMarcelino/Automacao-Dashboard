from selenium import webdriver
from extrator_cliques import extrair_cliques_marketing
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from extrator_dashboard import extrair_dados_dashboard
from dotenv import load_dotenv
from notion_utils import get_ultima_data_salva
from datas_utils import gerar_datas_faltantes
from notion_save import enviar_para_notion 
import os
import time


# carrega variáveis do .env
load_dotenv()

# pega as credenciais do ambiente
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")


# pega a última data salva e gera as faltantes
ultima_data = get_ultima_data_salva()
datas_faltantes = gerar_datas_faltantes(ultima_data)

for data_str in datas_faltantes:
    print(f"\n📅 Coletando dados do dia: {data_str}")

    filtro_data = f"{data_str}{data_str}"

    navegador = webdriver.Chrome()
    navegador.get("https://afiliados.segurobet.com/login")
    navegador.set_window_size(1920, 1080)

    time.sleep(2)

    # login
    navegador.find_element(By.ID, "userName").send_keys(EMAIL)
    navegador.find_element(By.ID, "password").send_keys(SENHA)
    time.sleep(1)
    navegador.find_element(By.ID, "signIn").click()
    time.sleep(5)

    # filtro de data
    data_input = navegador.find_element(By.CLASS_NAME, 'input-element')
    data_input.click()
    time.sleep(1)
    data_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
    time.sleep(1)
    data_input.send_keys(filtro_data)
    time.sleep(3)

    # extrair dados da aba principal
    dados = extrair_dados_dashboard(navegador)

    # ir para aba de estatísticas de link
    navegador.find_element(By.ID, "reports").click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//a[@href="/reports/marketing"]').click()
    time.sleep(10)
    navegador.find_element(By.XPATH, '//a[@href="/reports/marketing/linkStatistics"]').click()
    time.sleep(10)

    # extrair cliques
    cliques = extrair_cliques_marketing(navegador)

    # encerra navegador
    navegador.quit()

    # mostra resultado
    print(f"Depósito: {dados.get('Depósito')}")
    print(f"Registros: {dados.get('Registros')}")
    print(f"Primeiro Depósito: {dados.get('Primeiro depósito')}")
    print(f"Cliques: {cliques}")

    enviar_para_notion({
    "Depósito": dados.get("Depósito"),
    "Registros": dados.get("Registros"),
    "Primeiro depósito": dados.get("Primeiro depósito"),
    "Cliques": cliques
    
}, data_str)

    # envio ao Notion 
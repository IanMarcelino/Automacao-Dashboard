from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from extrator_dashboard import extrair_dados_dashboard

# define o dia de ontem
ontem = (datetime.now() - timedelta(days=1)).strftime("%Y/%m/%d")
filtro_data = f"{ontem}{ontem}"

# inicializa navegador
navegador = webdriver.Chrome()
navegador.get("https://afiliados.segurobet.com/login")
navegador.maximize_window()

time.sleep(2)

# login
navegador.find_element(By.ID, "userName").send_keys("vltzalb@gmail.com")
navegador.find_element(By.ID, "password").send_keys("Vltz@2025")
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

# extrair dados
dados = extrair_dados_dashboard(navegador)

# exibir
print(f"Depósito: {dados.get('Depósito')}")
print(f"Registros: {dados.get('Registros')}")
print(f"Primeiro Depósito: {dados.get('Primeiro depósito')}")

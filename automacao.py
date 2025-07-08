from selenium import webdriver
import time
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://afiliados.segurobet.com/login")
navegador.maximize_window()

# Localiza os campos de e-mail e senha
email_input = navegador.find_element(By.ID, "userName")     # ou By.ID, By.CLASS_NAME etc.
senha_input = navegador.find_element(By.ID, "password")

# Preenche os campos
email_input.send_keys("vltzalb@gmail.com")
senha_input.send_keys("Vltz@2025")

# Clica no botão de login
botao_login = navegador.find_element(By.ID, "signIn")
botao_login.click()

# Aguarda a resposta do login
time.sleep(10)


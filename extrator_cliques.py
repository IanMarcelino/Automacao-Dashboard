from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def extrair_cliques_marketing(navegador: WebDriver) -> int:
    try:
        cliques_element = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/section/main/div[3]/div/div/div[2]/div/div/div/div[1]/div[3]/div/div[9]/div')
        cliques_text = cliques_element.text.strip().replace(".", "").replace(",", "")
        return int(cliques_text)
    except Exception as e:
        print("Erro ao extrair Cliques:", e)
        return 0
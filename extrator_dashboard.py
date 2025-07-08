from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def extrair_dados_dashboard(navegador: WebDriver) -> dict[str, int | str]:
    """Extrai valores do painel: depósito, registros e primeiro depósito."""
    
    # Pegar depósito (valor principal separado)
    deposito = navegador.find_element(By.CLASS_NAME, 'dashboardSmallWidgetTag-bc').text


    # Pegar elementos tipo "Registros - 123"
    itens = navegador.find_elements(By.CLASS_NAME, "item-name")

    dados = {
        "Depósito": deposito
    }

    for item in itens:
        texto = item.text
        if "-" in texto:
            chave, valor = texto.split("-", 1)
            chave = chave.strip()
            valor = valor.strip()
            try:
                dados[chave] = int(valor)
            except ValueError:
                continue

    return dados
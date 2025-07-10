from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def extrair_dados_dashboard(navegador: WebDriver) -> dict[str, int | str]:
    """Extrai valores do painel: depósito, registros, primeiro depósito e cliques."""

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

    # 🔽 Novo trecho: extrai apenas "Cliques"
    try:
        cliques_element = navegador.find_element(By.XPATH, '//div[contains(text(), "Cliques")]/following-sibling::div')
        cliques_text = cliques_element.text.strip().replace(".", "").replace(",", "")
        dados["Cliques"] = int(cliques_text)
    except Exception as e:
        print("Não foi possível extrair os Cliques:", e)
        dados["Cliques"] = 0  # ou None, se preferir

    return dados

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def get_default_edge_options():
    options = Options()
    # Adicione outras opções padrão do Edge se necessário
    return options


options = get_default_edge_options()
options.timeouts = {'script': 5000}
driver = webdriver.Edge(options=options)

browser = webdriver.Edge()

url = "https://www.tbca.net.br/base-dados/composicao_alimentos.php"

browser.get(url)
# text_box = webdriver.find_element(by=By.CLASS_NAME, value="TBCA - Tabela Brasileira de Composição de Alimentos.")
element = browser.find_element(by=By.ID, value="produto")
element.click()
element.send_keys('alface')

btn_submit = browser.find_element(by=By.XPATH, value="//button[@type='submit']")
btn_submit.click()

result = browser.find_element(by=By.XPATH, value="//th[contains(.,'Código')]")
# driver.implicitly_wait(1)

codigo = browser.find_element(by=By.XPATH, value=" *//tr[1]/td[1]")

if codigo:
    print(codigo.text)
else:
    print("fail")

driver.quit()

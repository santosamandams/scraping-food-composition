import requests as req
from bs4 import BeautifulSoup
from lxml import etree
import time

# dicionario contem o xpath do valor dos componentes
xpath_composition = {
    "energy_kcal": "//*[@id=\"tabela1\"]/tbody/tr[2]/td[3]",
    "carbohydrate": "//*[@id=\"tabela1\"]/tbody/tr[4]/td[3]",
    "protein": "//*[@id=\"tabela1\"]/tbody/tr[6]/td[3]",
    "fiber": "//*[@id=\"tabela1\"]/tbody/tr[8]/td[3]"
}

codigos_alimentos = ["BRC0001C", "BRC0002C", "BRC0003C"]  # Adicione quantos quiser

# Percorrer cada código de alimento
for codigo in codigos_alimentos:
    url = f"https://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto={codigo}"
    print(f"\n🔎 Buscando dados para o alimento: {codigo}\n" + "-" * 40)

    try:
        response = req.get(url)
        response.raise_for_status()

        # Usar lxml para analisar o HTML e habilitar XPath
        parser = etree.HTMLParser()
        tree = etree.fromstring(response.content, parser)

        soup = BeautifulSoup(response.content, "lxml")
        overview_element = soup.find("h5", id="overview")
        print(overview_element)

        for componente, xpath in xpath_composition.items():
            valor = tree.xpath(xpath)

            # Se o XPath retornar algum valor, pegamos o primeiro elemento
            valor_texto = valor[0].text.strip() if valor else "N/A"

            print(f"Componente: {componente}; Valor por 100g: {valor_texto}")
            time.sleep(3)

    except req.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

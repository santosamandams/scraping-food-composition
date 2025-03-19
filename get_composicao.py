import requests as req
from bs4 import BeautifulSoup
from lxml import etree

# code = read csv

#composicao do alimento com codigo
# url = "https://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto=BRC0003U"
# url = "https://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto={code}"


try:
    response = req.get(url)
    response.raise_for_status()

    # Usar lxml para analisar o HTML e habilitar XPath
    parser = etree.HTMLParser()
    tree = etree.fromstring(response.content, parser)

    # Selecionar o primeiro elemento <tr> usando XPath
    # primeiro_tr = tree.xpath('//*[@id="tabela1"]/tbody/tr[2]/td[0]')[0]
    # print(f"Primeiro TR: {primeiro_tr}")
    soup = BeautifulSoup(response.content, "lxml")
    overview_element = soup.find("h5", id="overview")
    print(overview_element)

    # firt_td = tree.xpath('//*[@id="tabela1"]/tbody/tr[8]/td[1]')[0]
    # print(f"componente: {firt_td.text}")
    #
    # # Selecionar o terceiro elemento <td> dentro do primeiro <tr> usando XPath
    # terceiro_td = tree.xpath('//*[@id="tabela1"]/tbody/tr[8]/td[3]')[0]
    # print(f"Terceiro TD: {terceiro_td.text}")

    # // *[ @ id = "tabela1"] / tbody / tr[2,4,5,6]
    # // *[ @ id = "tabela1"] / tbody / tr[4] / td[3]

except req.exceptions.RequestException as e:
    print(f"Erro ao acessar a URL: {e}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
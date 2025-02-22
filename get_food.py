from bs4 import BeautifulSoup
import requests as req

url = "https://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto=BRC0001C"
response = req.get(url)

if response.status_code == 200:
    content = response.text
    # print(content)
    soup = BeautifulSoup(content, features="lxml")
    # print(soup)
    print(soup.get_text())
else:
    print("Erro ao fazer a requisição:", response.status_code)



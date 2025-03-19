from bs4 import BeautifulSoup
import requests as req
import csv
from datetime import datetime

#lista de alimentos com codigo

url = "https://www.tbca.net.br/base-dados/composicao_alimentos.php"
# url = "https://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto=BRC0028C"
response = req.get(url)

response.encoding = "utf-8"
with open("data.html", "r", encoding="utf-8") as file:
    html_string = file.read()

soup = BeautifulSoup(html_string, "lxml")


# linhas
linhas = soup.find_all("tr")

#criar csv
now = datetime.now()
nome_arquivo = f"lote_{now.strftime('%Y%m%d_%H%M')}.csv"

# overview_element = soup.find("h5", id="overview")

if response.status_code == 200:
    # Iterar sobre as linhas e extrair o texto de cada célula
    # for linha in linhas:
    #     celulas = linha.find_all("td")
    #     for celula in celulas:
    #         texto = celula.get_text(strip=True)
    #         print(texto, end=" | ")  # Imprimir as células separadas por "|"
    #     print()  # Nova linha após cada linha da tabela
    # Escrever os dados no arquivo CSV
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=";")
        writer.writerow(["code", "name", "scientific_name", "group"])

        # Iterar sobre as linhas e extrair os dados
        for linha in linhas:
            celulas = linha.find_all("td")
            dados_linha = [celula.get_text(strip=True) for celula in celulas]
            writer.writerow(dados_linha[:4])  # pega somente as 4 primeiras colunas, pois as demais estao vazias.

    print(f"Arquivo CSV '{nome_arquivo}' criado com sucesso.")
else:
    print("Erro ao fazer a requisição:", response.status_code)
    # with open("https://thinking-tester-contact-list.herokuapp.com/l") as fp:
    # soup = BeautifulSoup(response.text)

# print(soup.prettify())


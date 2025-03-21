from bs4 import BeautifulSoup
import requests as req
import csv
from datetime import datetime

# main - vai juntar as informacoes e criar um dataset final


# step 2
with open("data/lote_test.csv", "r", newline='', encoding='utf-8') as csv_file:
    list_code = csv.reader(csv_file, delimiter=';')

    # for linha in list_code:
    #     print(linha[0])

    contador = 0
    for linha in list_code:
        if contador < 2: #começa em 2
            print(linha[0])
            contador += 1
        else:
            break

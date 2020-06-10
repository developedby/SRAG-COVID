"""
Exibe os casos e mortes de SRAG de uma cidade usando os dados do OpenDataSus

Modo de usar:
    Baixe os dados em https://opendatasus.saude.gov.br/dataset/bd-srag-2020
    Troque o valor de FILEPATH para o caminho até o arquivo baixado
    Troque CITYNAME para o nome do municipio que quer consultar (em caps)
    Troque STATE para o estado em que fica o municipio (abreviado e em caps)
    Rode o script (Python 3)

Autor: Nicolas Abril
Data de atualização: 10/06/2020
"""

import csv

FILEPATH = "./INFLUD_09-06-2020.csv"
STATE = 'PR'
CITYNAME = 'CURITIBA'

file = open(FILEPATH, 'r', newline='', encoding='windows-1252')
data = list(csv.DictReader(file, delimiter=';', strict=True))

cases_sars = 0
cases_covid = 0
deaths_sars = 0
deaths_influenza = 0
deaths_respiratory_other = 0
deaths_other = 0
deaths_unknown = 0
deaths_covid = 0
for case in data:
    if case['ID_MUNICIP'] == CITYNAME and case['SG_UF_NOT'] == STATE:
        cases_sars += 1

        if case['CLASSI_FIN'] == '5':
            cases_covid += 1

        if case['EVOLUCAO'] == '2':
            deaths_sars += 1
            if case['CLASSI_FIN'] == '1':
                deaths_influenza += 1
            elif case['CLASSI_FIN'] == '2':
                deaths_respiratory_other += 1
            elif case['CLASSI_FIN'] == '3':
                deaths_other += 1
            elif case['CLASSI_FIN'] == '4':
                deaths_unknown += 1
            elif case['CLASSI_FIN'] == '5':
                deaths_covid += 1
            else:
                print('ue')

print('Casos SRAG:', cases_sars)
print('Casos COVID:', cases_covid)
print('Mortes SRAG total:', deaths_sars)
print('Mortes SRAG influenza:', deaths_influenza)
print('Mortes SRAG outro respiratorio:', deaths_respiratory_other)
print('Mortes SRAG outro:', deaths_respiratory_other)
print('Mortes SRAG desconhecido:', deaths_unknown)
print('Mortes COVID:', deaths_covid)

file.close()
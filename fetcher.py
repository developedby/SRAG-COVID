"""
Exibe os casos e mortes de SRAG de uma cidade usando os dados do OpenDataSus

Modo de usar:
    Baixe os dados em https://opendatasus.saude.gov.br/dataset/bd-srag-2020
    Troque o valor de FILEPATH para o caminho até o arquivo baixado
    Troque CITYNAME para o nome do municipio que quer consultar (em caps)
    Troque STATE para o estado em que fica o municipio (abreviado e em caps)
    Rode o script (Python 3)

ATENCAO: Os dados de 16/06/2019 vieram com carateres invalidos que precisam ser deletados antes

Autor: Nicolas Abril
Data de atualização: 18/06/2020
"""

import csv

FILEPATH = "./INFLUD-16-06-2020-Revisado.csv"
STATE = 'PR'
CITYNAME = 'CURITIBA'

with open(FILEPATH, 'r', newline='', encoding='windows-1256') as file_cases:
    data = list(csv.DictReader(file_cases, delimiter=';', strict=True))

cases_sars = 0
cases_covid = 0
deaths_sars = 0
deaths_influenza = 0
deaths_respiratory_other = 0
deaths_other = 0
deaths_unknown = 0
deaths_covid = 0
death_no_cause = 0
for case in data:
    if case['ID_MUNICIP'] == CITYNAME and case['SG_UF_NOT'] == STATE:
        cases_sars += 1

        if case['CLASSI_FIN'] == '5':
            cases_covid += 1

        if case['EVOLUCAO'] == '2':
            deaths_sars += 1
            causa_morte = case['CLASSI_FIN']
            if causa_morte == '1':
                deaths_influenza += 1
            elif causa_morte == '2':
                deaths_respiratory_other += 1
            elif causa_morte == '3':
                deaths_other += 1
            elif causa_morte == '4':
                deaths_unknown += 1
            elif causa_morte == '5':
                deaths_covid += 1
            elif causa_morte == '':
                death_no_cause += 1
            else:
                print(f'Morte por motivo invalido encontrada: {repr(causa_morte)}')

print('Casos SRAG:', cases_sars)
print('Casos COVID:', cases_covid)
print('Mortes SRAG total:', deaths_sars)
print('Mortes SRAG influenza:', deaths_influenza)
print('Mortes SRAG outro respiratorio:', deaths_respiratory_other)
print('Mortes SRAG outro:', deaths_respiratory_other)
print('Mortes SRAG desconhecido:', deaths_unknown)
print('Mortes COVID:', deaths_covid)
print('Mortes sem causa registrada:', death_no_cause)
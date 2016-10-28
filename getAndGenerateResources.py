#!/usr/bin/env python3

import requests
from lxml import html

states = ("AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", 
    "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO")
    
baseUrl = "http://cidades.ibge.gov.br/download/mapa_e_municipios.php?lang=&uf={0}"

for uf in states:
    print("Obtendo cidades para o estado {0}...".format(uf))
    page = requests.get(baseUrl.format(uf))
    tree = html.fromstring(page.content)
    cities = tree.xpath("//td[@class='nome']/text()")
    
    file = open('{0}.xml'.format(uf), 'w')
    # file content
    file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    file.write('<resources>\n')
    file.write('\t<string-array name="{0}_cities">\n'.format(uf))
    
    city_str = '\t\t<item>{0}</item>\n'
    
    for city in cities:
        file.write(city_str.format(city))
    
    file.write('\t</string-array>\n')
    file.write('</resources>')
    
    file.close()    
    
    print('{0} cidades'.format(len(cities)))
    #break
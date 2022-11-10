import bs4 #Utilisation de beautifulsoup pour le scraping
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from urllib import request 
import sqlite3

conn = sqlite3.connect('champions.db')

@staticmethod
def leagueScrapping(role):

    cursor = conn.cursor()
    ml_url = "https://www.op.gg/champions?region=global&tier=platinum_plus&position=" + role

    request_text = request.urlopen(ml_url).read().decode('utf-8')
    page = bs4.BeautifulSoup(request_text, "html.parser")

    columns = []
    for column in page.find('main').findAll({'th'})[1:]:
        columns.append(column.text)

    # Itération sur les champions du rôle choisi
    for champion in page.find('main').find('tbody').findAll({'tr'}):
        championinfo = []
        counters = ""
        # Itération sur les différentes propriétés
        for column in champion.findAll({'td'})[1:]:
            if ('%' in column.text ):
                championinfo.append(float(column.text[0:-2]))

            elif (column.text != ''):
                championinfo.append(column.text)

        for counter in champion.findAll('img', {'width' : '24'}):
            counters += counter.get('alt')+', '
        
        counters = counters[0:-2]
        championinfo.append(counters)
        existSql = "Select name from " + role + " where name = \"" + championinfo[0] +"\""
        existQuery = cursor.execute(existSql)
        if existQuery.fetchall() == []:
            sql = "INSERT INTO " + role + " (name, tier, winrate, pickrate, banrate, counters) VALUES (?,?,?,?,?,?)"
            data = championinfo
            cursor.execute(sql, data)
            conn.commit()
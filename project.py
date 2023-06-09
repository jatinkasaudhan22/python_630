# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_EbyH9K7KEn3l20uRKcsxSzgIaZXL1ro
"""

# !pip install beautifulsoup4
# !pip install requests

from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup = BeautifulSoup(soup.text, "lxml")
soup

table_code = soup.table
table_code

tags = table_code.find_all('tr')
tags

data = []
for tag in tags:
    y = tag.text.split('\n')
    if y[1] != "":
        data.append(y[1:])
    
data

import csv
file = open('covid_data.csv','w')
x = csv.writer(file)
x.writerows(data)
file.close()

import pandas as pd
df = pd.read_csv('covid_data.csv',encoding = 'latin1')
df

countries = list(df['Country,Other'])
total_cases = df['TotalCases'] 
total_cases = list(map(lambda x:int(x.replace(',' , '')),list(df['TotalCases'] )))

#   !pip install plotly==5.14.1

import plotly.graph_objects as go

fig = go.Figure([go.Bar(x=countries[0:10], y=total_cases[0:10])])
fig.show()


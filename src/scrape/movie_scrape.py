#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='main')

elems = results.find_all('h3','lister-item-header')

movies=[]
for elem in elems:
    for y in elem.find_all('a'):
        print(y.text)
        movies.append(y.text)
df=pd.DataFrame(movies)
df.index = df.index + 1
df.to_csv('movies.csv') 

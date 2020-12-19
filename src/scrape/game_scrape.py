import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://store.steampowered.com/search/?filter=topsellers'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='search_resultsRows')

elems = results.find_all('span', class_='title')
games = []
for elem in elems:
    print(elem)
    print(elem.text)
    games.append(elem.text)
df = pd.DataFrame(games)
df.to_csv('games.csv') 
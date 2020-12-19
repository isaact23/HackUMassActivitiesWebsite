import requests
from bs4 import BeautifulSoup
import pandas as pd


# Find the best games from the Steam store and return as a dictionary.
def scrape_games() -> dict:
    try:
        URL = 'https://store.steampowered.com/search/?filter=topsellers'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id='search_resultsRows')

        elems = results.find_all('span', class_='title')
        games = {}
        for i, elem in enumerate(elems):
            games[i] = {"name": elem.text, "url": "TEST1", "img_url": "TEST2"}
            # games.append(elem.text)

        return games

    except:
        return {}

# df = pd.DataFrame(games)
# df.index = df.index + 1
# df.to_csv('games.csv')

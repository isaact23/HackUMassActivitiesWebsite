#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Find the best movies from IMDB and return as a dictionary.
def scrape_movies() -> dict:
    try:
        URL = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id='main')

        elems = results.find_all('h3','lister-item-header')
        movies = {}
        for elem in elems:
            for i, y in enumerate(elem.find_all('a')):
                movies[i] = {"name": y.text, "type": "Movie", "url": "TEST1", "img_url": "TEST2"}

        print(movies)
        return movies

    except:
        return {}

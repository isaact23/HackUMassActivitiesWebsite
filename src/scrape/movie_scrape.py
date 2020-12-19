#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Find the best movies from IMDB and return as a dictionary.
def scrape_movies() -> dict:
    URL = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='lister-list')

    elems = results.find_all('div', class_='lister-item mode-advanced')
    movies = {}
    for i, elem in enumerate(elems):
        header = elem.find('h3').find('a')
        name = header.text
        url = "https://www.imdb.com" + header['href']
        img_url = elem.find('div', class_='lister-item-image float-left').find('img')['alt']
        print(img_url)
        movies[i] = {"name": name, "type": "Movie", "url": url, "img_url": img_url}

    return movies
    '''try:
        
    except:
        print("There was an error.")
        return {}'''

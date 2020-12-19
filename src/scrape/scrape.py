#!/usr/bin/env python3
from src.scrape import game_scrape, movie_scrape

# Get necessary data from internet and sort it.
def get_activity_data():
    game_data = game_scrape.scrape_games()
    return game_data
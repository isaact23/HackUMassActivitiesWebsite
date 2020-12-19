#!/usr/bin/env python3
from src.scrape import game_scrape, movie_scrape


# Get necessary data from internet and sort it. Called by App.js.
def get_activity_data():
    # Scrape internet for data
    game_data = game_scrape.scrape_games()
    movie_data = movie_scrape.scrape_movies()

    # Merge all data into one dictionary
    all_data = []
    for i in range(len(game_data)):  # game_data:
        all_data.append(game_data[i])
    for i in range(len(movie_data)):  # movie_data:
        all_data.append(movie_data[i])

    # Sort alphabetically
    print(all_data)
    all_data = sorted(all_data, key=lambda entry: entry['name'])
    print(all_data)

    # Convert to dictionary form
    data_dict = {}
    for i in range(len(all_data)):
        data_dict[i] = all_data[i]

    # Send data to App.js to be constructed in HTML form.
    return data_dict

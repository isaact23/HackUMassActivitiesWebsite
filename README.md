# stufftodo.tech

Find all of the latest activities and things to do at stufftodo.tech.
From sports to books to video games, you won't miss a thing. The website
constantly scrapes the internet for the latest activities and consolidates
them in one place!

## The Tools
stufftodo.tech uses several tools:
* React.JS - a frontend library developed by Facebook. Users can change
filters on the homepage and see activities update in real time.
* HTML, CSS & JavaScript for web design.
* Flask - a backend library for Python. Realtime data is scraped from
popular websites and consolidated into one directory.
* Python for internet scraping.
* Domain.com for our stufftodo.tech domain.
* Google Cloud to host our website, complete with ReactJS and Flask.

## The Code

### `/flask-api/`
Contains a virtual environment for Python 3.7.9 and an app.py script that
serves as a Flask backend for the project. The script queries
`/src/scrape/scrape.py` to mine the internet for glorious boredom-ending
activities.

### `/public/`
Contains data exposed to the client, namely index.html.

### `/src/`
The code for the React application. `index.js` is called first, which calls
`App.js` to generate HTML for the activity elements. `App.js` also communicates
with the Flask backend to get the latest activities.

### `/src/scrape/`
The real meat and potatoes of the algorithm. `scrape.py` calls other files
such as `game_scrape.py` and `movie_scrape.py` to check popular websites
for up-to-date activities. The data is filtered and compiled into a dictionary.
Finally, `/src/App.js` reads the dictionary to generate HTML for the activities.

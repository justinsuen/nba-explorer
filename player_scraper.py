from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# change this to scrape the player you want
name = "Luke Jackson"

all_players = pd.DataFrame.from_csv("./all_players.csv")
url_list = [url for url in all_players[all_players['name'] == name]['player_url']]
bref_url_list = ["http://www.basketball-reference.com/{0}".format(url) for url in url_list]

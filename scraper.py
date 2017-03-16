from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

players_name = []
players_url = []

for al in alph:
    print("Getting players '{0}' last names".format(al))
    response = requests.get("http://www.basketball-reference.com/players/{0}/".format(al))

    soup = BeautifulSoup(response.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    players = body.select("tbody th a")

    players_name = np.concatenate((players_name, [player.get_text() for player in players]))
    players_url = np.concatenate((players_url, [player['href'] for player in players]))

all_players = pd.DataFrame({
    "name": players_name,
    "player_url": players_url
})

all_players.to_csv(path_or_buf="./all_players.csv")

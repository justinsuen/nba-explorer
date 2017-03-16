from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

players_name = []
players_url = []
players_year_min = []
players_year_max = []
players_pos = []
players_ht = []
players_wt = []

for al in alph:
    print("Getting players '{0}' last names".format(al))
    response = requests.get("http://www.basketball-reference.com/players/{0}/".format(al))

    soup = BeautifulSoup(response.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]

    players = body.select("tbody th a")
    year_min = soup.findAll("td", {"data-stat": "year_min"})
    year_max = soup.findAll("td", {"data-stat": "year_max"})
    pos = soup.findAll("td", {"data-stat": "pos"})
    ht = soup.findAll("td", {"data-stat": "height"})
    wt = soup.findAll("td", {"data-stat": "weight"})

    players_name = np.concatenate((players_name, [player.get_text() for player in players]))
    players_url = np.concatenate((players_url, [player['href'] for player in players]))
    players_year_min = np.concatenate((players_year_min, [stat.get_text() for stat in year_min]))
    players_year_max = np.concatenate((players_year_max, [stat.get_text() for stat in year_max]))
    players_pos = np.concatenate((players_pos, [stat.get_text() for stat in pos]))
    players_ht = np.concatenate((players_ht, [stat.get_text() for stat in ht]))
    players_wt = np.concatenate((players_wt, [stat.get_text() for stat in wt]))

all_players = pd.DataFrame({
    "name": players_name,
    "player_url": players_url,
    "players_year_min": players_year_min,
    "players_year_max": players_year_max,
    "players_pos": players_pos,
    "players_ht": players_ht,
    "players_wt": players_wt
})

all_players.to_csv(path_or_buf="./all_players.csv")

"""
This file contains the code for generating ajective and noun cards.
"""
import random
import requests
from bs4 import BeautifulSoup
import pandas as pd

green_cards_url = "http://www.com-www.com/applestoapples/applestoapples-green-with.html"
red_cards_url = "http://www.com-www.com/applestoapples/applestoapples-red-with.html"

def get_green_cards(green_cards_url: str = green_cards_url) -> list:
    exclude = {'Apples To Apples'}
    response = requests.get(green_cards_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    green_strings = soup.find_all('b')
    cards = {card.get_text(strip=True) for card in green_strings} - exclude

    return sorted(list(cards))


def get_red_cards(red_cards_url: str = red_cards_url) -> list:
    exclude = {'Apples To Apples'}
    response = requests.get(red_cards_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    red_strings = soup.find_all('b')
    cards = {card.get_text(strip=True) for card in red_strings} - exclude
    return list(cards)

def sampled_cards(cards: list, n: int, seed: int = 42) -> list:
    random.seed(seed)
    return random.sample(cards, n)

adjs = get_green_cards()
adjs_df = pd.DataFrame(adjs, columns=["adj"])
adjs_df.to_csv("adjs.csv", index=False)
nouns = sampled_cards(get_red_cards(), 30)
nouns_df = pd.DataFrame(nouns, columns=["noun"])
nouns_df.to_csv("nouns.csv", index=False)

adj_nouns_cards = [f"{adj} {noun}" for adj in adjs for noun in nouns]
print(adj_nouns_cards)

adj_nouns_df = pd.DataFrame(adj_nouns_cards, columns=["adj_noun"])
adj_nouns_df.to_csv("adj_nouns_cards.csv", index=False)

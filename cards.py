"""
This file contains the code for generating ajective and noun cards.
"""
import random
import requests
from bs4 import BeautifulSoup

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

adjs = get_green_cards()[:10]
nouns = sampled_cards(get_red_cards(), 10)

adj_nouns_cards = [f"{adj} {noun}" for adj in adjs for noun in nouns]

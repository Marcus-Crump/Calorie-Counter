# An application to take a given list of main ingredients in a dish and give a caloric break down and a total

# It will store this info in a list **TODO how will this work for portions, are you going to make mom calaculate it**

# Ideally, I want the program to take the measurements the user is putting in and figure out how many calories it has

import requests as req
from bs4 import BeautifulSoup as bs
import PyQt5 as gui

def get_soup(url):
    response = req.get(url)
    soup = bs(response.text,'html.parser')
    response.close()
    return soup

def get_food_url(food_split):
    url = "https://www.myfooddata.com/search?search="
    r = len(food_split)
    for i in range(r):
        url += food_split[i]
        if i + 1 < r:
            url+="%20"
    return url

def get_calories(soup):
    return soup.find('td', class_="nft-cal-amt ENERC_KCAL").text.strip()

def get_item_URL(food_split):
    url = get_food_url(food_split)
    soup = get_soup(url)
    link = soup.find("a", class_="searchlink")
    return link.text.strip()
    


def get_food_data(food):
    item_URL = get_item_URL(food.split())
    item_URL = item_URL[:len(item_URL)-3] + "100g/1"
    soup = get_soup(item_URL)
    kcal = get_calories(soup)
    return kcal

def main():
    foods = ["roast chicken","fusilli", "unsalted butter", "olive oil", "dried basil", "dried oregano"]
    for item in foods:
        print(get_food_data(item))


if __name__ == "__main__":
    main()

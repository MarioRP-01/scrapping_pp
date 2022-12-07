from bs4 import BeautifulSoup
import requests

import scrapping_pp.common.viewer as viewer

def scrap_amazon(headers):

    ITEM = "playstation+4"
    URL = "https://www.amazon.es/s?k=" + ITEM + "&ref=nb_sb_noss_2"

    webpage = requests.get(URL, headers=headers)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    data = __scrap(soup)
    viewer.view(data)

def __scrap(soup):
    return []
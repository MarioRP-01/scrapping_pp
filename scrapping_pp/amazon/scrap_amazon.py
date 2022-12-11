from bs4 import BeautifulSoup
import cloudscraper

import scrapping_pp.common.viewer as viewer

def scrap_amazon(headers):

    ITEM = "playstation+4"
    scraper = cloudscraper.create_scraper()

    __general_information(scraper, ITEM)

    # links = list(map(lambda link: link.get('href'), links))


def __scrap(soup):
    return []

def __general_information(scraper, item):
    URL = "https://www.amazon.es/s?k=" + item + "&ref=nb_sb_noss_2"
    webpage = scraper.get(URL)

    print(webpage)

    soup = BeautifulSoup(webpage.content, "lxml")
    items_data = soup.find_all("div", attrs={'data-component-type':'s-search-result'})

    items_data = list(map(__extract_general_information, items_data))

    # TODO: Delete later
    for item in items_data:
        print(item)
        print()

    return items_data

def __extract_general_information(item_data: BeautifulSoup):
    # TODO: Extract title
    product_title = item_data.select_one("span.a-price-whole")
    if product_title is not None:
        product_title
    # TODO: Extract price
    # TODO: Extract valoration
    # TODO: Extract availability (if exist)
    return [product_title]

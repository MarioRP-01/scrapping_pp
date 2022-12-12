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
    product_title = item_data.select_one("span.a-size-base-plus")
    if product_title is not None:
        product_title = product_title.string.strip()

    product_price = item_data.select_one("span.a-price-whole")
    if product_price is not None:
        product_price = product_price.string.strip()

    product_valoration = item_data.select_one("span[aria-label] span[class=\"a-size-base\"]")
    if product_valoration is not None:
        product_valoration = product_valoration.string.strip()

    product_availability = item_data.select_one("span[aria-label] span.a-size-base.s-underline-text")
    if product_availability is not None:
        product_availability = product_availability.string.strip()[1:-1]

    return [product_title, product_price, product_valoration, product_availability]

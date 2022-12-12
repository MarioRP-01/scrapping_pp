import sys
from bs4 import BeautifulSoup

import scrapping_pp.common.viewer as viewer
from cloudscraper import CloudScraper

def scrap_amazon(scraper: CloudScraper, item = None, pages = 0):

    if (item is None and isinstance(item, str)): return
    if (not isinstance(pages, int)): return

    pages = abs(pages)
    response, status = __scrap(scraper, item, pages)

    # TODO: Delete later
    for (i, items), ok in zip(enumerate(response), status):
        print("\n---\nPage ", i, " | Status ", ok, "\n---\n")
        for item in items:
            print(item, "\n")


def __scrap(scraper: CloudScraper, item, pages):

    response = []
    status = []

    for i in range(1, pages + 1):
        pages_message = "page=" + str(i)
        URL = "https://www.amazon.es/s?k=" + item + "&" + pages_message + "&ref=nb_sb_noss_2"

        while (True):
            webpage = scraper.get(URL)
            if webpage.status_code == 200: break

        status.append(webpage.status_code)
        response.append(__general_information(webpage))

    return response, status


def __general_information(webpage):

    soup = BeautifulSoup(webpage.content, "lxml")
    items_data = soup.find_all("div", attrs={'data-component-type':'s-search-result'})

    items_data = list(map(__extract_general_information, items_data))

    return items_data


def __extract_general_information(item_data: BeautifulSoup):

    product_title = item_data.select_one("span.a-size-base-plus")
    if product_title is not None:
        product_title = product_title.string.strip()
    else:
        product_title = item_data.select_one("h2.s-line-clamp-3")
        if product_title is not None:
            product_title = product_title.string.strip()

    product_link = item_data.select_one(".s-no-outline")
    if product_link is not None:
        product_link = product_link.get("href")
    else:
        product_link = item_data.select_one("a[title=\"product-image\"]")
        if product_link is not None:
            product_link = product_link.get("href").strip()

    product_price = item_data.select_one("span.a-price-whole")
    if product_price is not None:
        product_price = product_price.string.strip()

    product_valoration = item_data.select_one("span[aria-label] span[class=\"a-size-base\"]")
    if product_valoration is not None:
        product_valoration = product_valoration.string.strip()
    else:
        product_valoration = item_data.select_one("i span.a-icon-alt")
        if product_valoration is not None:
            product_valoration = product_valoration.string.strip().split()[0]

    product_availability = item_data.select_one("span[aria-label] span.a-size-base.s-underline-text")
    if product_availability is not None:
        product_availability = product_availability.string.strip()[1:-1]
    else:
        product_availability = item_data.select_one("span[aria-label] span.puis-light-weight-text")
        if product_availability is not None:
            product_availability = product_availability.string.strip()[1:-1]

    return [product_title, product_link, product_price, product_valoration, product_availability]

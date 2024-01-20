# import amazon
import sys
import scrapping_pp.amazon.scrap_amazon as amazon
import cloudscraper

if __name__ == '__main__':

    arguments = sys.argv
    
    if (len(arguments) < 2 or len(arguments) > 3): sys.exit()

    scraper = cloudscraper.create_scraper()

    if (len(arguments) == 2):
        amazon.scrap_amazon(scraper, arguments[1])
        sys.exit()

    amazon.scrap_amazon(scraper, arguments[1], int(arguments[2]))

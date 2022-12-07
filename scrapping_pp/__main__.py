# import amazon
import scrapping_pp.amazon.scrap_amazon as amazon

if __name__ == '__main__':

    HEADERS = ({
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Accept-Language": "es-ES"
    })

    amazon.scrap_amazon(HEADERS)
    

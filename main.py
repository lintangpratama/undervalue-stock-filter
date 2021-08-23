# Importing the library
from undervalueStock import UndervalueStock
from emitenList import emitensCode

# Initialize Scrapingdog API key (scrapingdog.com)
# Scrappingdog is a web scrapper that let you used the scrapping API for free (max: 1000 request) 
api_key = 'YOUR API CODE HERE (STRING)'

undervalue_stock = UndervalueStock(api_key, emitensCode)

def main():
    undervalue_stock.filter()

if __name__ == "__main__":
    main()
# Importing the library
import random
from undervalueStock import UndervalueStock
from emitenList import emitensCode

# Initialize Scrapingdog API key (scrapingdog.com)
# Scrappingdog is a web scrapper that let you used the scrapping API for free (max: 1000 request) 
api_key = 'YOUR API CODE HERE (STRING)'

undervalue_stock = UndervalueStock(api_key, random.sample(emitensCode, len(emitensCode)))

def main():
    print('IHSG Undervalue Stocks Filter:')
    undervalue_stock.filter(per=15, dividen=2)

if __name__ == "__main__":
    main()
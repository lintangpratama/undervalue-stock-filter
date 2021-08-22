import requests
from bs4 import BeautifulSoup
from emitenList import emitensCode

class UndervalueStock():
    def __init__(self, apiKey):
        self.ihsg = list()
        self.emiten = {}
        self.apiKey = apiKey

    def filter(self, pbv = 1, per = 10, dividen = 5):
        for i in range(len(emitensCode)):
    # Get the API url
    # Data get from Yahoo! Finance
    # Using ScrapingDog for scrap the data that we want to use
            url = requests.get(f"https://api.scrapingdog.com/scrape?api_key={self.apiKey}&url=https://finance.yahoo.com/quote/{emitensCode[i]}/key-statistics?p={emitensCode[i]}").text
            soup = BeautifulSoup(url, "html.parser")
            data = soup.find_all("tbody")
            name = soup.find_all("h1")
            
            # Initialize the dictionary and list to contain the data that we get
            emiten = {}
            ihsg = list()

            # Add the emiten name from h1 tag
            try:
                emiten['Name'] = name[0].text

                # Find the PBV, PER, and dividend yield data from tr table and td class
                # PER and PBV table
                valuation_table = data[0].find_all("tr")
                # Dividend yield table
                dividend_table = data[3].find_all('tr')

                # Find the td table from td tags
                table_td_PER = valuation_table[2].find_all("td")
                table_td_PBV = valuation_table[6].find_all("td")
                table_dividend_yield = dividend_table[1].find_all("td")
                
                # Replace the '%' in dividend yield and turn it into float for logical expression later
                dividend_yield = table_dividend_yield[1].text.replace('%', '')
                dividend_yield = float(dividend_yield)   

                # Add an emitent data (PER, PBV, and dividend yield) to IHSG list
                emiten[table_td_PER[0].text] = float(table_td_PER[1].text)
                emiten[table_td_PBV[0].text] = float(table_td_PBV[1].text)
                emiten[table_dividend_yield[0].text] = table_dividend_yield[1].text
            except:
                continue
            
            ihsg.append(emiten)
    
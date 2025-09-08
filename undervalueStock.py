import requests
from bs4 import BeautifulSoup
from emitenList import emitensCode

class UndervalueStock():
    '''Use scrapingdog.com API key for the argument'''
    def __init__(self, apiKey, emitenList):
        self.emitensList = emitenList
        self.ihsg = list()
        self.apiKey = apiKey
        self.output = 0

    def filter(self, size = 10, pbv = 1, per = 10, dividen = 5):
        if (isinstance(pbv, int) or isinstance(pbv, float)) and (isinstance(per, int) or isinstance(per, float)) and (isinstance(dividen, int) or isinstance(dividen, float)):
            counter = 0
            for i in range(len(self.emitensList)):
                '''Filtering the undervalue stock by PBV, PER, and dividen yield. 
                pbv (Price to Book Value) -> int
                per (Price to Earning Ratio -> int
                dividen -> int'''
                
                # Checking the size of output
                if self.output < size:
                    # Get the API url
                    # Data get from Yahoo! Finance
                    # Using ScrapingDog for scrap the data that we want to use
                    url = requests.get(f"https://api.scrapingdog.com/scrape?api_key={self.apiKey}&url=https://finance.yahoo.com/quote/{self.emitensList[i]}/key-statistics?p={self.emitensList[i]}").text
                    soup = BeautifulSoup(url, "html.parser")
                    data = soup.find_all("tbody")
                    name = soup.find_all("h1")
                    emiten = {}

                    # Add the self.emiten name from h1 tag
                    try:
                        emiten['Name'] = name[0].text
                        if emiten['Name'] == 'Yahoo':
                            continue

                        # Find the PBV, PER, and dividend yield data from tr table and td class
                        # PER and PBV table
                        valuation_table = data[0].find_all("tr")
                        # Dividend yield table
                        dividend_table = data[3].find_all("tr")

                        # Find the td table from td tags
                        table_td_PER = valuation_table[2].find_all("td")
                        table_td_PBV = valuation_table[6].find_all("td")
                        table_dividend_yield = dividend_table[1].find_all("td")
                        
                        # Replace the '%' in dividend yield and turn it into float for logical expression later
                        dividend_yield = table_dividend_yield[1].text.replace('%', '')
                        dividend_yield = float(dividend_yield)   

                        # Add an self.emitent data (PER, PBV, and dividend yield) to self..ihsg list
                        emiten[table_td_PER[0].text] = float(table_td_PER[1].text)
                        emiten[table_td_PBV[0].text] = float(table_td_PBV[1].text)
                        emiten[table_dividend_yield[0].text] = table_dividend_yield[1].text
                    except:
                        continue
                else:
                    break
                
                self.ihsg.append(emiten)

                # Output
                if 0 <= self.ihsg[counter]['Trailing P/E '] <= per and 0 <= self.ihsg[counter]['Price/Book (mrq)'] <= pbv and dividend_yield >= dividen:
                    print('-', self.ihsg[counter]['Name'])
                    print('  PER:', self.ihsg[counter]['Trailing P/E '])
                    print('  PBV:', self.ihsg[counter]['Price/Book (mrq)'])
                    print('  Dividend Yield:', self.ihsg[counter]['Forward Annual Dividend Yield 4'])
                    self.output += 1
                
                counter += 1 

        else:
            raise TypeError("Only integers are allowed")

        print('Enough')
    

# Importing the library
import requests
from bs4 import BeautifulSoup
from emitenList import emiten_code # Import the emiten code from emitenList.py from the same folder

# Initialize Scrapingdog API key
# Scrappingdog is a web scrapper that let you used the scrapping API for free (max: 1000 request) 
api_key = 'YOUR SCRAPPINGDOG.COM API CODE'

# Title
print('')
print('IHSG Undervalue Emitent (0<PER<15 and 0<PBV<1) List:')

for i in range(len(emiten_code)):
    # Get the API url
    # Data get from Yahoo! Finance
    # Using ScrapingDog for scrap the data that we want to use
    url = requests.get(f"https://api.scrapingdog.com/scrape?api_key={api_key}&url=https://finance.yahoo.com/quote/{emiten_code[i]}/key-statistics?p={emiten_code[i]}").text
    soup = BeautifulSoup(url, "html.parser")
    data = soup.find_all("tbody")
    name = soup.find_all("h1")
    
    # Initialize the dictionary and list to contain the data that we get
    emiten = {}
    ihsg = list()

    # Add the emiten name from h1 tag
    try:
      emiten['Name'] = name[0].text
    except:
      pass

    # Find the PBV, PER, and dividend yield data from tr table and td class
    try:
       # PER and PBV table
       valuation_table = data[0].find_all("tr")
       # Dividend yield table
       dividend_table = data[3].find_all('tr')
    except:
       valuation_table = None
       dividend_table = None

    # Find the td table from td tags
    try:
       table_td_PER = valuation_table[2].find_all("td")
       table_td_PBV = valuation_table[6].find_all("td")
       table_dividend_yield = dividend_table[1].find_all("td")
    except:
       table_td_PER = None
       table_td_PBV = None  
       table_dividend_yield = None
    
    # Replace the '%' in dividend yield and turn it into float for logical expression later
    try:
      dividend_yield = table_dividend_yield[1].text.replace('%', '')
      dividend_yield = float(dividend_yield)   
    except: 
      pass

    # Add an emitent data (PER, PBV, and dividend yield) to IHSG list
    try:
      emiten[table_td_PER[0].text] = float(table_td_PER[1].text)
      emiten[table_td_PBV[0].text] = float(table_td_PBV[1].text)
      emiten[table_dividend_yield[0].text] = table_dividend_yield[1].text
    except:
      pass
    ihsg.append(emiten)

    try:
      if 0 <= ihsg[0]['Trailing P/E '] <= 15 and 0 <= ihsg[0]['Price/Book (mrq)'] <= 1 and dividend_yield >=1:
          print('-', ihsg[0]['Name'])
          print('  PER:', ihsg[0]['Trailing P/E '])
          print('  PBV:', ihsg[0]['Price/Book (mrq)'])
          print('  Dividend Yield:', ihsg[0]['Forward Annual Dividend Yield 4'])
          print('')
    except:
      pass


print('')
print('Thanks for using this program :)')
print('Data was got from Yahoo! Finance')
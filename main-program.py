# Importing the library
import requests
from bs4 import BeautifulSoup
from emitenList import emiten_code

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

    # Find the PBV and PER data from tr table and td class
    try:
       table = data[0].find_all("tr")
    except:
       table = None

    try:
       table_td_PER = table[2].find_all("td")
       table_td_PBV = table[6].find_all("td")
    except:
       table_td_PER = None
       table_td_PBV = None
      
    # Add the PBV and PER data to the emitent dictionary
    try:
      emiten['Name'] = name[0].text
    except:
      pass
    # Add an emitent data to IHSG list
    try:
      emiten[table_td_PER[0].text] = float(table_td_PER[1].text)
      emiten[table_td_PBV[0].text] = float(table_td_PBV[1].text)
    except:
      pass
    ihsg.append(emiten)

    try:
      if 0 <= ihsg[0]['Trailing P/E '] <= 15 and 0 <= ihsg[0]['Price/Book (mrq)'] <= 1:
          print('-', ihsg[0]['Name'])
    except:
      pass


print('')
print('Thanks for using this program :)')
print('Data was got from Yahoo! Finance')
# Importing the library
from bs4 import BeautifulSoup
import requests


# Dictionary url for each emitent
# You can add the url by change the emitent code, ex: ADHI.JK to BBCA.JK or something
allurl = ["https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/ADHI.JK/key-statistics?p=ADHI.JK", 
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/PTRO.JK/key-statistics?p=PTRO.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/TBLA.JK/key-statistics?p=TBLA.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/IGAR.JK/key-statistics?p=IGAR.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/SMSM.JK/key-statistics?p=SMSM.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/MLPT.JK/key-statistics?p=MLPT.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/LINK.JK/key-statistics?p=LINK.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/TINS.JK/key-statistics?p=TINS.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/POWR.JK/key-statistics?p=POWR.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/BJTM.JK/key-statistics?p=BJTM.JK",
         "https://api.scrapingdog.com/scrape?api_key=60304c8757fd5d19cf3ddf3b&url=https://finance.yahoo.com/quote/BBCA.JK/key-statistics?p=BBCA.JK"]

print('IHSG Undervalue Emitent (0<PER<15 and 0<PBV<1) List:')

for i in range(len(allurl)):
    # Get the API url
    # Data get from Yahoo! Finance
    # Using ScrapingDog for scrap the data that we want to use
    url = requests.get(allurl[i]).text
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
    emiten['Name'] = name[0].text
    emiten[table_td_PER[0].text] = float(table_td_PER[1].text)
    emiten[table_td_PBV[0].text] = float(table_td_PBV[1].text)

    # Add an emitent data to IHSG list
    ihsg.append(emiten)

    # Filtering an undervalued emitent
    if 0 <= ihsg[0]['Trailing P/E '] <= 15 and 0 <= ihsg[0]['Price/Book (mrq)'] <= 1:
        print(ihsg[0]['Name'])
    else:
        print(ihsg[0]['Name'], "WAS OVERVALUED!")

print('Thanks for using this program :)')
print('Data was got from Yahoo! Finance')
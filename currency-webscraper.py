import bs4
import pandas as pd 
import requests

URL = 'https://uk.finance.yahoo.com/currencies'
COLUMNS = ['cy-pair', 'rate']

def get_webpage(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text, 'html.parser')

def scrape(webpage):
    rows = webpage.find("table").find_all("tr")
    cy_data = []
    for row in rows:
        cells = row.find_all("td")[1:3]
        cy_data.append([cell.text for cell in cells])
    return pd.DataFrame(cy_data, columns=COLUMNS).drop(0, axis=0)

if __name__ == "__main__":
    page = get_webpage(URL)
    data = scrape(page)
    print(data)

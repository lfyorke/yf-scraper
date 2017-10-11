import bs4
import pandas as pd 
import requests

URL = 'https://widget-yahoo.ofx.com/resources/1500309750700/data/localizations/USA.json'
POST_URL = 'https://adsynth-ofx-quotewidget-prod.herokuapp.com/api/1'
COLUMNS = ['cy-pair', 'rate']

def get_webpage(url):
    return requests.get(url).json()


def get_list_of_cys(response):
    return [x.split("-")[0].strip() for x in response.keys() if x.endswith("- Description")]


def filter_cys(currencies):
    allowed = set(['GBP', 'USD', 'EUR'])
    return list(allowed & set(currencies))


def post_loop(currencies):
    results = []
    for base in currencies:
        for term in currencies:
            data = {"method": "spotRateHistory", "data": {"base": base, "term": term, "period": "day"}}
            f = requests.post(POST_URL, json=data).json()
            try:
                results.append([base + term, f['data']['CurrentInterbankRate']])
            except:
                pass
    return pd.DataFrame(results, columns=COLUMNS)


if __name__ == "__main__":
    webpage = get_webpage(URL)
    currencies = get_list_of_cys(webpage)
    filtered = filter_cys(currencies)
    data = post_loop(filtered)

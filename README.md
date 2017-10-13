# yf-scraper
Yahoo Finance currency exchange rates webscraper

## currency-webscraper.py
This script will go to Yahoo Finance's [currency website](https://uk.finance.yahoo.com/currencies) and fetch the current list of fx pairs and their assosciated rates.

It returns a pandas dataframe like the following table:

|    |cy-pair|   rate   |
|:--:|:-----:|:--------:|
|1   |GBP/USD|      1.32|
|2   |GBP/EUR|    1.1188|
|3   |EUR/USD|      1.18|
|4   |GBP/JPY|  148.1754|

## yf-post.py
This script will go to [here](https://widget-yahoo.ofx.com/) and extract a list of currencies, an then use that list to make POST requests for each currency pair to retrieve the correct rate.  This is a more thorough script that can return a bigger list of currency pairs.


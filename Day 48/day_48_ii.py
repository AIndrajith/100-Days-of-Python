# Using requests and BeautifulSoup for Scraping

import requests
from bs4 import BeautifulSoup
import time    

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


# print(fetch_page("https://www.udemy.com/cart/success/2110435977/"))    


# Extracting Stock Prices from a Website

def get_stock_price(ticker):
    url = f"httpps://finance.yahoo.com/qoute{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    
    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", {"data-symbol": ticker, "data-field":"regularMarketPrice"})
    if price_tag:
        return price_tag.text
    else:
        print("Stock price not forund")
        return None

def track_stock_price(ticker, interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}: ${price}")
        time.sleep(interval)    


ticker = "AAPL"
track_stock_price(ticker, 2)

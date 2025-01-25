import requests
from bs4 import BeautifulSoup

BASE_URL = "https://finance.yahoo.com/quote"

def scrape_crypto_data(symbol: str) -> dict:
    response = requests.get(f"{BASE_URL}/{symbol}/")
    if response.status_code != 200:
        print(f"Failed to fetch data for {symbol}.")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}

    try:
        data['Price'] = soup.find('span', {'data-testid': 'qsp-price'}).text.strip()
        data['Change'] = soup.find('span', {'data-testid': 'qsp-price-change'}).text.strip()
        data['Change Percent'] = soup.find('span', {'data-testid': 'qsp-price-change-percent'}).text.replace("(", "").replace(")", "").strip()
        data['Previous Close'] = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'}).text.strip()
        data['Open'] = soup.find('fin-streamer', {'data-field': 'regularMarketOpen'}).text.strip()
        data['Market Cap'] = soup.find('fin-streamer', {'data-field': 'marketCap'}).text.strip()
        data['Volume'] = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'}).text.strip()
    except Exception as e:
        print(f"Failed to scrape data for {symbol}: {e}")

    return data
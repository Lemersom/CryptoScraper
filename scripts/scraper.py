import requests
from bs4 import BeautifulSoup

BASE_URL = "https://finance.yahoo.com/quote"

def scrape_crypto_data(symbol: str) -> dict:
    """
    Scrapes cryptocurrency data from Yahoo Finance for a given symbol.

    Args:
        symbol (str): The cryptocurrency symbol (e.g., 'BTC-USD').

    Returns:
        dict: A dictionary containing the scraped data, including:
              - 'Price': Current price of the cryptocurrency.
              - 'Change': Absolute change in price.
              - 'Change Percent': Percentage change in price.
              - 'Previous Close': Previous closing price.
              - 'Open': Opening price.
              - 'Market Cap': Market capitalization.
              - 'Volume': Trading volume.
              
              If scraping fails, returns an empty dictionary.
    """
    data = {}
    print(f"Scraping data for '{symbol}'...")
    try:
        response = requests.get(f"{BASE_URL}/{symbol}/")
        response.raise_for_status() # Raise an HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')

        data['Price'] = soup.find('span', {'data-testid': 'qsp-price'}).text.strip()
        data['Change'] = soup.find('span', {'data-testid': 'qsp-price-change'}).text.strip()
        data['Change Percent'] = (
            soup.find('span', {'data-testid': 'qsp-price-change-percent'})
            .text.replace("(", "").replace(")", "").strip()
        )
        data['Previous Close'] = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'}).text.strip()
        data['Open'] = soup.find('fin-streamer', {'data-field': 'regularMarketOpen'}).text.strip()
        data['Market Cap'] = soup.find('fin-streamer', {'data-field': 'marketCap'}).text.strip()
        data['Volume'] = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'}).text.strip()
    except requests.RequestException as e:
        print(f"Request error for {symbol}: {e}")
    except AttributeError as e:
        print(f"Failed to locate a data field for {symbol}: {e}")
    except Exception as e:
        print(f"Failed to scrape data for {symbol}: {e}")

    return data
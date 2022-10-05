import datetime
import requests as req

HOSTNAME = '127.0.0.1:8000'
USER = 'admin'
PASS = 'temporal2022'


def create_session_and_call(url_path):
    session = req.Session()
    session.auth = (USER, PASS)

    return session.get("http://" + HOSTNAME + url_path)


def get_all_coins_from_api():
    """
        Returns all the Crypto Coins registered in the DataBase in json format
    """
    response = create_session_and_call("/coins/")
    return response.json()


def get_coin_names_and_symbols():
    """
        Returns all Crypto Coins names, symbols and counts from API in json format
    """
    response = create_session_and_call("/coins/list_names_symbols/")
    return response.json()


def get_close_price(coin, date):
    """
        Returns the Close price for the given coin and date
    """
    response = create_session_and_call(f"/coins/close_price/{coin}/{date}/")
    json_response = response.json()
    if not json_response:
        return "There is not Close price for those selected options"

    close_price = json_response[0]['close']
    return str(close_price)


def get_min_max_dates():
    response = create_session_and_call("/min_and_max/")

    min_date = response.json()['min_date']
    max_date = response.json()['max_date']
    fmin = datetime.datetime.strptime(min_date, "%Y-%m-%dT%H:%M:%SZ")
    fmax = datetime.datetime.strptime(max_date, "%Y-%m-%dT%H:%M:%SZ")

    return fmin, fmax

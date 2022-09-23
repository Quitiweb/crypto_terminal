import requests as req

HOSTNAME = '127.0.0.1:8000'
USER = 'admin'
PASS = 'temporal2022'


def get_all_coins_from_api():
    """
        Returns all the Crypto Coins registered in the DataBase in json format
    """
    session = req.Session()
    session.auth = (USER, PASS)

    response = session.get("http://" + HOSTNAME + "/coins/")
    return response.json()


def get_coin_names_and_symbols():
    """
        Returns all Crypto Coins names, symbols and counts from API in json format
    """
    session = req.Session()
    session.auth = (USER, PASS)

    response = session.get("http://" + HOSTNAME + "/coins/list_names_symbols/")
    return response.json()


def get_close_price(coin, date):
    """
        Returns the Close price for the given coin and date
    """
    session = req.Session()
    session.auth = (USER, PASS)

    response = session.get("http://" + HOSTNAME + f"/coins/close_price/{coin}/{date}/")
    json_response = response.json()
    if not json_response:
        return "There is not Close price for those selected options"

    close_price = json_response[0]['close']
    return str(close_price)

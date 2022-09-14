import requests as req

HOSTNAME = '127.0.0.1:8000'


def get_all_coins_from_api():
    """
        Returns all the Crypto Coins registered in the DataBase in json format
    """
    session = req.Session()
    session.auth = ('admin', 'temporal2022')

    response = session.get("http://" + HOSTNAME + "/coins/")
    return response.json()


def get_coin_names():
    """
        Returns all Crypto Coins names and counts from API in json format
    """
    session = req.Session()
    session.auth = ('admin', 'temporal2022')

    response = session.get("http://" + HOSTNAME + "/coins/list_names/")
    return response.json()

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
    return round(close_price, 2)


def get_min_max_dates():
    response = create_session_and_call("/min_and_max/")

    min_date = response.json()['min_date']
    max_date = response.json()['max_date']
    fmin = datetime.datetime.strptime(min_date, "%Y-%m-%dT%H:%M:%SZ")
    fmax = datetime.datetime.strptime(max_date, "%Y-%m-%dT%H:%M:%SZ")

    return fmin, fmax


def get_min_max_dates_by_symbol(symbol):
    response = create_session_and_call(f"/coins/dates_by_symbol/{symbol}/")

    min_date = response.json()['min_date']
    max_date = response.json()['max_date']
    fmin = datetime.datetime.strptime(min_date, "%Y-%m-%dT%H:%M:%SZ")
    fmax = datetime.datetime.strptime(max_date, "%Y-%m-%dT%H:%M:%SZ")

    return fmin, fmax


def buy_and_sell_times_to_maximise_profit(ini_date, end_date, coin):
    """
        Finds the best buying and selling dates for maximum profit.

        - itemises by coin
        - filters the prices by dates
        - assumes the sell date is always after a buy date

        - output example:
            - Buy on date: 01/02/2021 and Sell on date: 05/02/2021
            - Buy on date: 12/02/2021 and Sell on date: 19/02/2021
    """
    response = create_session_and_call(
        f"/coins/prices_dates/{coin}/{ini_date}/{end_date}"
    )
    json_response = response.json()
    if not json_response:
        return 0, ["There are not records for the selected coin and dates"]

    prices = []
    dates = []
    for pd in json_response:
        prices.append(pd['close'])
        cdate = datetime.datetime.strptime(pd['date'], "%Y-%m-%dT%H:%M:%SZ").date()
        dates.append(cdate)

    max_profit = get_maximum_profit(prices)
    round_value = 5
    if max_profit > 1:
        round_value = 2

    max_profit = round(max_profit, round_value)
    buy_and_sell = get_buy_and_sell_times(prices, dates)

    results = {
        'prices': prices,
        'dates': dates,
        'max_profit': max_profit,
        'buy_sell': buy_and_sell,
    }
    return results


def get_buy_and_sell_times(prices, dates):
    """
        Receives two lists with prices and dates to find the best possible buy and sell times
        to maximise profit

        :param prices: A list with prices
        :param dates: A list with dates
        :return: a list with buy and sell dates
            - output example:
                - Buy on date: 01/02/2021 and Sell on date: 05/02/2021
                - Buy on date: 12/02/2021 and Sell on date: 19/02/2021
    """
    prices_len = len(prices)
    if prices_len <= 1:
        return []

    dates_result = []
    count = 0
    while count < (prices_len - 1):
        # BUY
        while (count < (prices_len - 1)) and (prices[count + 1] <= prices[count]):
            count += 1
        if count >= prices_len - 1:
            break
        buy = count
        count += 1

        # SELL
        while (count < prices_len) and (prices[count] >= prices[count - 1]):
            count += 1
        sell = count - 1

        msg = "Buy on date: {} and Sell on date: {}\n"
        dates_result.append(msg.format(dates[buy], dates[sell]))

    return dates_result


def get_maximum_profit(prices):
    """
        Receives a list of prices and returns the maximum profit value
    """
    prev_price = float("inf")
    profit = 0
    for p in prices:
        if p > prev_price:
            profit += p - prev_price
        prev_price = p
    return profit

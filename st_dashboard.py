import datetime
import pandas as pd
import streamlit as st

from crypto_tools.utils import (
    get_all_coins_from_api, get_close_price, get_coin_names_and_symbols,
    get_min_max_dates, buy_and_sell_times_to_maximise_profit,
    get_min_max_dates_by_symbol
)

MIN_DATE, MAX_DATE = get_min_max_dates()


def crypto_coins_count():
    """
        Shows the total coins count
    """
    coins_df = pd.DataFrame.from_dict(get_all_coins_from_api())
    metric_columns = st.columns(1)
    metric_columns[0].metric(label="Crypto Coins Total", value=len(coins_df))
    st.markdown("---")


def question_one(coins_df):
    st.subheader("1. What coins are available in our dataset?")

    # Metrics
    metric_columns = st.columns([1, 2])
    metric_columns[0].success(f"Different types of coins: {len(coins_df)}")

    # Plot
    metric_columns = st.columns([1, 2])
    metric_columns[0].dataframe(coins_df)
    metric_columns[1].bar_chart(coins_df, x='name', y='cc_count')

    st.markdown("---")


def question_two(coins_df):
    st.subheader("2. What was the Close price of X "
                 "coin at date yyyy-mm-dd (eg: BTC in 2020-01-02)")

    d = st.date_input(
        "Select a date to know its Close price",
        datetime.date(2020, 10, 7),
        min_value=MIN_DATE,
        max_value=MAX_DATE
    )
    coin = st.selectbox(
        'Which coin would you like to check?',
        coins_df['symbol']
    )

    st.success(str(get_close_price(coin, d)) + " €")
    st.markdown("---")


def question_three(coins_df):
    st.subheader("3. Given a start date and end date, what are the best "
                 "possible buy and sell times to maximise profit?")

    ccoin = st.selectbox(
        'Select a coin to show profits',
        coins_df['symbol']
    )
    min_date = False
    max_date = False
    if ccoin:
        min_date, max_date = get_min_max_dates_by_symbol(ccoin)
    date_ini = st.date_input(
        "Select a start date",
        datetime.date(2020, 11, 6),
        min_value=min_date if min_date else MIN_DATE,
        max_value=max_date if max_date else MAX_DATE
    )
    date_end = st.date_input(
        "Select an end date",
        datetime.date(2020, 12, 15),
        min_value=min_date if min_date else MIN_DATE,
        max_value=max_date if max_date else MAX_DATE
    )
    st.markdown("---")

    results = {}
    if date_end >= date_ini:
        results = buy_and_sell_times_to_maximise_profit(date_ini, date_end, ccoin)

    if results:
        "The maximum profit for this coin and the dates selected is"
        st.success(str(results['max_profit']) + " €")

        "Best buy and sell times"
        dates_columns = st.columns([2, 2])
        buy_sell_len = len(results['buy_sell'])
        col = 0
        for idx, bs in enumerate(results['buy_sell']):
            if not col and buy_sell_len / 2 <= idx:
                col = 1
            if idx % 2:
                dates_columns[col].success(bs)
            else:
                dates_columns[col].warning(bs)

        prices_cd = pd.DataFrame(results['prices'], results['dates'], columns=['prices'])
        st.line_chart(prices_cd)
    else:
        st.error("No results for the inputs selected")


def main():
    # Title
    st.set_page_config(
        page_title="Crypto Terminal Dashboard", layout="wide", page_icon=":euro:")
    st.title("Crypto Terminal Dashboard")

    # Show a total coins count at the top
    crypto_coins_count()

    coins_df = pd.DataFrame.from_dict(get_coin_names_and_symbols())
    # Q1
    question_one(coins_df)
    # Q2
    question_two(coins_df)
    # Q3
    question_three(coins_df)


# %%
if __name__ == "__main__":
    main()

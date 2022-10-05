import datetime
import pandas as pd
import streamlit as st

from crypto_tools.utils import (
    get_all_coins_from_api, get_close_price, get_coin_names_and_symbols,
    get_min_max_dates
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
        coins_df['symbol'])

    st.success(get_close_price(coin, d))
    st.markdown("---")


def question_three():
    st.subheader("3. Given a start date and end date, what are the best "
                 "possible buy and sell times to maximise profit?")

    dini = st.date_input(
        "Select a start date",
        datetime.date(2020, 10, 7),
        min_value=MIN_DATE,
        max_value=MAX_DATE
    )
    dend = st.date_input(
        "Select an end date",
        datetime.date(2021, 1, 3),
        min_value=MIN_DATE,
        max_value=MAX_DATE
    )


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
    question_three()


# %%
if __name__ == "__main__":
    main()

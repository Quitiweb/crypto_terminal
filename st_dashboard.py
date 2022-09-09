import pandas as pd
import requests as req
import streamlit as st

HOSTNAME = '127.0.0.1:8000'


def show_header_metrics(coins_df: pd.DataFrame) -> None:
    metric_columns = st.columns(1)
    metric_columns[0].metric(label="Crypto Coins Total", value=len(coins_df))
    st.write("---")


def question_one(coins_df: pd.DataFrame) -> None:
    st.subheader("1. What coins are available in our dataset?")

    # Metrics
    metric_columns = st.columns([1, 2])
    metric_columns[0].success(f"Different types of coins: {len(coins_df)}")

    # Plot
    metric_columns = st.columns([1, 2])
    metric_columns[0].dataframe(coins_df)
    metric_columns[1].bar_chart(coins_df, x='name', y='cc_count')

    st.markdown("---")


def get_all_coins_from_api():
    session = req.Session()
    session.auth = ('admin', 'temporal2022')

    response = session.get("http://" + HOSTNAME + "/coins/")
    res_json = response.json()
    return pd.DataFrame.from_dict(res_json)


def get_coin_names():
    session = req.Session()
    session.auth = ('admin', 'temporal2022')

    response = session.get("http://" + HOSTNAME + "/coins/list_names/")
    res_json = response.json()
    return pd.DataFrame.from_dict(res_json)


def main():
    # Title
    st.set_page_config(
        page_title="Crypto Terminal Dashboard", layout="wide", page_icon="📀"
    )
    st.title("Crypto Terminal Dashboard")

    # Get all Crypto Coins from API
    coins = get_all_coins_from_api()

    # Header metrics
    show_header_metrics(coins)

    # Get all Crypto Coins from API
    coin_names = get_coin_names()

    # Question one
    question_one(coin_names)


# %%
if __name__ == "__main__":
    main()

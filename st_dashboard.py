import pandas as pd
import requests as req
import streamlit as st

HOSTNAME = '127.0.0.1:8000'


def show_header_metrics(coins_df: pd.DataFrame) -> None:
    metric_columns = st.columns(3)
    metric_columns[0].metric(label="Crypto Coins in DataBase", value=len(coins_df))
    st.write("---")


def get_coins_from_api():
    session = req.Session()
    session.auth = ('admin', 'temporal2022')

    response = session.get("http://" + HOSTNAME + "/coins/")
    res_json = response.json()
    return pd.DataFrame.from_dict(res_json)


def main():
    # Title
    st.set_page_config(
        page_title="Crypto Terminal Dashboard", layout="wide", page_icon="📀"
    )
    st.title("Crypto Terminal Dashboard")

    # Get Crypto Coins from API
    coins = get_coins_from_api()

    # Header metrics
    show_header_metrics(coins)


# %%
if __name__ == "__main__":
    main()

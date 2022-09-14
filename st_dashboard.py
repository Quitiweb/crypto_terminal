import pandas as pd
import streamlit as st

from crypto_tools.utils import get_all_coins_from_api, get_coin_names


def crypto_coins_count():
    """
        Shows the total coins count
    """
    coins_df = pd.DataFrame.from_dict(get_all_coins_from_api())
    metric_columns = st.columns(1)
    metric_columns[0].metric(label="Crypto Coins Total", value=len(coins_df))
    st.write("---")


def question_one():
    st.subheader("1. What coins are available in our dataset?")
    coins_df = pd.DataFrame.from_dict(get_coin_names())

    # Metrics
    metric_columns = st.columns([1, 2])
    metric_columns[0].success(f"Different types of coins: {len(coins_df)}")

    # Plot
    metric_columns = st.columns([1, 2])
    metric_columns[0].dataframe(coins_df)
    metric_columns[1].bar_chart(coins_df, x='name', y='cc_count')

    st.markdown("---")


def main():
    # Title
    st.set_page_config(
        page_title="Crypto Terminal Dashboard", layout="wide", page_icon="📀")
    st.title("Crypto Terminal Dashboard")

    # Show a total coins count at the top
    crypto_coins_count()

    #
    # Question 1
    #
    question_one()


# %%
if __name__ == "__main__":
    main()

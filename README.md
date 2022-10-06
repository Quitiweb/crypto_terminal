# Crypto Terminal

## Data
All necessary data is in `data/archive`.

## Create an interactive tool to answer the following questions
1) What coins are available in our dataset?
2) What was the Close price of X coin at date yyyy-mm-dd (eg: BTC in 2020-01-02)
3) Given a start date and end date, what are the best possible buy and sell times to maximise profit?

You can use any language and GUI (command line interface, streamlit, etc.).

## Bonus
These are not necessary for evaluation, but the candidate can use them to showcase his/her skills.
- Load the data into SQLite
- Create a REST API backend to serve the data to the tool
- Create a dashboard with useful metrics and graphs


## How to install Crypto Terminal locally
1) Get the app from [GitHub repository](https://github.com/Quitiweb/crypto_terminal/) or unzip it from the file sent via email
2) From `crypto_terminal` folder, run `make install` (creates a virtual env)
3) Run `make init_database` (loads the data into SQLite)
4) Run `make start_django_server` (starts the backend server)
5) Final step: run `streamlit run st_dashboard.py` (runs the frontend using `streamlit`)

## Screenshot
![image](https://user-images.githubusercontent.com/8633009/194383664-45df1bea-de68-427c-a5f9-17f1c82708e9.png)

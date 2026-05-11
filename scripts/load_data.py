import pandas as pd


def load_news_data():

    df_news = pd.read_csv(
        "../data/raw/newsData/raw_analyst_ratings.csv"
    )

    return df_news


def load_stock_data():

    stocks = {
        "AAPL": pd.read_csv("../data/raw/yfinance_data/Data/AAPL.csv"),
        "AMZN": pd.read_csv("../data/raw/yfinance_data/Data/AMZN.csv"),
        "GOOG": pd.read_csv("../data/raw/yfinance_data/Data/GOOG.csv"),
        "META": pd.read_csv("../data/raw/yfinance_data/Data/META.csv"),
        "NVDA": pd.read_csv("../data/raw/yfinance_data/Data/NVDA.csv")
    }

    return stocks

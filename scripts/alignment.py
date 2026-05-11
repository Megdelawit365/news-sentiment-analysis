import pandas as pd


def align_news_to_stock_data(
    df_news,
    df_stock
):

    df_news = df_news.copy()
    df_stock = df_stock.copy()

    df_news["date"] = pd.to_datetime(
        df_news["date"],
        format="mixed",
        utc=True
    ).dt.tz_localize(None)

    df_stock["Date"] = pd.to_datetime(
        df_stock["Date"]
    ).dt.tz_localize(None)

    df_news = df_news.sort_values("date")
    df_stock = df_stock.sort_values("Date")

    df_news = pd.merge_asof(
        df_news,
        df_stock[["Date"]],
        left_on="date",
        right_on="Date",
        direction="forward"
    )

    df_news = df_news.rename(
        columns={
            "Date": "aligned_date"
        }
    )

    return df_news

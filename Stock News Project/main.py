import requests
import smtplib
import os
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv(".env")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

MY_EMAIL = os.getenv("MY_EMAIL")
PWD = os.getenv("MY_PWD")
TEST_EMAIL = os.getenv("TEST_EMAIL")

stock_api_parameters = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAIlY",
    "symbol": STOCK,
    "interval": "60min"
}

news_api_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": "2025-09-09",
    "to": "2025-09-10"
}

stocks_response = requests.get(STOCK_ENDPOINT, params=stock_api_parameters)
stock_data = stocks_response.json()
yesterday_closing = float(stock_data["Time Series (Daily)"]["2025-09-10"]["4. close"])
before_yesterday_closing = float(stock_data["Time Series (Daily)"]["2025-09-09"]["4. close"])
price_diff = before_yesterday_closing - yesterday_closing
percentage_diff = round((price_diff/((yesterday_closing + before_yesterday_closing)/2)) * 100)

if abs(percentage_diff) >= 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
    news_data = news_response.json()
    articles = news_data["articles"]
    top_articles = articles[:3]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PWD)
        for article in top_articles:
            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= TEST_EMAIL,
                msg= f"Subject:ALERT\n\n TSLA {percentage_diff}%\n\nHeadline: {article["title"]}\n\nBrief: {article["description"]}"
            )



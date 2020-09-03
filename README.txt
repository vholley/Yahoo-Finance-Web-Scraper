Yahoo-Finance-Web-Scraper


Yahoo Finance no longer has a publicly available API, so I decided to create my own tool to pull a company's financial information.


This uses BeautifulSoup and urllib to scrape a company's income statement, balance sheet, and cash flow statement data from yahoo finance.

get_yahoo_financials.py contains the following functions:

yahoo_income_statement('ticker')
yahoo_balance_sheet('ticker')
yahoo_cash_flow('ticker')

These functions assume valid tickers.

The functions output the tables as pandas dataframes.


Also included is a Jupyter Notebook version. To use, set the ticker variable.

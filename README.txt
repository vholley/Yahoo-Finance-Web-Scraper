Yahoo-Finance-Web-Scraper

This uses BeautifulSoup and urllib to scrape a company's income statement, balance sheet, and cash flow statement data from yahoo finance.

yahoo_income_statement('ticker')
yahoo_balance_sheet('ticker')
yahoo_cash_flow('ticker')

These functions assume valid tickers.

The functions output the tables as pandas dataframes.

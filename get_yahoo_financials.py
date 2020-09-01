# -*- coding: utf-8 -*-

import pandas as pd
import urllib.request as ur
from bs4 import BeautifulSoup


# Begin yahoo_income_statement(ticker)
# =============================================================================


def yahoo_income_statement(ticker='AAPL'):

    # ## Read the yahoo income statement url
    income_url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    read_url = ur.urlopen(income_url).read()

    # BeautifulSoup the xml
    income_soup = BeautifulSoup(read_url, 'lxml')

    # ## Find relevant data structures for financials
    div_list = []

    # Find all HTML data structures that are divs
    for div in income_soup.find_all('div'):
        # Get the contents and titles
        div_list.append(div.string)

        # Prevent duplicate titles
        if not div.string == div.get('title'):
            div_list.append(div.get('title'))

    # ## Filter out irrelevant data
    # Exclude 'Operating Expenses' and 'Non-recurring Events'
    div_list = [incl for incl in div_list if incl not in
                ('Operating Expenses', 'Non-recurring Events', 'Expand All')]

    # Filter out 'empty' elements
    div_list = list(filter(None, div_list))

    # Filter out functions
    div_list = [incl for incl in div_list if not incl.startswith('(function')]

    # Sublist the relevant financial information
    income_list = div_list[13: -5]

    # Insert "Breakdown" to the beginning of the list to give it the proper stucture
    income_list.insert(0, 'Breakdown')

    # ## Create a DataFrame of the financial data
    # Store the financial items as a list of tuples
    income_data = list(zip(*[iter(income_list)]*6))

    # Create a DataFrame
    income_df = pd.DataFrame(income_data)

    # Make the top row the headers
    headers = income_df.iloc[0]
    income_df = income_df[1:]
    income_df.columns = headers

    return income_df

# End yahoo_income_statement(ticker)
# =============================================================================


# Begin yahoo_balance_sheet(ticker):
# =============================================================================


def yahoo_balance_sheet(ticker='AAPL'):

    # ## Read the yahoo balance sheet url
    balancesheet_url = f'https://finance.yahoo.com/quote/{ticker}/balance-sheet?p={ticker}'
    read_url = ur.urlopen(balancesheet_url).read()

    # BeautifulSoup the xml
    balancesheet_soup = BeautifulSoup(read_url, 'lxml')

    # ## Find relevant data structures for balance sheet
    div_list = []

    # Find all HTML data structures that are divs
    for div in balancesheet_soup.find_all('div'):
        # Get the contents and titles
        div_list.append(div.string)

        # Prevent duplicate titles
        if not div.string == div.get('title'):
            div_list.append(div.get('title'))

    # ## Filter out irrelevant data
    # Exclude 'Operating Expenses' and 'Non-recurring Events'
    div_list = [incl for incl in div_list if incl not in
                ('Operating Expenses', 'Non-recurring Events', 'Expand All')]

    # Filter out 'empty' elements
    div_list = list(filter(None, div_list))

    # Filter out functions
    div_list = [incl for incl in div_list if not incl.startswith('(function')]

    # Sublist the relevant financial information
    balancesheet_list = div_list[13: -5]

    # Insert "Breakdown" to the beginning of the list to give it the proper stucture
    balancesheet_list.insert(0, 'Breakdown')

    # ## Create a DataFrame of the financial data
    # Store the financial items as a list of tuples
    balancesheet_data = list(zip(*[iter(balancesheet_list)]*5))

    # Create a DataFrame
    balancesheet_df = pd.DataFrame(balancesheet_data)

    # Make the top row the headers
    headers = balancesheet_df.iloc[0]
    balancesheet_df = balancesheet_df[1:]
    balancesheet_df.columns = headers

    return balancesheet_df

# End yahoo_balance_sheet(ticker):
# =============================================================================


# Begin yahoo_cash_flow(ticker)
# =============================================================================


def yahoo_cash_flow(ticker='AAPL'):

    # ## Read the yahoo cash flow url
    cashflow_url = f'https://finance.yahoo.com/quote/{ticker}/cash-flow?p={ticker}'
    read_url = ur.urlopen(cashflow_url).read()

    # BeautifulSoup the xml
    cashflow_soup = BeautifulSoup(read_url, 'lxml')

    # ## Find relevant data structures for cash flow
    div_list = []
    
    # Find all HTML data structures that are divs
    for div in cashflow_soup.find_all('div'):
        # Get the contents and titles
        div_list.append(div.string)
    
        # Prevent duplicate titles
        if not div.string == div.get('title'):
            div_list.append(div.get('title'))

    # ## Filter out irrelevant data
    # Exclude 'Operating Expenses' and 'Non-recurring Events'
    div_list = [incl for incl in div_list if incl not in
                ('Operating Expenses', 'Non-recurring Events', 'Expand All')]

    # Filter out 'empty' elements
    div_list = list(filter(None, div_list))

    # Filter out functions
    div_list = [incl for incl in div_list if not incl.startswith('(function')]

    # Sublist the relevant financial information
    cashflow_list = div_list[13: -5]

    # Insert "Breakdown" to the beginning of the list to give it the proper stucture
    cashflow_list.insert(0, 'Breakdown')

    # ## Create a DataFrame of the financial data
    # Store the financial items as a list of tuples
    cashflow_data = list(zip(*[iter(cashflow_list)]*6))

    # Create a DataFrame
    cashflow_df = pd.DataFrame(cashflow_data)

    # Make the top row the headers
    headers = cashflow_df.iloc[0]
    cashflow_df = cashflow_df[1:]
    cashflow_df.columns = headers

    return cashflow_df

# End yahoo_cash_flow(ticker)
# =============================================================================

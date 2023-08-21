import random
import pandas as pd
import os
import stat

fileE = r'Z:\Class Repo\Personal Practice\Stevoogle 2\quotes\steve_quotes.xlsx'

quote_list = []
def getQuote():
    df = pd.read_excel(fileE)
    quote_list = df.values.tolist()
    print(quote_list)
    return quote_list

def randomQuote():
    quote_list = getQuote()
    qotd = str(random.choice(quote_list))
    qotd = qotd.strip('[]')
    qotd = qotd.strip('/')
    qotd = qotd.strip('""')
    return qotd
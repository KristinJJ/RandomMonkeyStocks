# imports 
import pandas as pd
import random

num_of_stocks = 30   # number of desired stocks

# read CSV with pandas, extract one column as stock list
stock_csv = pd.read_csv ('./NASDAQ_full.csv')
stock_list= list(stock_csv['Symbol'])

# select 30 random stocks and store in list
chosen_stock_list = random.sample(stock_list, 30)
print (chosen_stock_list)
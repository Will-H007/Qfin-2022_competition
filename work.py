import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(filename):
    with open("prices.txt",'r') as file:
        file = file.read()

    df = pd.DataFrame(file.split())
    df = pd.DataFrame(df.values.reshape(250,-1)).astype(float)
    return df

def buy_list(df, budget, start_date, end_date, concentration = 10):
    percentage_change = df[start_date:end_date].pct_change()
    average_percentage_change = percentage_change.mean()
    average_percentage_change.name = "Buylist"
    # print(average_percentage_change)
    average_percentage_change = average_percentage_change.sort_values(ascending=False)
    if(len(average_percentage_change)>= 10):
        average_percentage_change = average_percentage_change.sort_values(ascending=False)[:concentration]
    else:
        average_percentage_change = average_percentage_change.sort_values(ascending=False)
    stocks_to_buy = np.array(average_percentage_change[average_percentage_change > 0].keys())
    df = average_percentage_change[average_percentage_change > 0].to_frame()
    normalised_buy_list = df["Buylist"] / df["Buylist"].sum()
    # print(normalised_buy_list* budget)
    return normalised_buy_list * budget

def buy_and_sell(current_stock, buylist):
    pass

def main():
    PERIOD = 250 / 30
    BUDGET = 100
    df = read_file("prices.txt")
    # Concentration is always less than 10
    start = 0
    current_stock = []
    for i in range(30,250,30):
        if BUDGET < 100/(PERIOD):
            break
        buylist = buy_list(df= df,budget = 100/(PERIOD), start_date= start , end_date=i , concentration= 3)
        start += 30
        BUDGET -= 100/(PERIOD)
        buy_and_sell(current_stock, buylist)
    print(current_stock)
main()
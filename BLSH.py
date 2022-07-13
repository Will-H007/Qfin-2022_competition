import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nInst=100
currentPos = np.zeros(nInst)

def sell(df):
    df = np.zeros(nInst)
    return df

#Return a list showing the average percentage change over a period from highest to lowest
def buy_list(df, budget, start_date, end_date, concentration = 10):
    percentage_change = df[start_date:end_date].pct_change()
    # print(percentage_change.mean())
    average_percentage_change = percentage_change.mean()
    # plt.plot(average_percentage_change)
    # plt.show()
    average_percentage_change.name = "Buylist"
    # print(average_percentage_change)
    average_percentage_change = average_percentage_change.sort_values(ascending=False)

    # x_axis = average_percentage_change.keys()
    # print(x_axis)
    # plt.bar(average_percentage_change.keys(),average_percentage_change.values)
    # plt.show()
    if(len(average_percentage_change)>= 10):
        average_percentage_change = average_percentage_change.sort_values(ascending=False)[:concentration]
    else:
        average_percentage_change = average_percentage_change.sort_values(ascending=False)
    stocks_to_buy = np.array(average_percentage_change[average_percentage_change > 0].keys())
    df = average_percentage_change[average_percentage_change > 0].to_frame()

    normalised_buy_list = df["Buylist"] / df["Buylist"].sum()
    # print(normalised_buy_list* budget)

    return normalised_buy_list * budget

def getMyPosition (prcSoFar):
    global currentPos
    if len(prcSoFar[0]) % 15 == 0:
        df = pd.DataFrame(prcSoFar).transpose()
        currentPos = sell(df)

        buy = buy_list(df = df, budget = 1000
                 , start_date = len(prcSoFar[0]) - 15, end_date = len(prcSoFar[0]), concentration = 15)
        stocks_to_buy = np.array(buy.keys())
        money_to_spend = np.array(buy.values)
        for i in range(len(stocks_to_buy)):
            currentPos[stocks_to_buy[i]] += money_to_spend[i]

        print(currentPos)
    # Build your function bod
    # y here

    return currentPos

    

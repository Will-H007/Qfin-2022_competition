import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    with open("prices.txt",'r') as file:
        file = file.read()

    df = pd.DataFrame(file.split())
    df = pd.DataFrame(df.values.reshape(250,-1)).astype(float)
    return df

def buy_list(df, start_date, end_date, concentration = 10):
    percentage_change = df[start_date:end_date].pct_change()
    average_percentage_change = percentage_change.mean()
    average_percentage_change.name = "average_percentage_change"
    # print(average_percentage_change)
    average_percentage_change = average_percentage_change.sort_values(ascending=False)
    if(len(average_percentage_change)>= 10):
        average_percentage_change = average_percentage_change.sort_values(ascending=False)[:concentration]
    else:
        average_percentage_change = average_percentage_change.sort_values(ascending=False)
    stocks_to_buy = np.array(average_percentage_change[average_percentage_change > 0].keys())
    df = average_percentage_change[average_percentage_change > 0].to_frame()
    normalised_buy_list = df["average_percentage_change"] / df["average_percentage_change"].sum()
    print(normalised_buy_list* 100)
    return normalised_buy_list



def main():
    df = read_file("prices.txt")
    # Concentration is always less than 10
    buy_list(df, 0, 30,3)

main()
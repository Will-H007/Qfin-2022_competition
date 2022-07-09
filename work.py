import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
with open("prices.txt",'r') as file:
    file = file.read()

df = pd.DataFrame(file.split())
df = pd.DataFrame(df.values.reshape(250,-1)).astype(float)

percentage_change = df[30:60].pct_change()
average_percentage_change = percentage_change.mean()
average_percentage_change.name = "average_percentage_change"
print(average_percentage_change)

fig, ax = plt.subplots(4)
ax[0].plot(df[:][:30][0])
ax[0].set_title('price change 30 days stock "0"')
ax[1].plot(percentage_change[:30][87])
ax[1].set_title('percentage change 30 days stock "87"')
ax[2].bar(np.arange(100),percentage_change[:30].mean())
ax[2].set_title('Average percentage change for each stock in first 30 days')
# ax[3].bar(np.arange(100),percentage_change[30:60].mean())
# ax[3].set_title('Average percentage change for each stock in the second month')
ax[3].bar(np.arange(100),average_percentage_change.sort_values(ascending=False))
ax[3].set_title('Average percentage change from highest to lowest')
fig.tight_layout()
plt.show()

average_percentage_change = average_percentage_change.sort_values(ascending=False)
stocks_to_buy = np.array(average_percentage_change[average_percentage_change > 0].keys())

df = average_percentage_change[average_percentage_change > 0].to_frame()
normalised_buy_list = df["average_percentage_change"] / df["average_percentage_change"].sum()

print(normalised_buy_list)
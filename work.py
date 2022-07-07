import pandas as pd
import numpy as np
with open("prices.txt",'r') as file:
    file = file.read()

df = pd.DataFrame(file.split())
df = pd.DataFrame(df.values.reshape(250,-1)).astype(float)

print(df[0].mean())
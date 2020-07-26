import pandas as pd
import numpy as np
import math as m

import matplotlib as plt
# using following statements to look chart nicer in plot
# import seaborn as sns
# sns.set()


df = pd.read_csv(r'C:\Roy\Python\Equity price.csv')

print(type(df))

sharePrices = pd.DataFrame(df)

MA10 = pd.DataFrame()

nCols = len(df.columns)  # to count number of columns
nRow = len(df.index)

# Calculating 10 day moving average
for s in range(1, nCols):
    MA10['Dates'] = df['Dates']
    MA10.loc[:, s] = df.iloc[:, s].rolling(10).mean()

print(MA10.head(15))

MA60 = pd.DataFrame()

# Calculating 60 day moving average
for s in range(1, nCols):
    MA60['Dates'] = df['Dates']
    MA60.loc[:, s] = df.iloc[:, s].rolling(60).mean()

print(MA60.tail(15))
# print(type(MA60['ABA_shortMV']))
# print(MA60.dtypes)  # check data types


originalReturn = pd.DataFrame()

# Calculating log return of three stocks
for s in range(1, nCols):
    originalReturn['Dates'] = df['Dates']
    originalReturn.loc[:, s] = np.log(df.iloc[:, s] / df.iloc[:, s].shift(1))

print(sharePrices.shape)

originalReturn1 = pd.DataFrame()

# Calculating log return manually using original formulas
for i in range(1, 4):  # it's good to start with columns in for loop if you have a row loop as well
    for s in range(1, nRow):
        if not pd.isnull(sharePrices.iloc[s - 1, i]):
            originalReturn1["Dates"] = sharePrices["Dates"]
            originalReturn1.loc[s, i] = m.log(df.iloc[s, i]/df.iloc[s-1, i])
    else:
        pass

print(originalReturn.head(5))
print(originalReturn1.head(5))

strategyReturn = pd.DataFrame()

# Inputting returns from the original
for x in range(1, 4):
    for y in range(0, len(MA10.index)):
        strategyReturn["Dates"] = sharePrices["Dates"]
        if MA10.iloc[y, x] > MA60.iloc[y, x]:
            strategyReturn.loc[y, x] = originalReturn.iloc[y, x]
        else:
            strategyReturn.loc[y, x] = (.01/250)
print(strategyReturn)

print(strategyReturn.iloc[:, 1:4].describe())
print(originalReturn.iloc[:, 1:4].describe())

# originalReturn.to_csv('/Roy/Python/original_ret.csv')
# strategyReturn.to_csv('/Roy/Python/strategy_ret.csv')


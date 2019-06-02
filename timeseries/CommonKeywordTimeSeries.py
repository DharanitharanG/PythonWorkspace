# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/dharani/Desktop/multiTimeline.csv', skiprows=1)
# print(df.head())

df.columns = ['month', 'diet', 'gym', 'finance']
# print(df.head())

df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)

print(df.head())


df.plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);

# plt.show()

df[['diet']].plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);

# plt.show()

#---------------------------------------
# Identifying the trends:
#
# 1. Rolling Average
# - rolling average, which means that, for each time point,
# you take the average of the points on either side of it. Note that the
# number of points is specified by a window size, which you need to choose.

diet = df[['diet']]
diet.rolling(12).mean().plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);

gym = df[['gym']]
gym.rolling(12).mean().plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);

df_rm = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);

df_rm = pd.concat([diet,diet.rolling(12).mean(), gym,gym.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);

# plt.show()

# Seasonal Patterns in Time Series Data
#   - remove trend from time series
# first-order differencing

diet.diff().plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.title("FOD/seasonality")
plt.show()

df.diff(1).plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.title("FOD/seasonality-all")
plt.show()


































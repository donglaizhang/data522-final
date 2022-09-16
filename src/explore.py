#!/usr/bin/env python

__author__      = "Yahui Wei, Donglai Zhang"
__description__ = "UONA: DATA 522 Solving Big Data Problem - Data Analytics"
__project__ = "Supermarket Store Branches Sales Analysis"
import matplotlib.pyplot as plt
import seaborn as sns
import copy

import pandas as pd

df_master=pd.read_csv("./Stores.csv")
df = copy.copy(df_master)
print(df.head())
sns.pairplot(df,corner=True)
plt.show()

#def read_data() :
#    global df_master
#    df_master=pd.read_csv("./Stores.csv")
#
#read_data()
#def printlines():
#    print()
#    print()
#    print()
#def printhorizon():
#    print("==============================")

#def view() :
#    print(df_master.head())
#    printlines()
#
#view()
#
#def validate():
#    printhorizon()
#    print("Number of null Records")
#    print(df_master.isnull().sum())
#
#validate()
#
#printlines()
#def explore_customer_count_and_item_available():
#    printhorizon()
#    df = copy.copy(df_master)
#    df = df.sort_values(by = "Daily_Customer_Count")
#    sns.catplot(x = "Daily_Customer_Count",y = "Items_Available", data = df, aspect =4)
#    #plt.xticks(rotation =90)
#    plt.show()
sns.pairplot(df_master,corner=True)
plt.show()
explore_customer_count_and_item_available()

#if (1==1) :
#    quit();

df=copy.copy(df_master)

plt.show()

print("df.head done")
print("df.info() start")
df.info()

print("df.info() DONE")
print("df.describe() Start")
res_desc=df.describe()

print("df.describe() :", res_desc)
print("df.columns START ")
res_columns = df.columns
print("result of df.columns  ", res_columns)

df=df.drop('Store ID ', axis=1)
df.head()
sns.pairplot(df,corner=True)
plt.show()
sns.scatterplot(x="Store_Area",y="Items_Available",
                data=df,hue="Items_Available")

plt.show()
plt.figure(figsize=(8,6))

plt.show()
print("scatterplot DONE ")

sns.heatmap(df.corr(),annot=True)

plt.show()


df.corr()['Store_Sales']
plt.show()

df.corr()['Store_Sales'].sort_values()[:-1].plot(kind='bar')
plt.show()


#!/usr/bin/env python

__author__      = "Yahui Wei, Donglai Zhang"
__description__ = "UONA: DATA 522 Solving Big Data Problem - Data Analytics"
__project__ = "Supermarket Store Branches Sales Analysis"
import matplotlib.pyplot as plt
import seaborn as sns
import copy

import pandas as pd
from matplotlib import pyplot as plt

df_master=pd.read_csv("./Stores.csv")
df = copy.copy(df_master)
print(df.head())

def read_data() :
    global df_master
    df_master=pd.read_csv("./Stores.csv")


def printlines():
    print()
    print()
    print()
def printhorizon():
    print("==============================")

def view() :
    print(df_master.head())
    printlines()

def customer_count_and_item():

    plt.figure(figsize=(20, 8), dpi=200)
    ax2 = plt.subplot(221)
    plt.hist(df.Items_Available ,color='#1f77b4',bins=20)
    ax3 = plt.subplot(222)
    plt.hist(df.Daily_Customer_Count, color='#7f7f7f',bins=20)

    ax2.set_title('Items_Available')
    ax3.set_title('Daily_Customer_Count')
    plt.show()
#customer_count_and_item()

def customer_count_and_store_area():
    plt.figure(figsize=(20, 8), dpi=200)
    ax1 = plt.subplot(221)
    plt.hist(df.Store_Area, color='#e35f62',bins=20)
    ax3 = plt.subplot(222)
    plt.hist(df.Daily_Customer_Count, color='#7f7f7f',bins=20)
    ax1.set_title('Store_Area')
    ax3.set_title('Daily_Customer_Count')
    plt.show()

def customer_count_and_store_area_item_sales():
    plt.figure(figsize=(20, 8), dpi=200)

    ax1 = plt.subplot(221)
    plt.hist(df.Store_Area, color='#e35f62',bins=20)
    ax2 = plt.subplot(222)
    plt.hist(df.Items_Available ,color='#1f77b4',bins=20)
    ax3 = plt.subplot(223)
    plt.hist(df.Daily_Customer_Count, color='#7f7f7f',bins=20)
    ax4 = plt.subplot(224)
    plt.hist(df.Store_Sales, color='#17becf',bins=20)

    ax1.set_title('Store_Area')
    ax2.set_title('Items_Available')
    ax3.set_title('Daily_Customer_Count')
    ax4.set_title('Store_Sales')

    plt.show()

def store_area_item():
    sns.scatterplot(x="Store_Area",y="Items_Available",
                data=df,hue="Items_Available")
    plt.show()

def heatmap_correlation():
    sns.heatmap(df.corr(),annot=True)
    plt.show()

def corr_store_sales():
    df.corr()['Store_Sales'].sort_values()[:-1].plot(kind='bar')
    plt.show()

def pairplot():
    sns.pairplot(df, palette='Paired')
    plt.show()

read_data()
customer_count_and_item()
customer_count_and_store_area()
customer_count_and_store_area_item_sales()
store_area_item()
heatmap_correlation()
corr_store_sales()


pairplot()

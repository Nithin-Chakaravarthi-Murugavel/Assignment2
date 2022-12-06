# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:53:53 2022

@author: nithi
"""
import pandas as pd 
import matplotlib.pyplot as plt
def line_plot(filename):
    df=pd.read_csv(filename,skiprows=4)
    print(df)
    dfi1 = df.iloc[20,54:59]
    dfi2 = df.iloc[72,54:59]
    dfi3 = df.iloc[109,54:59]
    dfi4 = df.iloc[138,54:59]
    print(dfi1,dfi2,dfi3,dfi4)
    plt.figure()
    plt.plot(dfi1,label='Bangladesh',dashes=[1,1])
    plt.plot(dfi2,label='Ethiopia',dashes=[1,1])
    plt.plot(dfi3,label='India',dashes=[1,4])
    plt.plot(dfi4,label='Sri Lanka',dashes=[2,5])
    plt.xlabel('Year')
    plt.ylabel('% of population') 
    plt.title('Access to Electricity')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()
def line_plot2(filename):
    df=pd.read_csv(filename,skiprows=4)
    dfi1 = df.iloc[20,54:59]
    dfi2 = df.iloc[72,54:59]
    dfi3 = df.iloc[109,54:59]
    dfi4 = df.iloc[138,54:59]
    print(dfi1,dfi2,dfi3,dfi4)
    plt.figure()
    plt.plot(dfi1,label='Bangladesh',dashes=[1,1])
    plt.plot(dfi2,label='Ethiopia',dashes=[1,1])
    plt.plot(dfi3,label='India',dashes=[1,4])
    plt.plot(dfi4,label='Sri Lanka',dashes=[2,5])
    plt.xlabel('Year')
    plt.ylabel('Metric Tons Per Capita') 
    plt.title('CO2 Emissions')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()
line_plot(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_4695288.csv")
line_plot2(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_EN.ATM.CO2E.PC_DS2_en_csv_v2_4700403.csv")
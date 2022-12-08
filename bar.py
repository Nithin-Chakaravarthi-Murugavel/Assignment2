# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:26:33 2022

@author: nithi
"""
import pandas as pd 
import matplotlib.pyplot as plt
def line_plot(filename):
    read_data=pd.read_csv(filename,skiprows=4)
    print(read_data)
    selected_country1 = read_data.iloc[20,54:59]
    selected_country2 = read_data.iloc[72,54:59]
    selected_country3 = read_data.iloc[109,54:59]
    selected_country4 = read_data.iloc[138,54:59]
    print(selected_country1,selected_country2,selected_country3,
          selected_country4)
    plt.figure(dpi=1080)
    plt.plot(selected_country1,label='Bangladesh',dashes=[1,1])
    plt.plot(selected_country2,label='Ethiopia',dashes=[1,1])
    plt.plot(selected_country3,label='India',dashes=[1,4])
    plt.plot(selected_country4,label='Sri Lanka',dashes=[2,5])
    plt.xlabel('Year')
    plt.ylabel('% of population') 
    plt.title('Access to Electricity')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()
def line_plot2(filename):
    read_data=pd.read_csv(filename,skiprows=4)
    print(read_data)
    selected_country1 = read_data.iloc[20,54:59]
    selected_country2 = read_data.iloc[72,54:59]
    selected_country3 = read_data.iloc[109,54:59]
    selected_country4 = read_data.iloc[138,54:59]
    print(selected_country1,selected_country2,selected_country3,
          selected_country4)
    plt.figure(dpi=1080)
    plt.plot(selected_country1,label='Bangladesh',dashes=[1,1])
    plt.plot(selected_country2,label='Ethiopia',dashes=[1,1])
    plt.plot(selected_country3,label='India',dashes=[1,4])
    plt.plot(selected_country4,label='Sri Lanka',dashes=[2,5])
    plt.xlabel('Year')
    plt.ylabel('Metric Tons Per Capita') 
    plt.title('CO2 Emissions')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()
line_plot(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_4695288.csv")
line_plot2(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_EN.ATM.CO2E.PC_DS2_en_csv_v2_4700403.csv")
def Bar_plot(filename):
    read_data2=pd.read_csv(filename,skiprows=4)
    read_data2=read_data2.drop(["Country Code","Indicator Name","Indicator Code"],axis=1)
    print(read_data2)
    clean_data=read_data2.fillna(0)
    print(clean_data)
    select_country=(clean_data.apply(lambda row: row[clean_data["Country Name"].
                                     isin(['Bangladesh','Ethiopia','India'
                                           ,'Sri Lanka'])]))
    print(select_country)  
    transposing_data = transpose(select_country)
    Plotting(select_country)
    plt.show()
    return select_country,transposing_data 
def Plotting(select_country):
    plt.figure(dpi=1080)
    select_country.plot(x="Country Name",y=["2010","2011","2012","2013","2014"],
              kind="bar")
    plt.xticks(rotation = 0)
    plt.ylabel('Annual Growth %')
    plt.title('GDP')
def transpose(select_country):
    transposed_data=select_country.transpose()
    print(transposed_data)
Bar_plot(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4701072.csv")
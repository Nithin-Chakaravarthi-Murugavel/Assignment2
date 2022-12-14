# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 00:08:02 2022

@author: nithi
"""
# Importing libary into spyder
# Used to read the csv file into spyder and also to compute statistic operation
import pandas as pd 
# To plot the Visualisation
import matplotlib.pyplot as plt
# Defining a function called line plot so that it can run when it is called
def line_plot(filename):
    # Creating a varaiable and stores the csv file data in it
    read_data = pd.read_csv(filename,skiprows=4)
    print(read_data)
    #iloc is used the select the specific rows and columns(Slicing the data)
    selected_country1 = read_data.iloc[20,54:59]
    selected_country2 = read_data.iloc[72,54:59]
    selected_country3 = read_data.iloc[109,54:59]
    selected_country4 = read_data.iloc[138,54:59]
    print(selected_country1,selected_country2,selected_country3,
          selected_country4)
    plt.figure()
    # Used to plot the line plot and dashes are used to change the line plot spacing
    plt.plot(selected_country1,label = 'Bangladesh',dashes = [1,1])
    plt.plot(selected_country2,label = 'Ethiopia',dashes = [1,1])
    plt.plot(selected_country3,label = 'India',dashes = [1,4])
    plt.plot(selected_country4,label = 'Sri Lanka',dashes = [2,5])
    # Used to label the x-axis, y-axis and Title
    plt.xlabel('Year')
    plt.ylabel('% of population') 
    plt.title('Access to Electricity')
    # Add the legend and loc is used to produce the legend in specific side of the graph
    # bbox_to_anchor is used the show the legend outside the box of the plot
    plt.legend(loc='center right',bbox_to_anchor = (1.40, 0.6))
    plt.show()
def line_plot2(filename):
    read_data = pd.read_csv(filename,skiprows=4)
    selected_country1 = read_data.iloc[20,54:59]
    selected_country2 = read_data.iloc[72,54:59]
    selected_country3 = read_data.iloc[109,54:59]
    selected_country4 = read_data.iloc[138,54:59]
    print(selected_country1,selected_country2,selected_country3,
          selected_country4)
    plt.figure()
    plt.plot(selected_country1,label = 'Bangladesh',dashes = [1,1])
    plt.plot(selected_country2,label = 'Ethiopia',dashes = [1,1])
    plt.plot(selected_country3,label = 'India',dashes = [1,4])
    plt.plot(selected_country4,label = 'Sri Lanka',dashes = [2,5])
    plt.xlabel('Year')
    plt.ylabel('Metric Tons Per Capita') 
    plt.title('CO2 Emissions')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()
# Defining a function called Bar plot so that it can run when it is called
def Bar_plot(filename):
    read_data2 = pd.read_csv(filename,skiprows=4)
    # drop() is used to remove the columns from the respective axis mentioned
    read_data2 = read_data2.drop(["Country Code","Indicator Name",
                                "Indicator Code"],axis=1)
    # fillna() is used to remove the NaN (Not a Number) to Zero
    clean_data = read_data2.fillna(0)
    # pandas.DataFrame.apply() is used to select the specific rows of data from the one column
    select_country = (clean_data.apply(lambda row: row[clean_data["Country Name"].
                                     isin(['Bangladesh','Ethiopia','India'
                                           ,'Sri Lanka'])]))
    print(select_country)
    # mean() is used to find the mean value of the specifc year
    finding_mean = select_country["2021"].mean()
    print("Mean Value of all countries in 2021:",finding_mean)
    correlation1 = select_country["2021"]
    correlation2 = select_country["2020"]
    # .corr() is used to find the correlation between two years
    final_correlation = correlation1.corr(correlation2)
    print("The Correlation between 2020 & 2021 for all countries is", 
          final_correlation)
    # Calling a function which is defined already
    transposing_data = transpose(select_country)
    plt.figure()
    # Plotting the dataframe created using pandas plot
    select_country.plot.bar(x="Country Name",
                        y=["2010","2011","2012","2013","2014"])
    # Rotates X-Axis Ticks by 0-degrees
    plt.xticks(rotation = 0)
    plt.ylabel('Annual Growth %')
    plt.title('GDP')
    plt.show()
    # Returns the original and transposed data
    return select_country,transposing_data 
def transpose(select_country):
    # Used to transpose the rows in to column and columns in to rows
    transposed_data = select_country.transpose()
    print("\nTranspose:\n", transposed_data)
# Calling the function with csv file path that are defined above
line_plot(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_4695288.csv")
line_plot2(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_EN.ATM.CO2E.PC_DS2_en_csv_v2_4700403.csv")
Bar_plot(r"D:\Applied Data Science 1\Assignment_2\Data Source\API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4701072.csv")
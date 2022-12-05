# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:12:05 2022

@author: nithi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"D:\Applied Data Science 1\Assignment_2\API_EN.CO2.ETOT.ZS_DS2_en_csv_v2_4538219.csv"
                   ,skiprows=4)
dfi = df.iloc[13,54:59]
dfi2 = df.iloc[109,54:59]
dfi3 = df.iloc[252,54:59]
dfi4 = df.iloc[82,54:59]
print(dfi,dfi2,dfi3,dfi4)

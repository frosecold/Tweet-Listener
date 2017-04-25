#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:08:42 2017

@author: franco
"""
import pandas as pd


filepath='/home/franco/Data Bases/DB7.csv'
df=pd.read_csv(filepath)
df.columns = ['User Name', 'Account', 'Text', 'Time', 'UserID', 'Location']
df['Time'] = df['Time'].str[20:-12]
df['User Name'] = df['User Name'].str[15:-1]
df['Account'] = df['Account'].str[22:-1]
df['Text'] = df['Text'].str[16:-1]
df['UserID'] = df['UserID'].str[12:]
df['Location'] = df['Location'].str[19:-2]



    
print(df)
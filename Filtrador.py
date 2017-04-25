#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:08:42 2017

@author: franco
"""
import pandas as pd


filepath='/home/franco/Data Bases/DB6.csv'

df=pd.read_csv(filepath)
df.columns = ['User Name', 'Account', 'Text', 'Time', 'UserID', 'Location']
df['Time'] = df['Time'].str[20:-12]
df['User Name'] = df['User Name'].str[15:-1]
df['Account'] = df['Account'].str[22:-1]
df['Text'] = df['Text'].str[16:-1]
df['UserID'] = df['UserID'].str[12:]
df['Location'] = df['Location'].str[19:-2]

text_florida = df[df['Text'].str.contains("florida")]
text_fl = df[df['Text'].str.contains(" fl ")]
text_miami = df[df['Text'].str.contains("miami")]
text_mia = df[df['Text'].str.contains(" mia ")]
text_orlando = df[df['Text'].str.contains("orlando")]
location_florida = df[df['Location'].str.contains("florida")]
location_fl = df[df['Location'].str.contains(" fl ")]
location_miami = df[df['Location'].str.contains("miami")]
location_mia = df[df['Location'].str.contains(" mia ")]
location_orlando = df[df['Location'].str.contains("orlando")]

filtrados = [text_florida, text_fl, text_miami, text_mia, text_orlando, location_florida, location_fl, location_miami, location_mia, location_orlando]
final_results = pd.concat(filtrados).drop_duplicates()
final_results
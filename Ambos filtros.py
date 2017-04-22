#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:37:29 2017

@author: franco
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:00:19 2017

@author: franco
"""
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
import pandas as pd

filepath='/home/franco/Data Bases/DB7.csv'
with open(filepath, newline='') as inputfile:
    results = list(csv.reader(inputfile))

#######################################################
#Creo una lista con los textos de los tweets solamente#
#######################################################

tweet_text= list()
location_text = list()
user_list = list()
for elements in results:
    tweet_text.append(results[results.index(elements)][2].replace(" 'tweet_text': ", "").lower().replace("\\n", "#"))
    location_text.append(results[results.index(elements)][5].replace("'", "").replace(" user_location:", "").replace("}","").lower())
    user_list.append(results[results.index(elements)][0].replace("{'user_name': '", "").replace("'",""))
    
original = tweet_text[:]

filtered = list()
filtered_index = list()

#Aplica fuzz.ratio a cada par de elementos en las listas

for original_string in original:
    include = True
    for filtered_string in filtered:
        if fuzz.ratio(original_string, filtered_string) >= 80:
            include = False
            break
    if include:
        filtered.append(original_string)
        filtered_index.append(original.index(original_string))
        


text_filtered= list()
location_filtered= list()
user_filtered= list()

for elements in filtered_index:
    text_filtered.append(tweet_text[elements])
    location_filtered.append(location_text[elements])
    user_filtered.append(user_list[elements])
    
    


print("Se han eliminado "+ str(len(original)-len(filtered_index))+" tweets repetidos")

index_filtered2 = list()
for elements in text_filtered:
    if "florida" in elements:
        index_filtered2.append(text_filtered.index(elements))
        pass
    if "fl " in elements:
        index_filtered2.append(text_filtered.index(elements))
        pass
    if "orlando" in elements:
        index_filtered2.append(text_filtered.index(elements))
        pass
    if "miami" in elements:
        index_filtered2.append(text_filtered.index(elements))
        pass
    if "mia " in elements:
        index_filtered2.append(text_filtered.index(elements))
        pass


for elements in location_filtered:
    if "florida" in elements:
        if location_filtered.index(elements) not in index_filtered2:
            index_filtered2.append(location_filtered.index(elements))
        
    if "fl " in elements:
        if location_filtered.index(elements) not in index_filtered2:
            index_filtered2.append(location_filtered.index(elements))
        
    if "orlando" in elements:
        if location_filtered.index(elements) not in index_filtered2:
            index_filtered2.append(location_filtered.index(elements))
        
    if "miami" in elements:
        if location_filtered.index(elements) not in index_filtered2:
            index_filtered2.append(location_filtered.index(elements))
        
    if "mia " in elements:
        if location_filtered.index(elements) not in index_filtered2:
            index_filtered2.append(location_filtered.index(elements))

user_filtered2= list()
location_filtered2 =list()
text_filtered2 = list()

for elements in index_filtered2:
    user_filtered2.append(user_filtered[elements])
    location_filtered2.append(location_filtered[elements])
    text_filtered2.append(text_filtered[elements])



df = pd.DataFrame(
                    {"User" : user_filtered2,
                   "Tweet" : text_filtered2,
                   "Location" : location_filtered2},
                    index = index_filtered2 )
outputfile=filepath.replace(filepath.split("Bases/")[1],"Filtrado: " + str(round(time.time())))+".xls"
df.to_excel(outputfile)

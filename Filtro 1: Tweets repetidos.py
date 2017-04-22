#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:00:19 2017

@author: franco
"""
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

filepath='/home/franco/RAWDB.csv'
with open(filepath, newline='') as inputfile:
    results = list(csv.reader(inputfile))

#######################################################
#Creo una lista con los textos de los tweets solamente#
#######################################################

tweet_text= list()
for elements in results:
   tweet_text.append(results[results.index(elements)][2].replace(" 'tweet_text': ", "").lower().replace("\\n", "#"))


original = tweet_text[:]

filtered = list()

#Aplica fuzz.ratio a cada par de elementos en las listas

for original_string in original:
    include = True
    for filtered_string in filtered:
        if fuzz.ratio(original_string, filtered_string) >= 80:
            include = False
            break
    if include:
        filtered.append(original_string)

print("Se han eliminado "+ str(len(original)-len(filtered))+" tweets repetidos")

#Crea o abre el archivo
output_filepath = filepath[:-4]+"F1.txt"
saveFile = open(output_filepath, 'a')


#Escribe 1 Linea por cada elemento
text_list=filtered
for elements in text_list:
    saveFile.write(elements+"\n")
saveFile.close()




path= 
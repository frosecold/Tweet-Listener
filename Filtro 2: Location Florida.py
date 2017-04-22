#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:13:28 2017

@author: franco
"""

import csv
import time

#ACA VA EL NOMBRE DEL ARCHIVO A FILTRAR, RECORDAR PONERLO EN LA CARPETA CORRECTA
filepath='/home/franco/RAWDBF1.txt'
with open(filepath, newline='') as inputfile:
    results = list(csv.reader(inputfile))
    
text_list=[]
index_list = []

for elements in results:
    try:
        #Con este se escucha la base de dato en otro formato
        #twit_text = results[results.index(elements)][0].split("::")[1].replace("\\n", "#")
  
        
        #Este es el texto del tweet en miniscula
        twit_text = results[results.index(elements)][2].replace(" 'tweet_text': ", "").lower().replace("\\n", "#")
        
        #Esta es la location
        location_text = results[results.index(elements)][5].replace("'", "").replace(" user_location:", "").replace("}","").lower()

    
        ##################
        #FILTROS DE TEXTO#
        ##################
        
        #Con esto agrego a la lista los tweets que tienen "florida"
        if "florida" in twit_text:
            text_list.append(twit_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #Con esto agrego a la lista los tweets que tienen "fl"
        if "fl " in twit_text:
            text_list.append(twit_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #con este agrego a la lista los tweets que tienen "miami"
        if "miami" in twit_text:
            text_list.append(twit_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #con este agrego a la lista los tweets que tienen "mia"
        if "mia " in twit_text:
            text_list.append(twit_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #Con este agrego a la lista los twits que tienen "orlando"
        if "orlando" in twit_text:
            text_list.append(twit_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #####################
        #FILTROS DE LOCATION#
        #####################
        
        #Con esto agrego a la lista los tweets que tienen "florida" en su location
        if "florida" in location_text:
            text_list.append(location_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #Con esto agrego a la lista los tweets que tienen "fl" en su location
        if "fl " in location_text:
            text_list.append(location_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #con este agrego a la lista los tweets que tienen "miami" en su location
        if "miami" in location_text:
            text_list.append(location_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #con este agrego a la lista los tweets que tienen "mia" en su location
        if "mia " in location_text:
            text_list.append(location_text)
            index_list.append(results.index(elements))
        else:
            pass
        
        #Con este agrego a la lista los twits que tienen "orlando" en su location
        if "orlando" in location_text:
            text_list.append(location_text)
            index_list.append(results.index(elements))
        else:
            pass
        
    except:
        pass


print(str(len(text_list))+ " elements found!")

#Crea o abre el archivo
output_filepath=filepath[:-4]+"F2.txt"
saveFile = open(output_filepath, 'a')

#Escribe 1 Linea por cada elemento
for elements in text_list:
    saveFile.write(str(index_list[text_list.index(elements)]) +' : '+ results[text_list.index(elements)][2].split("'tweet_text': ")[1].replace("'","")+"\n")
    #saveFile.write('\n')
saveFile.close()


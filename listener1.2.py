#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:04:46 2017

@author: franco
"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

#consumer key, consumer secret, access token, access secret.
ckey="je1LQs78Y7cAaSri9ym6yzbo2"
csecret="AjOvkFaLul2QVEHbYZIInGoIAgpdXxVNAKmTsRo85qKMoamPu2"
atoken="120909840-thbApVBzxrfyCZNB2iLBSN2AiZpMTXs6sMgImE6e"
asecret="tuAJGb79CI0tmpjlhwPcbI2FnLFWSjAy6RXaTcWJhgqVG"
rows=50000 #Numero de
iterator=iter(range(rows))
created_at=round(time.time())
destination='/home/franco/Data Bases/'+str(created_at)+'.csv'
class listener(StreamListener):

    def on_data(self, data):

        try:
            global iterator
            d = json.loads(data)
            tweet_text= d['text'].replace(","," ")
            tweet_time= d['created_at']
            user_id= d['user']['id']
            user_name= d['user']['name'].replace(","," ")
            user_screen_name=d['user']['screen_name'].replace(","," ")
            try:
                user_location = d['user']['location'].replace(","," ")
            except:
                user_location = None
           
            LINEA= {"user_name": user_name, 
                    "user_screen_name": user_screen_name, 
                    "tweet_text": tweet_text,
                    "tweet_time": tweet_time,
                    "user_id": user_id,
                    "user_location": user_location}
          
            if "RT " not in tweet_text:  
                print(next(iterator))
                print(LINEA)
                saveFile = open(destination, 'a')
                saveFile.write(str(LINEA))
                saveFile.write('\n')
                saveFile.close()
            else:
                pass

        except BaseException as e:
            pass
            print('ERROR: ', str(e))
            time.sleep(5)
            

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car accident","car crash","injured","injury attorney","choque", "autopista", "accidente","ayuda legal","asesoria legal","lesionado", "lesionados"])

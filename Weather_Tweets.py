
# coding: utf-8

# In[2]:


print("Open File")
import tweepy
import time
import json
import random
import requests as req
import datetime


# In[3]:


import os
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]
weather_api_key = os.environ["weather_api_key"]


# In[4]:


def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Austin"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status("Austin Weather " +        (datetime.datetime.now().strftime("%I:%M %p") + " " +         str(weather_json["main"]["temp"])+"F"))

    # Print success message
    print("Tweeted successfully!")


# In[5]:


counter = 0
# Set timer to run every 1 hour
while counter < 60:
    WeatherTweet()
    time.sleep(3600)


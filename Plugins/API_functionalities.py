import os
import datetime
from dotenv import load_dotenv
from newsapi import NewsApiClient
import re
import requests
from wolframalpha import Client

load_dotenv(dotenv_path='..\\Data\\.env')

NEWS = os.getenv('NEWS_API')
WOLFRAMALPHA = os.getenv('WOLFRAMALPHA_API')
OPENWEATHERMAP = os.getenv('OPENWEATHERMAP_API')
TMDB = os.getenv('TMDB_API')
news = NewsApiClient(api_key=NEWS)

def get_ip(_return=False):
    try:
        response = requests.get(f'http://ip-api.com/json/').json()
        if _return:
            return response
        else:
            return f'Your IP address is {response["query"]}'
    except KeyboardInterrupt:
        return None
    except requests.exceptions.RequestException:
        return None

def get_joke():
    try:
        joke = requests.get('https://v2.jokeapi.dev/joke/Any?format=txt').text
        return joke
    except KeyboardInterrupt:
        return None
    except requests.exceptions.RequestException:
        return None

def get_news():
    try:
        top_news = ""
        top_headlines = news.get_top_headlines(language="en", country="in")
        for i in range(10):
             top_news += re.sub(r'[|-] [A-Za-z0-9 |:.]*', '', top_headlines['articles'][i]['title']).replace("’", "'") + '\n'
        return top_news
    except KeyboardInterrupt:
        return None
    except requests.exceptions.RequestException:
        return None

def get_weather(city=''):
    try:
        if city:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP}&units=metric').json()
        else:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={get_ip(True)["city"]}&appid={OPENWEATHERMAP}&units=metric').json()
        weather = f'It\'s {response["main"]["temp"]}° Celsius and {response["weather"][0]["main"]}\n' \
               f'But feels like {response["main"]["feels_like"]}° Celsius\n' \
               f'Wind is blowing at {round(response["wind"]["speed"] * 3.6, 2)}km
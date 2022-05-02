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
news = NewsApiClient(api_key=NEW
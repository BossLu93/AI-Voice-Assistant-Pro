import webbrowser
import re
import wikipedia
import speedtest
from youtubesearchpython import VideosSearch
import websites


def googleSearch(query):
	if 'image' in query:
		query += "&tbm=isch"
	query = query.replace('images', '')
	query = query.replace('image', '')
	query = query
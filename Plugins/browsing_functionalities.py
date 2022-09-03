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
	query = query.replace('search', '')
	query = query.replace('show', '')
	query = query.replace('google', '')
	query = query.replace('tell me about', '')
	query = query.replace('for', '')
	webbrowser.open("https://www.google.com/search?q=" + query)
	return "Here you go..."

def youtube(query):
	query = query.replace('play', ' ')
	query = query.replace('on youtube', ' ')
	query = query.replace('youtube', ' ')

	print("Searching for videos...")
	videosSearch = VideosSearch(query, limit=1)
	results = videosSearch.result()['result']
	print("Finished searching!")

	webbrowser.open('https://www.youtube.com/watch?v=' + results[0]['id'])
	return "Enjoy..."

def open_specified_website(query):
	website = query[5:] #re.search(r'[a-zA-Z]* (.*)', query)[1]
	if website in websites.websites_dict:
		url = websites.websites_dict[website]
		webbrowser.open(url)
		return True
	else:
		return None

def get_speedtest():
	try:
		
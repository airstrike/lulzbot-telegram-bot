#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser 
import urllib.request, urllib.error, urllib.parse
from urllib.request import Request

def gitfeed(username):
	returnval = ''
	username = username.replace(' ', '')

	url = "https://github.com/"+username+".atom"

	try:
		#check if url returns 404
		a=urllib.request.urlopen(url)
		feed = feedparser.parse(url)["entries"]
		for i in range(1,5):
			returnval +='['+str(i)+' '+feed[i].title+' - '+feed[i].link+' ]\n'

		return returnval

	except urllib.error.HTTPError as e:
		if e.code == 404:
			error = 'Either user does not exist or you gave invalid username'
			return error
        	

# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
import json as m_json

def google(terms): # google <search term>
    query=terms
    query = urllib.parse.urlencode ( { 'q' : query } )
    response = urllib.request.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    returnval=""
    for result in results:
        title = result['title']
        url = result['url']
        title=title.translate({ord(k):None for k in '<b>'})
        title=title.translate({ord(k):None for k in '</b>'})
        returnval += title + ' ; ' + url + '\n'
        
    return returnval.encode('utf-8')

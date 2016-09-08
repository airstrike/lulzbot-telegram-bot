#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulStoneSoup
import urllib.request, urllib.parse, urllib.error

def weather(components): # !weather <city> or !weather <city>, <state or country>
    '''Returns a string containing the weather conditions from a location'''
    #print components
    head, sep, location = components.partition('/weather')
    response = ''
    conditions = ''

    try:
        if len(location) < 1:
            raise Exception('Empty location!')
    except:
        response = 'Usage: /weather <city>, <state>'
    else:
        location = location.replace(' ', '')
        conditions = get_weather(location)
        if type(conditions) == type(str()):
            response = conditions
        else:
            response = conditions['location'] + ' - ' + conditions['temp'] + \
                    ' - ' + conditions['weather'] + ' - Provided by: ' + \
                    'Weather Underground, Inc.'

    return response.encode('utf8')

def get_weather(location):
    degree = '°'.decode('utf8')
    conditions = {}
    base_url = 'http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query='

    try:
        page = urllib.request.urlopen(base_url + location)
    except:
        return 'Could not open the page!'
    else:
        soup = BeautifulStoneSoup(page)
        conditions['location'] = soup.find('full').contents[0]

        if 2 >= len(conditions['location']):
            return 'Inexistent location: ' + location
        else:
            conditions['weather'] = soup.find('weather').contents[0]
            conditions['temp'] = soup.find('temperature_string').contents[0]

            pos = conditions['temp'].find(' ')
            conditions['temp'] = conditions['temp'][:pos] + degree + \
                    conditions['temp'][pos:]

            pos = conditions['temp'].rfind(' ')
            conditions['temp'] = conditions['temp'][:pos] + degree + \
                    conditions['temp'][pos:]

        page.close()

    return conditions

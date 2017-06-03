#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import zlib
from HTMLParser import HTMLParser

my_data_list = []
new_my_data_list = []

class MyHTMLParser(HTMLParser):
    cnt = 1
    def handle_starttag(self, tag, attrs):
        if tag != 'table':
            return
        #print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        if tag != 'table':
            return
        #print "Encountered an end tag :", tag

    def handle_data(self, data):
        self.cnt += 1
        data = data.strip(' \t\n\r')
        if data == '' in data or 'html' in data:
            return
        if self.cnt <= 147:
            return
        if self.cnt >= 356:
            return
        my_data_list.append(data)
        #print "%d Encountered some data  : %s" % (self.cnt, data)
        
        
        

def deflate(data): 
    try:               
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

url = 'http://www.stockq.org/taiwan/exchange_rate_CNY.php'
session = requests.session()

r = session.get(url)
#print r.text

html_str = r.content

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html_str)

i = 0
while i < len(my_data_list):
    my_data_dict = {
        'name': '',
        'buy_sight': '',
        'sell_sight': '',
        'buy_cash': '',
        'sell_cash': '',
        'time': ''
    }
    if i > 5:
        my_data_dict['name'] = my_data_list[i]
        my_data_dict['buy_sight'] = my_data_list[i+1]
        my_data_dict['sell_sight'] = my_data_list[i+2]
        my_data_dict['buy_cash'] = my_data_list[i+3]
        my_data_dict['sell_cash'] = my_data_list[i+4]
        my_data_dict['time'] = my_data_list[i+5]

        print "(%s): %s" % (my_data_list[0], my_data_dict['name'])
        print "(%s): %s" % (my_data_list[1], my_data_dict['buy_sight'])
        print "(%s): %s" % (my_data_list[2], my_data_dict['sell_sight'])
        print "(%s): %s" % (my_data_list[3], my_data_dict['buy_cash'])
        print "(%s): %s" % (my_data_list[4], my_data_dict['sell_cash'])
        print "(%s): %s" % (my_data_list[5], my_data_dict['time'])
        print '--------'
    new_my_data_list.append(my_data_dict)
    i += 6
    if i >= 85:
        break

#!/usr/bin/python3
'''
Created on 8.11.2010

@author: xhresko
'''
import urllib.request, re
import sys


sample_utf = "http://www.root.cz"
sample_cp1250 = "http://www.ihned.cz"
sample_iso8859_2 = "http://www.aktualne.cz"

pat_utf8 = re.compile(b'[\xC2\xC3]')
pat_cp1250 = re.compile(b'[\x8A\x8D\x8E\x9A\x9C-\x9F]')
pat_iso8859_2 = re.compile(b'[\xA6\xA9\xAB\xAE\xB1\xB5-\xB7\xBB]')

def det_encoding(input_data):
    if (re.search(pat_utf8, input_data)):
        return 'utf-8'    
    elif (re.search(pat_cp1250, input_data)):
        return 'cp1250'
    elif (re.search(pat_iso8859_2, input_data)):
        return 'iso8859-2'
    else :
        return "unknown"

for arg in sys.argv: 
    opener = urllib.request.FancyURLopener({})
    f = opener.open(arg)
    text = f.read()
    print(det_encoding(text))



#!/usr/bin/python3
'''
Created on 8.11.2010

@author: xhresko
'''
import urllib.request, re
import sys,logging


sample_utf = "http://www.root.cz"
sample_cp1250 = "http://www.ihned.cz"
sample_iso8859_2 = "http://www.aktualne.cz"

pat_utf8 = re.compile(b'[\xC2\xC3]') #194,195
pat_cp1250 = re.compile(b'[\x8A\x8D\x8E\x9A\x9C-\x9F]') #138,141,142,154,156-159
pat_iso8859_2 = re.compile(b'[\xA6\xA9\xAB\xAE\xB1\xB5-\xB7\xBB]') #166,169,171,174,177,181-183,187

pat_encinfo = re.compile('charset=[^\",\']+')

def det_encoding(input_data):

    string = str(input_data)
    m = re.search(pat_encinfo, string)
    if (m!=None): 
        #logging.info("Meta tag hit...")
        return (m.group(0).replace("charset=","")).strip('\\') 
    elif (re.search(pat_utf8, input_data)):
        return 'utf-8'    
    elif (re.search(pat_cp1250, input_data)):
        return 'cp1250'
    elif (re.search(pat_iso8859_2, input_data)):
        return 'iso8859-2'
    else :
        #logging.info("Using default...")
        return "default"

logging.basicConfig(level=logging.INFO)
sys.stdin = sys.stdin.detach()
data = sys.stdin.read()
enc = det_encoding(data)
if(enc == 'default'):
    print(data)
else:
    #logging.info("Encoding detected - " + enc)
    try: 
        lines = data.decode(enc).splitlines()
        for line in lines:
            print(line.strip())
    except:
        logging.warn("Wrong encoding " + enc)
        print(data)

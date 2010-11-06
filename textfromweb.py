import html2text
import htmllib, formatter, urllib, sys

def wrapwrite(text): sys.stdout.write(text.encode('utf8'))

baseurl = 'http://www.aktualne.cz/'
if baseurl.startswith('http://') or baseurl.startswith('https://'):
    j = urllib.urlopen(baseurl)
    try:
        from feedparser import _getCharacterEncoding as enc
    except ImportError:
        enc = lambda x, y: ('utf-8', 1)
    text = j.read()
    encoding = enc(j.headers, text)[0]
    if encoding == 'us-ascii': encoding = 'utf-8'
    data = text.decode(encoding)

else:
    encoding = 'utf8'    
    

wrapwrite(html2text.html2text(data, baseurl))
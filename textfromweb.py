import html2text, urllib, sys,  chardet

def wrapwrite(text): sys.stdout.write(text.encode('utf8'))

baseurl = 'http://www.aktualne.cz/'
if baseurl.startswith('http://') or baseurl.startswith('https://'):
    j = urllib.urlopen(baseurl)    
    text = j.read()
    encoding = chardet.detect(text)['encoding']
   
    data = text.decode(encoding)

else:
    encoding = 'utf8'    
    

wrapwrite(html2text.html2text(data, baseurl))

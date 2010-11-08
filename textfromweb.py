import urllib, sys, html2text_old, encutils
def wrapwrite(text): sys.stdout.write(text.encode('utf8'))

baseurl = 'http://blisty.cz/2010/11/5/art55351.html'
if baseurl.startswith('http://') or baseurl.startswith('https://'):
    j = urllib.urlopen(baseurl)    
    text = j.read()
    print (str(encutils.det_encoding(text)))
    encoding = encutils.det_encoding(text)
    
    data = text.decode(encoding)

else:
    encoding = 'utf8'
    

wrapwrite(html2text_old.html2text(data, baseurl))

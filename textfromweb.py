from pyparsing_py3 import *
import urllib.request, textutil, sys, encutils

def clean_html(text):

    removeText = replaceWith("")
    scriptOpen,scriptClose = makeHTMLTags("script")
    scriptBody = scriptOpen + SkipTo(scriptClose) + scriptClose
    scriptBody.setParseAction(removeText)
    
    anyTag,anyClose = makeHTMLTags(Word(alphas,alphanums+":_"))
    anyTag.setParseAction(removeText)
    anyClose.setParseAction(removeText)
    htmlComment.setParseAction(removeText)
    
    commonHTMLEntity.setParseAction(replaceHTMLEntity)
    
    # get some HTML
    
    # first pass, strip out tags and translate entities
    firstPass = (htmlComment | scriptBody | commonHTMLEntity | 
                 anyTag | anyClose ).transformString(text)
    
    # first pass leaves many blank lines, collapse these down
    repeatedNewlines = LineEnd() + OneOrMore(LineEnd())
    repeatedNewlines.setParseAction(replaceWith("\n\n"))
    secondPass = repeatedNewlines.transformString(firstPass)
    
    return secondPass

if len(sys.argv) > 1 :
    #for arg in sys.argv: 
    opener = urllib.request.FancyURLopener()
    f = opener.open(sys.argv[1])
    data = f.read()
    encoding = encutils.det_encoding(data)
    text = data.decode(encoding)
    print("Encoding detected - " + encoding)
    #print(clean_html(text))
    
    topwords = list()
    wordlist = textutil.get_wordlist_rate(clean_html(text))
    
    for rwg in wordlist:
        if rwg.rating > 3 and len(rwg.wordgroup[0]) > 4 :
            print(str(rwg))
    
    sort_wg = sorted(wordlist, key = lambda group : group.rating, reverse=True)
    for rwg in sort_wg:
        if rwg.rating > 1 and len(rwg.wordgroup[0]) > 4 :
          #and len(rwg.wordgroup) > 1:
            weight = 1
            weight += rwg.rating/2
            weight += len(rwg.wordgroup[0])/2
            weight += len(rwg.wordgroup)/1
            for word in rwg.wordgroup :
                #topwords.add((word, weight))
                topwords.append((weight,word))
    if(not True):
        for tw in sorted(topwords):
            print("(" + str(tw[0]) + ") - " + tw[1])
            
            
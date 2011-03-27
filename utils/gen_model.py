#!/usr/bin/python3
#Generate model for page, from vertical file.

import sys,re,logging

logging.basicConfig(level=logging.INFO)

garbage = ["<", ">", "//", "=", "|", ";"]

del_tags = ["script"]
high_tags = ["title","h1","h2","h3","h4","script","style"]
count_tags = ["a","img","alltags"]


del_content = False
del_lines = 0

letters = re.compile("[\w]",re.UNICODE)
tag_pattern = re.compile("<[/]*[a-z0-9]+")


def get_tag(line):
    match = re.search(tag_pattern,line)
    if not match == None:        
        tagname = match.group(0)[1:]
        if(line[-2]=="/"): # oneline tag
            #logging.info("oneline - " + tagname)
            return [0,tagname]          
        elif(line[1] == "/"):
            #logging.info("endtag - " + tagname[1:] )
            return [2,tagname[1:]]  
        else:     
            #logging.info("starttag - "+ match.group(0)[1:])
            return [1,match.group(0)[1:]]
    elif(line[0:2] == "<!" or "<?"):
            #logging.info("comment")
            return [0,"comment"]
    else:
        logging.warn("Unexpected line! " + line)
        pass

def ext_text(line):
    if(line.find("&") == -1 ):
        line = line.strip("`~1234567890_=<>@#$%^&!-+.,:;\"\'[](){}|*/\ \t\n")
    else:
        line = ''
    return line

docstate = list()
tagdict = {}
for tag in count_tags:
    tagdict[tag] = 0
try: 
    for line in sys.stdin:
    
        if(len(line.strip()) > 1 and line.strip()[0]  == '<'):
            tagdict["alltags"] += 1
            tag_tuple = get_tag(line.strip())
            #print(tag_tuple)
            if (tag_tuple == None):
                pass
            elif (tag_tuple[0] == 0 ): # one line tag
                if tag_tuple[1] in count_tags:
                    tagdict[tag_tuple[1]] += 1
                pass
            elif((tag_tuple[0] == 1) and (tag_tuple[1] in high_tags)):
                docstate.append(tag_tuple[1])
            elif((tag_tuple[0] == 2) and (tag_tuple[1] in high_tags) and tag_tuple[1] in docstate):
                docstate.remove(tag_tuple[1])
        elif(len(line.strip()) > 1 and ' '.join(docstate).find('script') ==-1 and ' '.join(docstate).find('style') ==-1):
            tag = 'none'
            if(len (docstate) > 0 and len(line)>3):
                tag = docstate[0]
            for word in line.split(): 
                word = ext_text(word)
                if(len(word) > 3):
                    print(word.lower() + '\t' + tag)
            pass
except:
    logging.error("Error while parsing file.")
print(tagdict)    

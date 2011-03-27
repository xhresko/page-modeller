#!/usr/bin/python3
'''
Created on 27.3.2011

@author: xhresko
'''
import re,sys,logging

attFile = open("/home/xhresko/dp/data/attributes.txt", 'r')
csvFile = open("/home/xhresko/dp/data/examples.csv", 'r')
tagDict = {"title":10,"h1":8,"h2":5,"h3":3,"h4":2,"none":1}

def printHeader():
    ''' Prints header of .arff file '''
    print("@RELATION\tpagecategory")
    print('\n')
    
def printAttributes(attList,classList):
    for attribute in attList:
        print("@ATTRIBUTE\t"+attribute+"\tNUMERIC")
    for cls in classList:
        print("@ATTRIBUTE\t"+cls+"\t{True,False}")
        
def readAttributes(filename):
    attrDict = dict()
    infile = open(filename,'r')
    tagstats = dict()
    for line in infile:
        line = line.strip()
        if(line[0]=='{'):
            tagstats = eval(line)
            #print(tagstats)
        else:
            a = line.split('\t')
            try:
                attrDict[a[0]] += tagDict[a[1]]
            except:    
                attrDict[a[0]]  = tagDict[a[1]]
    attrDict.update(tagstats)
    return attrDict
    
def printData(attributes,csvfile,pagepath,classnum):
    print("@DATA")
    #infile = open(csvfile,'r')
    linenum = 0
    namebonus = 1000000
    for line in csvfile:
        row = line.split(";")
        if(linenum>0):
            features = readAttributes(pagepath+str(namebonus+linenum)+'.html.mod')
            record = ''
            for a in attributes:
                try:
                    record += str(features[a]) + ','
                except:
                    record += '0,'
            record += str(row[classnum].strip==1)
            print(record)
        else:
            pass
        
        linenum += 1


def getAttributes(infile):
    result = list()
    for line in infile:
        result.append(line.strip())
    return result
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    attributes = getAttributes(attFile)
    #print(attributes)
    
    #print(tagDict['h1'])
    #attList = readAttributes("/home/xhresko/diplomka/data/pages/1026818.html.mod")
    #print(attributes)
    printHeader()
    printAttributes(attributes,['class'])
    printData(attributes,csvFile,"../data/models/",8) # 2-62 - categories (3-Alco-Tobbaco)
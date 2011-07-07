#we have: a zip file(channel.zip): http://www.pythonchallenge.com/pc/def/channel.zip
#           We need to extract and do the same thing like in the url "nothing" level(4)
#           but instead of reaching to the last nothing and see the result, it tells to collect the coments
#           this prints HOCKEY word (but made with the characters OXYGEN)
#Solution: OXYGEN

import sys
import re
import zipfile

extractPath='/home/slok/python-challenge/data/channel'
zipFile='/home/slok/python-challenge/data/channel.zip'

nothing = '90052'
myRegex = re.compile('\d+$')

zfobj = zipfile.ZipFile(zipFile)
while True:
    try:
        #get info of the file inside the zip and extract 
        infoZipList = zfobj.getinfo(nothing+'.txt')
        aux = zfobj.extract(infoZipList.filename, extractPath)
        #open the file to know the next file to extract
        f = open(aux, 'r')
        body = f.read()
        aux = myRegex.findall(body)
        nothing = aux[0]
        #print the comment of the extracted file
        sys.stdout.write(infoZipList.comment)
        
    except:
        print '\nFinished uncompressing and parsing!'
        break


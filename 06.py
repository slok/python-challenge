
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


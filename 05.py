#we have: peak hell (pronaunced: pickel)
#           We unpicle banner.p (unmarshalling/serialization) and then we print a
#           banner (like unix style: http://en.wikipedia.org/wiki/Banner_%28Unix%29)
#solution: channel

import sys
import pickle
import urllib2
from cStringIO import StringIO

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

#simple way
#pkStr = pickle.load(StringIO(urllib2.urlopen(url).read()))

pkStr = StringIO(urllib2.urlopen(url).read())
unpk = pickle.Unpickler(pkStr)
finalUnpk =  unpk.load()

#print the banner (unix)
for i in finalUnpk:
	sys.stdout.write('\n')
	for j in i:
		for x in range(0,(j[1])):
			sys.stdout.write(j[0])


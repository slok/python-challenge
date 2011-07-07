
#we have: the alphabet is +2 letters, examples: k->m, o->q, e->g
#           the message below is translated and says to use the the alphabet +2 to change 'map' (map.html)
#Solution: 'ocr'

inStr = "map"
outStr = ''
for i in inStr:
	outStr += chr(ord(i)+2)
	

print outStr

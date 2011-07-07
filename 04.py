import urllib2
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#nothing = '12345'
nothing = '8022'
myRegex = re.compile('\d+$')


for i in range(0,400):
  response = urllib2.urlopen(url+nothing)
  body = response.read()
  
  aux = myRegex.findall(body)
  try:
    nothing = aux[0]
    print 'Response: ' + body
    print 'nothing: ' + nothing 
  except:
    print 'Response: ' + body

   
  

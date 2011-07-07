#we have: 'Bert' name from previous levl ('Bert is evil'), and a picture to an XML bad formed
#           when we push the 5 button, so if we call Bert with RPC calls we obtain the solution
#Solution: italy 

import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server = xmlrpclib.ServerProxy(url)
print server.phone('Bert')

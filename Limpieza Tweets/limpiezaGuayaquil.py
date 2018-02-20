__author__ = 'bryangerman'

import couchdb
import sys
import re
import json
import urllib2
URL = 'localhost'
db_name = 'consultapopular'
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')
try:
    print (db_name)
    db = server[db_name]
    print ("success")

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url ='http://localhost:5984/consultapopular/_design/tweetsGuayaquil/_view/tweetsGuayaquil'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())

numero = 0
fa = open("salidaGuayaquil.json", "w")
for x in d['rows']:
	a = x['value'].encode('utf-8')
	#final = re.sub('[^A-Za-z0-9\s\xf3\xe1\xe9\xed\xfa]+','', a)
	#fa.write(final)
	a = a.replace("/","")
	a = a.replace(":","")
	a = a.replace("-","")
	a = a.replace("_","")
	a = a.replace(")","")
	a = a.replace("(","")
	a = a.replace(".","")
	a = a.replace(",","")
	a = a.replace("=","")
	a = a.replace("+","")
	a = a.replace("?","")
	a = a.replace("<","")
	a = a.replace(">","")
	a = a.replace("\n","")
	a = a.replace("!","")
	numero = numero + 1
	b = str(a)
	#print ('{"id":"'+str(numero)+'","text":"'+b+'"},\n')
	#fa.write('{"id":"'+str(numero)+'","text":"'+b+'"},\n')
	fa.write(b+'\n')

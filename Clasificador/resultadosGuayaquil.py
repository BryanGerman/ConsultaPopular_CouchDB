from sklearn.feature_extraction.text import CountVectorizer
with open('resultadoFinalGuayaquil.json','r') as fp:
	si = 0
	no = 0
	otros = 0
	for line in fp:
		texto2 =line+"\n"
		texto2 = texto2.upper()
		if texto2.find("NO") >= 0 and not texto2.find("SI") >= 0:
			no = no+1
		elif texto2.find("SI") >= 0 and not texto2.find("NO") >= 0:
			si = si+1
		elif texto2.find("SI") >= 0 and texto2.find("NO")>=0:
			if str(texto2.count("NO")) > str(texto2.count("SI")):
				no = no +1
			else: 
				si = si+1
		else: 
			otros = otros +1
	print ("SI: "+ str(si+otros))
	print ("NO: "+str(no))
	print ("TOTAL: "+str(si+no+otros))

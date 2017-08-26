import os

def search_and_replace(ss,rs):
	for line in text:
		if ss in line:
			line = line.replace(ss,rs)
			print line
			print text.index(line)



htmlfiles = [x for x in os.listdir(".") if x.endswith(".html")]

#print htmlfiles

for htmlfile in htmlfiles:
	text = []
	with open(htmlfile, "r") as fp:
		for line in fp.readlines():
			text.append(line)
	#print text
	search_and_replace('yellow','#70db70')
	
	
	


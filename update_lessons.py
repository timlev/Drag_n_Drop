import os, bs4
from makelessonjsonfromcsv import *

#gradelevels = ['3rdGrade','4thGrade','5thGrade']
gradelevels = ['Parts_of_Speech']
#check for all new csv files
for grade in gradelevels:
	allcsvs = [x.replace(".csv","") for x in os.listdir(grade) if x.endswith(".csv")]
	allhtmls = [x.replace(".html","") for x in os.listdir(grade) if x.endswith(".html")]
	notdone = [os.path.join(grade, x) + ".csv" for x in allcsvs if x not in allhtmls]
	for filename in notdone:
		write_html(write_json(filename, grab_csv(filename)))
		missing_words = get_sounds(grab_csv(filename))
		base_name = os.path.splitext(filename)[0]
		print(missing_words)
		#create missing words file and folder
		if grade not in os.listdir("missing_words"):
			os.mkdir(os.path.join("missing_words",grade))
		with open(os.path.join("missing_words", grade, os.path.split(base_name)[1] + "_missing_words.txt"),"w") as wb:
			wb.write("\n".join(missing_words))
		"""
		# #Add to Index
		folder, lesson = os.path.split(filename)
		index = bs4.BeautifulSoup(open("index.html"), "html5lib")
		table_cell = index.find(id = folder)
		new_link = index.new_tag('a', href = filename.replace(".csv",".html"))
		new_link.string = lesson.replace(".csv","")
		li_tag = index.new_tag("li")
		table_cell.ul.append(li_tag)
		li_tag.append(new_link)
		
		#Write Index file
		print "Updating index.html..."
		with open("index.html", "wb") as wb:
			wb.write(index.prettify(formatter="html"))
		print "Index File Updated" """

#generate new index.html file with all lessons

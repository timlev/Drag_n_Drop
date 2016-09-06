import os
from makelessonjsonfromcsv import *

gradelevels = ['3rdGrade','4thGrade','5thGrade']

#check for all new csv files
for grade in gradelevels:
	allcsvs = [x.replace(".csv","") for x in os.listdir(grade) if x.endswith(".csv")]
	allhtmls = [x.replace(".html","") for x in os.listdir(grade) if x.endswith(".html")]
	notdone = [os.path.join(grade, x) + ".csv" for x in allcsvs if x not in allhtmls]
	for filename in notdone:
		write_html(write_json(filename, grab_csv(filename)))
		get_sounds(grab_csv(filename))

#generate new index.html file with all lessons
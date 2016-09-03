import os, csv, sys, json
filename = "Unit 1 - in, un, dis, mis.csv"




def grab_csv(csvfilename):
    json_dict = {}
    with open(csvfilename, "rb") as csvfile:
        reader = csv.DictReader(csvfile)
#        headers = reader[0].keys()
#        print headers
        rowcount = 0
        for row in reader:
            for key in row.keys():
                if rowcount == 0 and row[key] != "":
                    json_dict[key] = [row[key]]
                elif row[key] != "":
                    json_dict[key].append(row[key])
            rowcount += 1
        return json_dict
def write_json(csvfilename, json_dict):
    json_filename = csvfilename.replace(".csv",".json")
    with open(json_filename, "w") as fp:
        fp.write("var lesson = ")
        json.dump(json_dict, fp, indent=4)
    
    
    
write_json(filename, grab_csv(filename))





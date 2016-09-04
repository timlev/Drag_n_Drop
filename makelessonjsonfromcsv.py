import os, csv, sys, json
filename = "Unit 1 - in, un, dis, mis.csv"


#os.chdir("/storage/emulated/0/AppProjects/Drag_n_Drop/")

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
    
    
    
#write_json(filename, grab_csv(filename))




def get_sounds(json_dict):
    import download_dict_sound_rough as down
    import download_dict_sound
    cwl = []
    for k in json_dict.keys():
        cwl += json_dict[k]
    print cwl
    nd = [w for w in cwl if w not in [f.replace(".mp3",'') for f in os.listdir("sounds")]]
    print nd
    for w in nd:
        down.dictionary_rough_search(w)
    print down.unable_to_download
get_sounds(grab_csv(filename))
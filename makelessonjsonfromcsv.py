import os, csv, sys, json


#os.chdir("/storage/emulated/0/AppProjects/Drag_n_Drop/")

def grab_csv(csvfilename):
    json_dict = {}
    with open(csvfilename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
#        headers = reader[0].keys()
#        print(headers)
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
        fp.write("var lessonname = '" + csvfilename.replace(".csv","") + "';")
        fp.write("var lesson = ")
        json.dump(json_dict, fp, indent=4)
    return json_filename

def write_html(json_filename):
    html_filename = json_filename.replace(".json", ".html")
    #Open orignial drag_n_drop.html
    html_contents = ""
    with open("drag_n_drop2.html", "r") as fp:
        html_contents += fp.read()
    #Point to json file in same folder
    json_link = json_filename.split("/")[1]
    html_contents = html_contents.replace("examplelesson.json", json_link)
    with open(html_filename, "w") as fp:
        fp.write(html_contents)
"""
def get_sounds(json_dict):
    import download_dict_sound_rough as down
    import download_dict_sound
    import download_wiktionary_word as dw
    cwl = []
    for k in json_dict.keys():
        cwl += json_dict[k]
    # print(cwl
    nd = [w for w in cwl if w not in [f.replace(".mp3",'') for f in os.listdir("sounds")]]
    # print(nd
    for w in nd:
        try:
            down.dictionary_rough_search(w)
        except:
            dw.get_wiki(w)
    print(down.unable_to_download
"""

def download_sound_files(master_word_list):
    print("Downloading sound files ...")
    soundfiles = [f.replace(".mp3","") for f in os.listdir("./sounds/") if f.endswith(".mp3")]

    for word in [word for word in master_word_list if word not in soundfiles]:
        downloaded_word = False
        try:
            oggpath = download_wiktionary_word.get_wiki(word, "./sounds/")
            if oggpath != 2:
                download_wiktionary_word.convert_ogg_to_mp3(oggpath, True)
                downloaded_word = True
        except:
            print("Could't convert from wiki", word)
        if downloaded_word == False:
            try:
                mp3path = download_wiktionary_word.download_gstatic(word, "./sounds/")
            except:
                print("Couldn't download from GStatic")
                
def get_sounds(json_dict):
    import download_wiktionary_word
    print("Downloading sound files ...")
    soundfiles = [f.replace(".mp3","") for f in os.listdir("./sounds/") if f.endswith(".mp3")]
    master_word_list = []
    missing_words = []
    for k in json_dict.keys():
        master_word_list += json_dict[k]
    for word in [word for word in master_word_list if word not in soundfiles]:
        downloaded_word = False
        try:
            oggpath = download_wiktionary_word.get_wiki(word, "./sounds/")
            if oggpath not in [1,2]:
                download_wiktionary_word.convert_ogg_to_mp3(oggpath, True)
                downloaded_word = True
            else:
                missing_words.append(word)
        except:
            print("Could't convert from wiki", word)
    print(missing_words)
    return missing_words


if __name__ == '__main__':
    filename = "Unit 1 - in, un, dis, mis.csv"
    write_json(filename, grab_csv(filename))
    get_sounds(grab_csv(filename))

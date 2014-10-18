# source code to extract from json file and print results

import json

with open("items_kgp_new.json") as json_file:
    json_data = json.load(json_file)
    for dic in json_data:
    	print dic["rank"]+' | '+dic["team_name"]+' | '+dic["institution"]+' | '+dic["score"]+'\n'
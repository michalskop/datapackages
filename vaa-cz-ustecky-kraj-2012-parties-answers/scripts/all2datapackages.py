''' all info to datapackages '''

import csv
import os.path

with open("regions.csv") as fin:
    csvr = csv.reader(fin)
    for row in csvr:
        town = row[0]
        town_name = row[1]
        path = "/home/michal/project/vaa2012-2/www/" + row[0] + "-2012/"
        directory = "vaa-cz-" + row[0] + "-2012-parties-answers"
        
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.makedirs(directory + "/data")
        


        exec(open("voters2datapackage.py").read())
        
        exec(open("votes2datapackage.py").read())
        
        exec(open("questions2datapackage.py").read())
        
        exec(open("create_datapackage_json.py").read())

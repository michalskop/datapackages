''' voters to datapackage '''

import csv
#import slugify
#import random
import json

with open (directory + "/data/voters.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","name","abbreviation"])
    with open(path + "answers.json") as fi:
        answers = json.load(fi)
        for a in answers:
            csvw.writerow([a['id'],a['name'],a['short_name']])
   

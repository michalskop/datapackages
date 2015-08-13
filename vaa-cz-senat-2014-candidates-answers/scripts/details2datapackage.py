''' details to datapackage '''

import csv
#import slugify
#import random
#import json


with open ("2014/data/options.csv", "w") as fout:
    with open("2014/details.json") as fin:
        details = json.load(fin)
    csvw = csv.writer(fout)
    csvw.writerow(["vote_event_id","voter_id","option","explanation"])
    i = 0
    with open("2014/data/options_0.csv") as fi:
        csvr = csv.reader(fi)
        for o in csvr:
            if i > 0:
                try:
                    d = details[o[1]][o[0]]
                except:
                    d = ""
                csvw.writerow([o[0],o[1],o[2],d])
            i =+ 1

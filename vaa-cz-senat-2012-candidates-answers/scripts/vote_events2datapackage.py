''' vote events to datapackage '''

import csv
#import slugify
#import random
import json


with open ("2012/data/vote_events.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","motion:name","motion:text","motion:description","order"])
    with open("2012/questions.json") as fi:
        questions = json.load(fi)
        for q in questions:
            csvw.writerow([q['id'],q['name'],q['question'],q['description'],q['order']])

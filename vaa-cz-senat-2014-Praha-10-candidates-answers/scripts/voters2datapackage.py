''' voters to datapackage '''

import csv
#import slugify
#import random
import json

with open ("2014-1/data/voters.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","name","give_name","family_name","group_id","votes"])
    with open("2014-1/answers.json") as fi:
        answers = json.load(fi)
        for b in answers:
            a = answers[b]
            nameli = a['name'].split(' ')
            csvw.writerow([a['id'],a['name'],nameli[0],nameli[1],a['friendly_name'],'yes'])
    
    with open("2014-1/noreply.json") as fi:
        answers = json.load(fi)
        for a in answers:
            nameli = a['name'].split(' ')
            csvw.writerow([a['id'],a['name'],nameli[0],nameli[1],a['friendly_name'],'no'])

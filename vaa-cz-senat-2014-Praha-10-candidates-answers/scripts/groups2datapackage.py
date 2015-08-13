''' voters to datapackage '''

import csv
#import slugify
#import random
import json

groups = {}

with open ("2014-1/data/groups.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","abbreviation","name"])
    with open("2014-1/answers.json") as fi:
        answers = json.load(fi)
        for b in answers:
            a = answers[b]
            groups[a['friendly_name']] = [a['friendly_name'],a['short_name'],""]
#            csvw.writerow([a['id'],a['name'],nameli[0],nameli[1],a['friendly_name'],a['cc'],'yes'])
    
    with open("2014-1/noreply.json") as fi:
        answers = json.load(fi)
        for a in answers:
            groups[a['friendly_name']] = [a['friendly_name'],a['short_name'],""]
#            csvw.writerow([a['id'],a['name'],nameli[0],nameli[1],a['friendly_name'],a['cc'],'no'])

    for k in groups:
        csvw.writerow(groups[k])

''' votes to datapackage '''

import csv
#import slugify
#import random
import json

def vote2option(v):
    try:
        if int(v) == 1:
            return 'yes'
        if int(v) == -1:
            return 'no'
        if int(v) == 0:
            return 'abstain'
    except:
        nothing = 0
    return 'not voting'

with open(path + "long_answers.json") as fin:
        ds = json.load(fin)

details = {}
for d in ds:
    details[d['id']] = d['vote']
    

with open (directory + "/data/votes.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["vote_event_id","voter_id","option","explanation"])
    with open(path + "answers.json") as fi:
        answers = json.load(fi)
        for a in answers:
            for k in sorted(a['vote']):
                v = a['vote'][k]
                try:
                    d = details[a['id']][k]
                except:
                    d = ""
                csvw.writerow([k,a['id'],vote2option(v),d])

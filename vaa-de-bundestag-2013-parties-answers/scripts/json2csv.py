'''transfer data from volebnikalkulacka.cz's jsons into csvs'''

import csv
import json

with open("questions.json") as fin:
    qs = json.load(fin)
    
with open("vote-events.csv","w") as fout:
    fieldnames = ['id','name','question','order','name:cs','question:cs']
    csvw = csv.DictWriter(fout,fieldnames)
    csvw.writeheader()
    for q in qs:
        q['name:cs'] = q['name']
        q['question:cs'] = q['question']
        q['name'] = ''
        q['question'] = ''
        csvw.writerow(q)

#parties
def o2o(v):
    v = int(v)
    if v == 1:
        return 'yes'
    if v == 0:
        return 'no'
    return 'abstain'

with open("answers.json") as fin:
    ass = json.load(fin)

with open("voters.csv","w") as fout:
    with open("votes.csv","w") as fout2:
        fieldnames = ['id','name',"abbreviation"]
        csvw = csv.DictWriter(fout,fieldnames)
        csvw.writeheader()
        fieldnames2 = ['vote_event_id','voter_id','option']
        csvw2 = csv.DictWriter(fout2,fieldnames2)
        csvw2.writeheader()
        for a in ass:
            out = {}
            out['id'] = a['id']
            out['name'] = a['party_long']
            out['abbreviation'] = a['party']
            csvw.writerow(out)
            for vk in a['vote']:
                dic = {"vote_event_id": vk, "voter_id": a['id'], "option": o2o(a['vote'][vk])}
                csvw2.writerow(dic)
            
        
        

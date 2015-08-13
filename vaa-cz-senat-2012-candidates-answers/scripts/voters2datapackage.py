''' voters to datapackage '''

import csv
#import slugify
#import random
import json

with open ("2012/data/voters.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","name","give_name","family_name","group_id","constituency_id"])
    with open("2012/answers.json") as fi:
        answers = json.load(fi)
        for a in answers:
            csvw.writerow([a['id'],a['name'],a['first_name'],a['last_name'],a['friendly_name'],a['constituency_code']])

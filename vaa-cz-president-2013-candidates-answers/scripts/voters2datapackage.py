''' voters to datapackage '''

import csv
#import slugify
#import random
import json

with open (directory + "/data/voters.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","name","given_name","family_name","votes"])
    with open(path + "answers.json") as fi:
        answers = json.load(fi)
        for a in answers:
            csvw.writerow([a['id'],a['name'],a['first_name'],a['last_name'],'yes'])
    

    csvw.writerow([9,'Jana Bobošíková','Jana','Bobošíková','no'])

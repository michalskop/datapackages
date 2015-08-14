''' questions to datapackage '''

import csv

with open (directory + "/data/vote_events.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","motion:name","motion:text","motion:description","order"])
    
    with open(path + "questions.json") as fi:
        questions = json.load(fi)
        for q in questions:
            try:
                order = q['order']
            except:
                order = ""
            csvw.writerow([q["id"],q["name"],q["question"],q["description"],order])

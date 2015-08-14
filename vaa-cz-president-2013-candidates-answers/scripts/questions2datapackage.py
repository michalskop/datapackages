''' questions to datapackage '''

import csv

with open (directory + "/data/vote_events.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","motion:name","motion:text","motion:description","order", "motion:text_candidates","order_long","order_2"])
    
    with open(path + "backend/source/questions.tsv") as fi:
        csvr = csv.reader(fi,delimiter = "\t")
        i = 0
        for row in csvr:
            if i > 0:
                csvw.writerow([row[0],row[6],row[2],row[3],row[5],row[1],row[4],row[8]])
            i += 1

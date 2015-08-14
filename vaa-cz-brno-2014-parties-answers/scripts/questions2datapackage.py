''' questions to datapackage '''

import csv

with open (directory + "/data/vote_events.csv", "w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["id","motion:name","motion:text","motion:description","order"])
    
    with open(path + "backend/source/questions.tsv") as fi:
        csvr = csv.reader(fi,delimiter = "\t")
        i = 0
        for row in csvr:
            if i > 0:
                csvw.writerow([row[0],row[1],row[2],row[3],row[4]])
            i += 1

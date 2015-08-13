''' answers to datapackage '''

import csv
import slugify
import random

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

voters = [["id","session_id","date","answered"]]
## vote_events = [["id","motion:name"]]  copy from 
votes = [["voter_id","vote_event_id","option","weight"]]
ve2column = {}
w2column = {}
sessionrank = {}        
n = 0

with open("praha-2014.csv") as fi:
    csvr = csv.reader(fi)
    i = 0
    for row in csvr:
        if i == 0:
            j = 0
            for item in row:
                li = item.split('-')
                if (li[0] == "c") and li[1].isdigit() and ((int(li[1]) > 0 and int(li[1]) <= 65) or ((int(li[1]) > 100 and int(li[1]) <= 120))):
                    w2column[li[1]] = j
                if (li[0] == "q") and li[1].isdigit() and ((int(li[1]) > 0 and int(li[1]) <= 65) or ((int(li[1]) > 100 and int(li[1]) <= 120))):
                    ve2column[li[1]] = j
                j = j + 1

        else:
            r = 1 #random.randrange(1,66+1)
            if r == 1:
                try:
                    sr = sessionrank[row[0]]
                except:
                    sessionrank[row[0]] = 0
                sessionrank[row[0]] = sessionrank[row[0]] + 1
                voter = [row[0] + '-' + str(sessionrank[row[0]]), row[0], row[1]]
                
                m = 0
                for k in ve2column:
                    try:
                        if row[w2column[k]] == 'on':
                            w = 2
                        else:
                            w = 1
                    except:
                        w = 1
                    try:
                        option = vote2option(row[ve2column[k]])
                    except:
                        option = "not voting"
                    if option != "not voting":
                        vote = [row[0] + '-' + str(sessionrank[row[0]]), k, option, w]
                        votes.append(vote)
                        m = m + 1
                #print(i)
                n = n + 1
                voter.append(m)
                voters.append(voter)
        i = i + 1
        

with open("users/data/votes.csv","w") as fo:
    csvw = csv.writer(fo)
    for row in votes:
        csvw.writerow(row)

with open("users/data/voters.csv","w") as fo:
    csvw = csv.writer(fo)
    for row in voters:
        csvw.writerow(row)             


# creates datapackage with voting records from visegrad API

# the term must be set manually
# the output (which fields in which file) must be set manually depending on data availability

import vpapi
#import slugify
import csv
import json
import re

last = '5501491a273a3961a6ac81f3'

    #cz/senat:
#        http://www.senat.cz/datum/datum.php?navrat=www.senat.cz%2Fsenat%2Findex.php%3Flng%3Dcz&ke_dni=10.1.20&O=&lng=cz&kontrola=1
vpapi.parliament('sk/nrsr')
terms = [
#    {
#        "id": "1",
#        "since": "1998-09-26T00:00:00",
#        "until": "1996-04-27T00:00:00"
#    },
    {
        "id": "2",
        "since": "1998-09-26T00:00:00",
        "until": "2002-09-21T00:00:00"
    },
    {
        "id": "3",
        "since": "2002-09-21T00:00:00",
        "until": "2006-06-17T00:00:00"
    },
    {
        "id": "4",
        "since": "2006-06-17T00:00:00",
        "until": "2010-06-12T00:00:00"
    },
    {
        "id": "5",
        "since": "2010-06-12T00:00:00",
        "until": "2012-03-10T00:00:00"
    },
    {
        "id": "6",
        "since": "2012-03-10T00:00:00",
        "until": "2016-03-10T00:00:00"
    },
]

def getid(link):
    m = re.search('ID=([0-9]{1,})',link)
    try:
        out = m.group(1)
    except:
        out = ""
    return out


organizations = {}
people = {}
vote_events = {}
motions = {}
votes = []



orgs = vpapi.getall("organizations")
for org in orgs:
    organizations[org['id']] = org
print("organizations downloaded: ",len(organizations))

peop = vpapi.getall("people")
for person in peop:
    people[person['id']] = person
print("people downloaded: ",len(people))

for term in terms:

    sli = term["since"].split('-')
    uli = term["until"].split('-')
    directory = "sk-nrsr-" + term["id"] + "-" + sli[0] + "-" + uli[0] + "-roll-call-votes"

    with open(directory + "/data/vote_events.json") as fi:
        cvote_events = json.load(fi)
#        vote_events = cvote_events.copy()
    with open(directory + "/data/voters.json") as fi:
        cpeople = json.load(fi)
#        people = cpeople.copy()
    with open(directory + "/data/groups.json") as fi:
        corganizations = json.load(fi) 
#        organizations = corganizations.copy()
       
#    if not os.path.exists(directory):
#        os.makedirs(directory)
#        os.makedirs(directory + "/data")

    w = {"$and": [
        {"start_date": {"$gte": term['since']}}, 
        {"start_date": {"$lte": term['until']}},
        {"id": {"$gt": last}}
    ]}

    ves = vpapi.getall("vote-events",where=w,sort="id")
    for ve in ves:
        vote_events[ve['id']] = ve
    print("vote_events downloaded: ",len(vote_events))

    cvotes = []
    cpeople = {}
    corganizations = {}
    cvote_events = {}
    cmotions = {}

#    with open(directory + "/data/votes.csv", "w") as fout:
#        csvw = csv.writer(fout)
#        row = ["vote_event_id","voter_id","option","group_id"]
#        csvw.writerow(row)

    for k in sorted(vote_events):
        print(k + " " + getid(vote_events[k]['sources'][0]['url']))
        with open(directory + "/data/votes.csv", "a") as fout:
            csvw = csv.writer(fout)

            if k > last:
                m_id = vote_events[k]["motion_id"]
                motions[m_id] = vpapi.get("motions",where={"id":m_id})
                cmotions[m_id] = motions[m_id]
                
                vos = vpapi.getall("votes",where={"vote_event_id":k})
                for vote in vos:
#                    votes.append(vote)
                    cvotes.append(vote)
                    try:
                        cpeople[vote["voter_id"]] = people[vote["voter_id"]]
                        corganizations[vote["group_id"]] = organizations[vote["group_id"]]
                        cvote_events[vote["vote_event_id"]] = vote_events[vote["vote_event_id"]]
    #                    m_id = vote_events[vote["vote_event_id"]]["motion_id"]
    #                    cmotions[m_id] = motions[m_id]  
                        
                        vote_event_id = getid(cvote_events[vote["vote_event_id"]]['sources'][0]['url'])
                        voter_id = cpeople[vote["voter_id"]]["identifiers"][0]["identifier"]
                        group_id = corganizations[vote["group_id"]]["identifiers"][0]["identifier"]
                        row = [vote_event_id, voter_id, vote["option"], group_id]
                        csvw.writerow(row)
                    except:
                        print("None " + getid(vote_events[k]['sources'][0]['url']))

        if k > last:
            with open(directory + "/data/vote_events.json", "w") as fout:
                json.dump(cvote_events, fout)
            with open(directory + "/data/voters.json", "w") as fout:
                json.dump(cpeople, fout)
            with open(directory + "/data/groups.json", "w") as fout:
                json.dump(corganizations, fout)
    #        with open(directory + "/data/votes.json", "w") as fout:
    #            json.dump(cvotes, fout)
        
                
        
    with open(directory + "/data/vote_events.csv", "w") as fout:
        csvw = csv.writer(fout)
        row = ["id","start_date","motion:text","identifier"]
        csvw.writerow(row)
        for k in cvote_events:
            ve = cvote_events[k]
            m_id = ve["motion_id"]
            m = cmotions[m_id]["_items"][0]
            try:
                vote_event_id = getid(ve['sources'][0]['url'])
                row = [vote_event_id, ve["start_date"], m["text"], ve["identifier"]]
                csvw.writerow(row)
            except:
                nothing = 0

    with open(directory + "/data/voters.csv", "w") as fout:
        csvw = csv.writer(fout)
        row = ["id","name","given_name","family_name","gender","national_identity", "municipality"]
        csvw.writerow(row)
        for k in cpeople:
            g = cpeople[k]
            voter_id = g["identifiers"][0]["identifier"]
            try:
                municipality = g["contact_details"][0]["value"]
            except:
                municipality = ""
            row = [voter_id, g["name"], g["given_name"], g["family_name"], g["gender"],g["national_identity"],municipality]
            csvw.writerow(row)

    with open(directory + "/data/groups.csv", "w") as fout:
        csvw = csv.writer(fout)
        row = ["id","name"]
        csvw.writerow(row)
        for k in corganizations:
            g = corganizations[k]
            group_id = g["identifiers"][0]["identifier"]
            row = [group_id, g["name"]]
            csvw.writerow(row)

#    with open(directory + "/data/votes.csv", "w") as fout:
#        csvw = csv.writer(fout)
#        row = ["vote_event_id","voter_id","option","group_id"]
#        csvw.writerow(row)
#        for vote in cvotes:
#            row = [vote["vote_event_id"], vote["voter_id"], vote["option"], vote["group_id"]]
#            csvw.writerow(row)




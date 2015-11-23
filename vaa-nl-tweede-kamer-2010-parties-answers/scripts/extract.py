'''extract data from stemwijzer'''
'''result.html - "save as" file of results'''
'''result2.html - "view generated source" of results'''

from lxml import html
import csv

def o2o(o):
    if o == 'Eens':
        return 'yes'
    if o == 'Oneens':
        return 'no'
    return 'abstain'

vote_events = []
voters = []
votes = []
with open("result.html") as fin:
    page = fin.read()
    tree = html.fromstring(page)
    
    questions = tree.xpath('//div[@id="gewichtTab"]/div/div/label')
    for q in questions:
        vote_events.append({
            "name": q.xpath("input")[0].tail.strip(),
            "id": q.xpath("@for")[0][1:],
            "order": int(q.xpath("input/@value")[0]),
            "question": q.xpath("@title")[0]
        })
    parties = tree.xpath('//div[@id="partijenTab"]/div/div/label')
    for p in parties:
        voters.append({
            "name": p.xpath("input")[0].tail.strip(),
            "id": p.xpath("@for")[0][6:],
        })

with open("result2.html") as fin:
    page = fin.read()
    tree = html.fromstring(page)
    
    
    lis = tree.xpath('//ul[@class="partijMatch"]/li')
    for li in lis:
        l = li.xpath('@id')[0].split('-')
        idd = "partijstandpunt-" + l[2] + '-' + l[1]
        votes.append({
            'vote_event_id': l[1],
            'voter_id': l[2],
            'option': o2o(li.xpath('strong')[0].text),
            'explanation': tree.xpath('//div[@id="' + idd + '"]/p')[0].text
        })
    
with open ("vote-events.csv","w") as fout:
    csvd = csv.DictWriter(fout,fieldnames = vote_events[0].keys())
    csvd.writeheader()
    for item in vote_events:
        csvd.writerow(item)    

with open ("voters.csv","w") as fout:
    csvd = csv.DictWriter(fout,fieldnames = voters[0].keys())
    csvd.writeheader()
    for item in voters:
        csvd.writerow(item)

with open ("votes.csv","w") as fout:
    csvd = csv.DictWriter(fout,fieldnames = votes[0].keys())
    csvd.writeheader()
    for item in votes:
        csvd.writerow(item)

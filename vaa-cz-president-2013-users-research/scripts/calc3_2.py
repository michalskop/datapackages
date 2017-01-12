# -*- coding: utf-8 -*-

# calculates the transfers, 2 rounds
# using weights from R

import json

# read into data
i = 0
data = []
with open("responses_weighted_info.csv","r") as fin:
  finreader = csv.reader(fin)
  for row in finreader:
    #print i
    if i == 0:
      keys = row
    else:
      j = 0
      val = {}
      for item in row:
        val[keys[j]] = item
        j = j + 1
      data.append(val)
      
      #print data
      #raise Exception()
    i = i + 1
    

people = {
  "zeman": {"name":"Zeman","color":"#FF0000"},
  "schwarzenberg":{"name":"Schwarzenberg","color":"#880088"},
  "fischer":{"name":"Fischer","color":"#0000FF"},
  "dienstbier":{"name":"Dienstbier","color":"#FFA500"},
  "franz":{"name":"Franz","color":"#000000"},
  "roithova":{"name":"Roithová","color":"#FFFF00"},
  "fischerova":{"name":"Fischerová","color":"#00AA00"},
  "sobotka":{"name":"Sobotka","color":"#000088"},
  "bobosikova":{"name":"Bobošíková","color":"#FFFF44"}
}

# rounds
r1 = {}
r2 = {}
for jsonvar in data:
  for key in people:
    #print key
    if (int(jsonvar[key]) == 1):
      try:
        r1[key]
      except:
        r1[key] = float(jsonvar['weight'])
      else:
        r1[key] = r1[key] + float(jsonvar['weight'])
      
      if (int(jsonvar['zeman']) < int(jsonvar['schwarzenberg'])):
        name = 'zeman'
      else:
        name = 'schwarzenberg'
      
      try:
        r2[key]
      except:
        r2[key] = {}
      try:
        r2[key][name]
      except:
        r2[key][name] = float(jsonvar['weight'])
      else:
        r2[key][name] = r2[key][name] + float(jsonvar['weight']) 


#print r2

out = {}
out["nodes"] = []
out["links"] = []
j = 0
toj1 = {}
toj2 = {'zeman':9, 'schwarzenberg': 10}
for item in r2:
  toj1[item] = j
  j = j + 1
for item in r2:
  for item2 in r2[item]:
    out["links"].append({"source":toj1[item],"target":toj2[item2],"value":r2[item][item2]})
  node = people[item]
  node['j'] = toj1[item]  
  out["nodes"].append(node)
print out['nodes']
# the following did not work as I expected, so I had to correct the output file by hand:
for item2 in toj2:
  node = people[item2]
  node['j'] = toj2[item2]
  print node
  out["nodes"].append(node)
print out['nodes']
with open('sankey2.json', 'w') as outfile:
  json.dump(out, outfile)  

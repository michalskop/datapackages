# -*- coding: utf-8 -*-

import json
import pickle

with open("responses0", 'rb') as f:
  responses = pickle.load(f)

out = {}
out["nodes"] = []
out["links"] = []
prevj = {}

i = 0
j = 0

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

for n in range(1, 9):
  sums = {}
  for jsonvar in responses:
    i = i + 1
    count = 0
    for key in jsonvar:
      try:
        if (jsonvar[key] == 1):
          count = count + 1
      except:
        nothing = 1
    for key in jsonvar:
      try:
        if (jsonvar[key] == 1):
          if key in sums:
            sums[key] = sums[key] + 1/count
          else:
            sums[key] = 1/count
      except:
        #del jsonvar[key]
        nothing = 1
  print(sums)
  print sum(sums.itervalues())
  print len(responses)
  outkey = min(sums, key=sums.get)
  print(outkey)
  for item in sums:
    out["nodes"].append({"color":people[item]["color"],"name":people[item]["name"], "j": j})
    if (item == outkey):
      currentj = j
    if (n > 1):
      tmp = sums[item] - last[item]
      out["links"].append({"source":lastj,"target":j,"value":tmp})
      out["links"].append({"source":prevj[item],"target":j,"value":last[item]})
    prevj[item] = j
    j = j + 1  
     
  lastj = currentj
  
  for jsonvar in responses:
    for key in jsonvar:
      if (jsonvar[key] > jsonvar[outkey]):
        jsonvar[key] = jsonvar[key] - 1
    del jsonvar[outkey]
  last = sums
        #raise Exception("diepy")
        #raise Exception("diepy")
with open('sankey.json', 'w') as outfile:
  json.dump(out, outfile)  

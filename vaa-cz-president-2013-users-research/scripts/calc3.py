# -*- coding: utf-8 -*-

# calculates the transfers
# using weights from R (manually entered)

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

weights = {
  'zeman': {'zeman': 1.6800465}, 
  'fischer': {'zeman': 1.4850209, 'schwarzenberg': 1.6041692},
  'sobotka': {'zeman': 0.8815094, 'schwarzenberg': 0.5447683}, 
  'fischerova': { 'zeman': 0.7513741, 'schwarzenberg': 0.4237004}, 
  'schwarzenberg': {'schwarzenberg': 0.7202682}, 
  'dienstbier': {'zeman': 2.6144173, 'schwarzenberg': 0.7212448}, 
  'roithova': {'zeman': 1.4540868, 'schwarzenberg': 0.5347517}, 
  'bobosikova': {'zeman': 1.1143363, 'schwarzenberg': 1.1098767}, 
  'franz': {'zeman': 0.7372130, 'schwarzenberg': 0.3176280}}

wresponses = []
for jsonvar in responses:
  minkey = min(jsonvar, key=jsonvar.get)
  if jsonvar['zeman'] < jsonvar['schwarzenberg']:
    weight = weights[minkey]['zeman']
  else:
    if jsonvar['zeman'] > jsonvar['schwarzenberg']:
      weight = weights[minkey]['schwarzenberg']
    else:
      weight = 1
  wresponses.append({
    'values': jsonvar,
    'weight': weight
  })
  #print(wresponses)
  #raise Exception("diepy")

for n in range(1, 9):
  sums = {}
  for jsonvar in wresponses:
    i = i + 1
    count = 0
    for key in jsonvar['values']:
      try:
        if (jsonvar['values'][key] == 1):
          count = count + 1
      except:
        nothing = 1
    for key in jsonvar['values']:
      try:
        if (jsonvar['values'][key] == 1):
          if key in sums:
            sums[key] = sums[key] + jsonvar['weight']/count
          else:
            sums[key] = jsonvar['weight']/count
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

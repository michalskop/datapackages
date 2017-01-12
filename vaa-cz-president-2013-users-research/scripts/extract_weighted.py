# -*- coding: utf-8 -*-

# extracts inputs and add weights
# only the correct ones

import json
import pickle
import collections
#fin = open('workfile.html', 'w')

# get weights
j = 0
weights = {}
with open("weights.csv","r") as fw:
  for wrow in fw:
    if (j>0):
      war = wrow.split("\t")
      weights[war[0].strip('"')] = {"zeman":war[1],"schwarzenberg":war[2].rstrip()}
    j = j + 1  
    

responses = []
i = 0

with open("research.txt","r") as fin:
  for row in fin:
    ar = row.split("\t")
    #print(ar)
    jsonvar = json.loads(ar[3])
    newvar = {}
    newvar["order"] = {}
    try:
        if "input-sort-bobosikova" in jsonvar:
          newvar["order"]["bobosikova"] = int(jsonvar["input-sort-bobosikova"])
          if "input-sort-dienstbier" in jsonvar:
            newvar["order"]["dienstbier"] = int(jsonvar["input-sort-dienstbier"])
            if "input-sort-fischer" in jsonvar:
              newvar["order"]["fischer"] = int(jsonvar["input-sort-fischer"])
              if "input-sort-fischerova" in jsonvar:
                newvar["order"]["fischerova"] = int(jsonvar["input-sort-fischerova"])
                if "input-sort-franz" in jsonvar:
                  newvar["order"]["franz"] = int(jsonvar["input-sort-franz"])
                  if "input-sort-roithova" in jsonvar:
                    newvar["order"]["roithova"] = int(jsonvar["input-sort-roithova"])
                    if "input-sort-schwarzenberg" in jsonvar:
                      newvar["order"]["schwarzenberg"] = int(jsonvar["input-sort-schwarzenberg"])
                      if "input-sort-sobotka" in jsonvar:
                        newvar["order"]["sobotka"] = int(jsonvar["input-sort-sobotka"])
                        if "input-sort-zeman" in jsonvar:
                          newvar["order"]["zeman"] = int(jsonvar["input-sort-zeman"])
                          cc = 0
                          for n in range(1, 10):
                            if n in newvar["order"].values():
                              cc = cc + 1
                          if (cc == 9):
                            minikey = min(newvar["order"], key=newvar["order"].get)
                            if (newvar["order"]['zeman'] < newvar["order"]['schwarzenberg']):
                              newvar["weight"] = weights[minikey]['zeman']
                            else:
                              newvar["weight"] = weights[minikey]['schwarzenberg']
                            responses.append(newvar)
                            i = i + 1
    except:
      nothing = 1
      
print (i)      
with open("responsesw", 'wb') as f:
  pickle.dump(responses, f)

writer = csv.writer(open('responses_weighted.csv', 'wb'))
vals = []
vals.append("weight")

k = 0
for jsonvar in responses:
  if (k == 0):
    print sorted(jsonvar["order"])
    for key in sorted(jsonvar["order"]):
      vals.append(key)
    writer.writerow(vals)
  vals = []
  vals.append(jsonvar["weight"])
  for key in sorted(jsonvar["order"]):
    vals.append(jsonvar["order"][key])
  writer.writerow(vals)
  k = k + 1
      #print(responses)
      #raise Exception('diePy')


# -*- coding: utf-8 -*-

# extracts inputs
# only the correct ones

import json
import pickle
#fin = open('workfile.html', 'w')

responses = []
i = 0

with open("research.txt","r") as fin:
  for row in fin:
    ar = row.split("\t")
    #print(ar)
    jsonvar = json.loads(ar[3])
    newvar = {}
    try:
        if "input-sort-bobosikova" in jsonvar:
          newvar["bobosikova"] = int(jsonvar["input-sort-bobosikova"])
          if "input-sort-dienstbier" in jsonvar:
            newvar["dienstbier"] = int(jsonvar["input-sort-dienstbier"])
            if "input-sort-fischer" in jsonvar:
              newvar["fischer"] = int(jsonvar["input-sort-fischer"])
              if "input-sort-fischerova" in jsonvar:
                newvar["fischerova"] = int(jsonvar["input-sort-fischerova"])
                if "input-sort-franz" in jsonvar:
                  newvar["franz"] = int(jsonvar["input-sort-franz"])
                  if "input-sort-roithova" in jsonvar:
                    newvar["roithova"] = int(jsonvar["input-sort-roithova"])
                    if "input-sort-schwarzenberg" in jsonvar:
                      newvar["schwarzenberg"] = int(jsonvar["input-sort-schwarzenberg"])
                      if "input-sort-sobotka" in jsonvar:
                        newvar["sobotka"] = int(jsonvar["input-sort-sobotka"])
                        if "input-sort-zeman" in jsonvar:
                          newvar["zeman"] = int(jsonvar["input-sort-zeman"])
                          cc = 0
                          for n in range(1, 10):
                            if n in newvar.values():
                              cc = cc + 1
                          if (cc == 9):
                            responses.append(newvar)
                            i = i + 1
    except:
      nothing = 1
      
print (i)      
with open("responses0", 'wb') as f:
  pickle.dump(responses, f)
  
  
      #print(responses)
      #raise Exception('diePy')


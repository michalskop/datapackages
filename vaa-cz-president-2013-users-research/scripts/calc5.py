# -*- coding: utf-8 -*-

#
#

import pickle
import json
import operator
import string

firstn = 5

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

with open("responsesw", 'rb') as f:
  responses = pickle.load(f)

j = 0
toj = {}
nodes = []
for n in range(1, firstn + 1):
  for key in people:
    try:
      toj[key]
    except:
      toj[key] = {}
    toj[key][n] = j
    # cannot do:
    # node = people[key]
    # node['j'] = j
    # as it changes the j somehow, so:
    node = {'name':people[key]['name'], 'color':people[key]['color'], 'j': j}   
    nodes.append(node)
    j = j + 1

print toj
#raise Exception()

sums = {}
for row in responses:
  sortedrow = sorted(row['order'].iteritems(), key=operator.itemgetter(1))
  #print sortedrow
  #raise Exception()
  for item in sortedrow:
    #print item
    if (item[1] == 1):
      lastitem = item
    else:
      #print item[1]
      if (item[1] <= firstn):
        #print item
        #raise Exception()    
        s = toj[lastitem[0]][lastitem[1]]
        t = toj[item[0]][item[1]]
    
        try:
          sums[s]
        except:
          sums[s] = {}
        try:
          sums[s][t]
        except:
          sums[s][t] = float(row['weight'])
        else:
          sums[s][t] = sums[s][t] + float(row['weight'])
      
        lastitem = item
links = []
for skey in sums:
  for tkey in sums[skey]:
    try:
      sums[skey][tkey]
    except:
      nothing = 1
    else:  
      links.append({'source':skey,'target':tkey,'value':int(sums[skey][tkey])})
    
print links
    
out = {
  'nodes' : nodes,
  'links' : links
}
fname = ['sankey3_',firstn,'.json']
with open(''.join([str(x) for x in fname]), 'w') as outfile:
  json.dump(out, outfile)

print sums

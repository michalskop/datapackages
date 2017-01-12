# -*- coding: utf-8 -*-

#
#

import pickle
import csv
import json

with open("responsesw", 'rb') as f:
  responses = pickle.load(f)

names = {
  'zeman': "Zeman",
  'schwarzenberg': "Schwarzenberg",
  'fischer': "Fischer",
  'dienstbier': 'Dientsbier',
  'roithova': 'Roithová',
  'sobotka': 'Sobotka',
  'fischerova': 'Fischerová',
  'franz': 'Franz',
  'bobosikova': 'Bobošíková'
}
  
out = {}
total = 0
for item in responses:
  total = total + float(item['weight'])
  for keyo in item['order']:
    val = item['order'][keyo]
    if ((val <= 4) or (val >= 8)):
      try:
        out[keyo]
      except:
        out[keyo] = {}
      try:
        out[keyo][val]
      except:
        out[keyo][val] = float(item['weight'])
      else:
        out[keyo][val] = out[keyo][val] + float(item['weight'])

for item in responses:
  if (item['info']['input-negative_vote'] != ''):
      try:
        out[item['info']['input-negative_vote']]['X']
      except:
        out[item['info']['input-negative_vote']]['X'] = float(item['weight'])
      else:
        out[item['info']['input-negative_vote']]['X'] = out[item['info']['input-negative_vote']]['X'] + float(item['weight'])
print out

writer = csv.writer(open('d42.csv', 'wb'))
for name in sorted(out):
  vals = []
  vals.append(name)
  for key in sorted(out[name]):
    vals.append(out[name][key])
  #print vals
  writer.writerow(vals)

# for chart:

with open('d11chart.json', 'w') as outfile:      

  cout = []
  for name in sorted(out):
    item = {
      'nname': names[name],
      'name': name,
      'positive':{'p1': out[name][1]/total},
      'negative':{'n1': out[name][9]/total},
      'total':{'t1': (out[name][1]-out[name][9])/total}
    }
    cout.append(item)
  json.dump(cout, outfile)

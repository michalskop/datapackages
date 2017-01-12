# -*- coding: utf-8 -*-

# calculates 18 groups

import pickle
import csv

with open("responses0", 'rb') as f:
  responses = pickle.load(f)

out = {}
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
        if jsonvar['zeman'] < jsonvar['schwarzenberg']:
          if key in sums:
            if 'zeman' in sums[key]:
              sums[key]['zeman'] = sums[key]['zeman'] + 1/count
            else:
              sums[key]['zeman'] = 1/count
          else:
            #print(jsonvar)
            sums[key] = {}
            sums[key]['zeman'] = 1/count
        else:
          if (jsonvar['schwarzenberg'] < jsonvar['zeman']):
            if key in sums:
              if 'schwarzenberg' in sums[key]:
                sums[key]['schwarzenberg'] = sums[key]['schwarzenberg'] + 1/count
              else:
                sums[key]['schwarzenberg'] = 1/count
            else:
              sums[key] = {}
              sums[key]['schwarzenberg'] = 1/count
    except:
      #del jsonvar[key]
      nothing = 1
print(sums)
writer = csv.writer(open('groups18.csv', 'wb'))
for key, value in sums.items():
  if 'zeman' not in value:
    value['zeman'] = 0
  if 'schwarzenberg' not in value:
    value['schwarzenberg'] = 0
  writer.writerow([key, value['zeman'], value['schwarzenberg']])
  print [key, value['zeman'], value['schwarzenberg']]

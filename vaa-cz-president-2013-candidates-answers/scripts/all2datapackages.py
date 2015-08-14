''' all info to datapackages '''

import csv
import os.path


town0 = "volba-prezidenta-cr"
town = "president"
town_name = 'President'


path = "/home/michal/project/vaa2012-2/www/" + town0 + "-2013/"
directory = "vaa-cz-" + town + "-2013-candidates-answers"

if not os.path.exists(directory):
    os.makedirs(directory)
    os.makedirs(directory + "/data")



exec(open("voters2datapackage.py").read())

exec(open("votes2datapackage.py").read())

exec(open("questions2datapackage.py").read())

exec(open("create_datapackage_json.py").read())

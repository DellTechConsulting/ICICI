import json
import csv
import os


with open('data.json') as d:
    jsondata = json.load(d)
    json_dic = json.dumps(jsondata)

with open('policy_data.json') as d:
    policy = json.load(d)
    
def f(d,newKey,newValue):
    for k,v in d.items():
        if k == newKey:
	        if newValue:
		        d[k] = newValue
        elif type(v) is list:
            for item in v:
                if type(item) is dict:
                    if k == newKey:
                        d[k] = newValue
                    elif type(item) is dict:
                        for item1 in item:
                            if item1 == newKey:
	                            if newValue:
		                            item[item1] = newValue
                            else:
                                filter1 = item['actionSpecificData']
                                filter2 = filter1['backup']
                                if type(filter2) is dict:
                                    for item2 in filter2:
                                        if item2 == newKey:
                                            if newValue:
                                                filter2[item2] = newValue
                                        else:
                                            filter3 = filter2['backupSpecificData']
                                            filter4 = filter3['traditional']
                                            for item3 in filter4:
                                                if item3 == newKey:
                                                    if newValue:
                                                        filter4[item3] = newValue

for item in policy:
    f(jsondata,item,policy[item])

print(json.dumps(jsondata))

filePath = 'updated.json'

if os.path.exists(filePath):
    os.remove(filePath)

with open("updated.json", "w") as outfile:
    outfile.write(json.dumps(jsondata))
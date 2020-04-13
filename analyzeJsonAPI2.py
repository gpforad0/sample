# in this part we will use that json file of packages n sort it here by its maximum installation in last 30days

import json

def get_package_sorted(package):
    return package['analytics']['30d']

with open('package_info.json','r') as f:
    data = json.load(f)                       # convert(load)  json file as python object

#print(data)
data.sort(key=get_package_sorted,)
data_str = json.dumps(data, indent=2)
print(data_str)    ## you will see sorted packages in ascending order  ,for descending REVERSE=True
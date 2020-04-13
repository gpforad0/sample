# analyze JSON API and sort its results and data
# we have large json data which contains lots of details about packages here we gonna parse that json data n then
      # we will separate json data belongs to particular packages
import requests
import json
import time
r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()      ## gives json data for all packages not particular
t1 = time.perf_counter()

#packages_str = json.dumps(packages_json[0], indent=2)
#print(packages_str)

"""following code is single package json data,    this is not legal way to make comment, same logic for all but in for loop 

package1_name = packages_json[0]['name']      # separating json data of one package from bunch of json data
package1_desc = packages_json[0]['desc']
package1_url = f'https://formulae.brew.sh/api/formula/{package1_name}.json'        # json data for particular package

response = requests.get(package1_url)
package1_json = response.json()
#print(package1_json)
package1_json_str = json.dumps(package1_json, indent=2)
#print(package1_json_str)
install_30d = package1_json['analytics']['install_on_request']['30d'][package1_name]
install_90d = package1_json['analytics']['install_on_request']['90d'][package1_name]
install_365d = package1_json['analytics']['install_on_request']['365d'][package1_name]

print(package1_name,package1_desc, install_30d, install_90d, install_365d)
"""
results = []
totalpackageNO=0
for package in packages_json:
    package_name = package['name']
    package_desc = package['desc']
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

    response = requests.get(package_url)
    package_json = response.json()
    #print(package1_json)
    # response.elapsed.total_seconds()   will count total seconds to get response
    install_30d = package_json['analytics']['install_on_request']['30d'][package_name]
    install_90d = package_json['analytics']['install_on_request']['90d'][package_name]
    install_365d = package_json['analytics']['install_on_request']['365d'][package_name]

    data={
        'name':package_name,
        'Desc':package_desc,
        'analytics':{
            '30d': install_30d,
            '90d': install_90d,
            '365d': install_365d
        }
    }

    results.append(data)
    #time.sleep(1)
    #print(package_name, package_desc, install_30d, install_90d, install_365d)
    totalpackageNO += 1
    if totalpackageNO == 100:
        break

t2 = time.perf_counter()
print(f'finished in {t2-t1}')
with open('package_info.json','w') as file:
    json.dump(results,file, indent=2)




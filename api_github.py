import requests
import json
import tabulate
BASE_URL='https://api.github.com/'
SEARCH_URL='search/repositories'
QUERY_URL='?q='
### Variables de busqueda
updated='+pushed:>01-01-2019'
####
print("*** Indica la busqueda deseada ***")
s=input()
req = requests.get(BASE_URL+SEARCH_URL+QUERY_URL+s)
repo_dict = req.json()['items']
result = []
for i in repo_dict:
    if i['license'] == None:
        item ={
            "name":i['name'],
            "url":i['html_url'],
            "owner": i['owner']['login'],
        }
        result.append(item.copy())
header = result[0].keys()
rows =  [x.values() for x in result]
print("*** RESULTADOS ***")
print(tabulate.tabulate(rows, header))

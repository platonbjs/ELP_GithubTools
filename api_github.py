import requests
import json
import tabulate
import math
BASE_URL='https://api.github.com/'
SEARCH_URL='search/repositories'
QUERY_URL='?q='
PAGE='&page='
PER_PAGE='&per_page=100'
UPDATED='+pushed:>2019-01-01'
TOTAL_ITEMS=1000
PAGES = math.ceil(TOTAL_ITEMS/100)
#### Programa
print("*** Indica la busqueda deseada ***")
s=input()
count = 0
result = []
for page in range(1,PAGES+1):
    query=BASE_URL+SEARCH_URL+QUERY_URL+s+UPDATED+PER_PAGE+PAGE+str(page)
    req = requests.get(query)
    repo_dict = req.json()['items']
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

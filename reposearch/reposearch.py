import requests
import json
import tabulate
import math
#import git
BASE_URL='https://api.github.com/'
SEARCH_URL='search/repositories'
UPDATED = '2019-11-01'
QUERY_URL = '?q='
PER_PAGE=100
NUM_ITEMS=100
STARS=100
NUM_PAGES_STR = '&page='
def search_repos(keyword,updated=UPDATED,per_page=PER_PAGE,num_items=NUM_ITEMS, stars=STARS):
    query_url=QUERY_URL+keyword
    per_page_str='&per_page='+str(per_page)
    updated_str='+pushed:>'+updated
    stars_str='+stars:>'+str(stars)
    num_pages=math.ceil(num_items/per_page)
    #### Programa
    count = 0
    result = []
    for page in range(1,num_pages+1):
        num_pages_str=NUM_PAGES_STR+str(page)
        query=BASE_URL+SEARCH_URL+query_url+updated_str+stars_str+per_page_str+num_pages_str
        print(query)
        req = requests.get(query)
        repo_dict = req.json()['items']
        for i in repo_dict:
            if i['license'] == None:
                item ={
                    "name":i['name'],
                    "url":i['html_url'],
                    "owner": i['owner']['login'],
                    "stars": i['stargazers_count'],
                }
                result.append(item.copy())
    header = result[0].keys()
    rows =  [x.values() for x in result]
    print("*** RESULTADOS ***")
    print(tabulate.tabulate(rows, header))
    return result
def main():
    keyword = input("Please enter your keyword to search: ")
    search_repos(keyword)
main()

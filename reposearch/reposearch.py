import requests
import json
import tabulate
import math
#import git
TOKEN='token'
USERNAME='user'
BASE_URL='https://api.github.com/'
SEARCH_URL='search/repositories'
FORK_URL='repos/'
def search_repos(keyword,updated='2019-11-01',total_items=1000):

    SEARCH_URL='search/repositories'
    QUERY_URL='?q='+keyword
    PAGE='&page='
    PER_PAGE='&per_page=100'
    UPDATED='+pushed:>'+updated
    TOTAL_ITEMS=total_items
    PAGES = math.ceil(TOTAL_ITEMS/100)
    #### Programa
    count = 0
    result = []
    for page in range(1,PAGES+1):
        query=BASE_URL+SEARCH_URL+QUERY_URL+UPDATED+PER_PAGE+PAGE+str(page)
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
    return result

def create_fork(owner,repo_name):
    query=BASE_URL+FORK_URL+owner+'/'+repo_name+'/'+'forks'
    req = requests.post(query,auth=(USERNAME, TOKEN))
#def add_license(repo_name):
#    git.Git
#    pass
def pull_request(repo):
    pass
def main():
    search_repos('opensource')
    #create_fork('','-')
main()

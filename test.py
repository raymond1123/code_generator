import time
import os
from datetime import datetime
from github import Github

# get github token: https://github.com/settings/tokens
ACCESS_TOKEN='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'
g = Github(ACCESS_TOKEN)
#print(g.get_user())

'''
query = 'language:python'

result = g.search_repositories(query)
print(result.totalCount)
'''

day_sec = 24*60*60
end_time = time.time()
start_time = end_time - day_sec

for _ in range(3):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')

    query = f'flask language:python created:{start_time_str}..{end_time_str}'
    #print(query)

    end_time -= day_sec
    start_time -= day_sec

    result = g.search_repositories(query)
    print(result.totalCount)

    for repo in result:
        print(f'{repo._clone_url}')
        print(f'{repo.clone_url}')
        print(repo.owner.login)

        os.system(f'git clone {repo.clone_url} repos/{repo.owner.login}/{repo.name}')



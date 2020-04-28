import requests

# Make an API call and store the respons

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
# print(f"Total respositories:{response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']

# # Print the length of repo_dicts to see how many repos we have
# print(f"Respositories returned:{len(repo_dicts)}")

# # Examine the first repo
repo_dict = repo_dicts[0]
# print(f"Name:{repo_dict['name']}")

# # Examine all repos
for repo_dict in repo_dicts:
	print(f"Name:{repo_dict['name']}")

# # Print the numbers of keys to see how much info we have
# print(f"\nKeys: {len(repo_dict)}")
# # Print all the dictionary's keys 
# for key in sorted(repo_dict.keys()):
# 	print(key)

# Process results
# print(response_dict.keys())

# Status code 200 means successful
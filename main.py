from src import Outlook

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/outlook-account-generator/'''

with open('proxies.txt', 'r') as f:
	proxies = f.read().splitlines()

proxies = [f'http://{proxy}' for proxy in proxies]
count = int(input('How many accounts do you want to create? '))

Outlook.create_accounts(count=count, proxies=proxies)
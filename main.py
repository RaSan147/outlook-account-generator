from src import Outlook

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/outlook-account-generator/'''

with open('proxies.txt', 'r') as f:
	proxies = f.read().splitlines()

count = int(input('How many accounts do you want to create? '))

Outlook.create_accounts(count=count, proxies=proxies)
import requests, random
from colorama import *
g = Fore.GREEN
r = Fore.RED
print(g + requests.get('http://artii.herokuapp.com/make?text=omar.com').text)
rt = requests.session()
litters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
u = '_'
id = input('id:')
token = input('token:')
hea = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'accept-encoding':'gzip, deflate, br',
 'accept-language':'en-US,en;q=0.9,ar;q=0.8',
 'cache-control':'max-age=0',
 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
 'sec-ch-ua-mobile':'?0',
 'sec-fetch-dest':'document',
 'sec-fetch-mode':'navigate',
 'sec-fetch-site':'same-origin',
 'sec-fetch-user':'?1',
 'upgrade-insecure-requests':'1',
 'user-agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
while True:
    user = str(''.join((random.choice(litters) for x in range(1))))
    user1 = str(''.join((random.choice(litters) for x in range(2))))
    usernames = user + u + user1
    tiko = f"https://www.tiktok.com/@{usernames}?"
    reqsnd = rt.get(tiko, headers=hea).status_code
    if reqsnd == 404:
        print(g + f"{usernames} ✔صح")
        bot = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Hunted: {usernames}\nحساب محذوف صادلك : {usernames} By:@ww8wwww-@ayqjl"
        rt.get(bot)
    else:
        print(r + f"{usernames} ❌خطأ  ")
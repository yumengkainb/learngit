import requests

##r=requests.get('https://github.com/yumengkainb/learngit')

##headers = { 'Cookie':str(r.cookies)
##}

##request=requests.get('https://github.com/',headers=headers)
s=requests.Session();
s.get('https://github.com/yumengkainb/learngit')

request=s.get('https://github.com/')

for key,value in request.headers.items():
    print(key+'='+value)

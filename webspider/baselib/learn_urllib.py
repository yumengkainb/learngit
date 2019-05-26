import requests
import urllib

url='https://fanyi.baidu.com/'
headers={'User_Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
         'Host' : 'httpbin/org'
}
dict={'name' : 'yumengkai'
}

try:
	req=urllib.request.Request(url=url)
	response=urllib.request.urlopen(req,timeout=10)
	print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
	print(e.reason,e.code,e.headers,sep='\n')

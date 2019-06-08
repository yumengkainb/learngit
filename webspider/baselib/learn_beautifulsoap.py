import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

def get_one_page(url):
    headers = {'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    request = requests.get(url=url,headers=headers)
    if request.status_code == 200:
       return request.text
    return none

def main(offset):
    url =  'https://maoyan.com/board/4?offset='+str(offset)
    content=get_one_page(url)
    soup=BeautifulSoup(content,'lxml')
    ##print(soup.find_all(name='a'))
    for item in soup.find_all(name='a')[17:37:2]:
        print(item.string)

def write_to_file(content):
    with open ('./test.html','w',encoding='utf-8') as f:
         f.write(content)


if __name__=='__main__':
   for i in range(10):
       main(offset=i*10)

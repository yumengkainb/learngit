import requests
import json
from lxml import etree

def get_one_page(url):
    headers = {'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    request = requests.get(url=url,headers=headers)
    if request.status_code == 200:
       return request.text
    return none

def main():
    url =  'https://maoyan.com/board/4'
    content=get_one_page(url)
    write_to_file(content)
    html=etree.parse('./test.html',etree.HTMLParser())
    result=html.xpath('//a[@href="/films/1203"]/@title')
    print(result)


def write_to_file(content):
    with open ('./test.html','w',encoding='utf-8') as f:
         f.write(content)


if __name__=='__main__':
   main()

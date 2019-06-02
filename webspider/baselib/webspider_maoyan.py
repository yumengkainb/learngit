import requests
import lxml

def get_one_page(url):
    headers = {'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    request = requests.get(url=url,headers=headers)
    print(request)
    if request.status_code == 200:
       return request.text
    return none

def main():
    url =  'https://maoyan.com/board/4'
    get_one_page(url)
    html=etree.HTML(get_one_page(url),etree.HTMLParser())
    result=html.xpath('//div')
    print(result)
    print(result[0])
    ##for item in get_one_page(url):
        ##write_to_file(item) 
        

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
         f.write(json.dumps(content,ensure_ascii=False)+'\n')


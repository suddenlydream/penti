'''
Created on 2013-7-8

@author: huqiming
'''

from urllib.request import urlopen
import ts_content
import re

__host_url__ = 'http://www.dapenti.com/blog/'

'''
每一期的图说
'''
class ts_summary:
    '''
            地址
    '''
    link = ''
    '''
            标题
    '''
    title = ''
    '''
            内容
    '''
    content = ''
    
    def __init__(self, title, link):
        self.title = title
        self.link = __host_url__ + link
    
    def __str__(self):
        return 'title: ' + self.title + ' link: ' + self.link

def parse(url):
    page = urlopen(url)
    html = page.read()
    result = perform_parse(html)
#     print(html)
    return result

def perform_parse(html):
    print(html)
    html = html.decode('GBK')
   
    p = re.compile(r'<li><a href=.*?</a></li>')
    
    list = p.findall(html)
    print(len(list))
    
    results = []
    for item in list:
        it = parse_item(item)
        results.append(it)
    return results

def parse_item(item):
    p = re.compile(r"((<li><a href=)|</a></li>)")
    tmp = p.sub('', item)
    list = re.split('>', tmp)
    result = ts_summary(list[1], list[0])
    content = ts_content.parse(result.link)
    print(content)
    return result

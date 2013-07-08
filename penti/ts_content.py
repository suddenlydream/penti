'''
Created on 2013-7-8

@author: huqiming
'''

from urllib.request import urlopen
class ts_content:
    parts = []
    
def parse(url):
    print(url)
    page = urlopen(url)
    html = page.read()
    result = perform_parse(html)
    return result

def perform_parse(html):
    print(html)
    html = html.decode('GBK')
    return ''
'''
Created on 2013-7-8

@author: huqiming
'''

from urllib.request import urlopen
import re
'''
图说内容
'''
class ts_content:
    '''
        图说的段落
    '''
    parts = []

'''
图说段落
'''
class ts_content_part:
    '''
        图说段落标题
    '''
    title = ''
    '''
        段落的子项
    '''
    items = []

class ts_content_part_item:
    txtInfo = ''
    ref_url = '' 
    
def parse(url):
    print(url)
    page = urlopen(url)
    html = page.read()
    result = perform_parse(html)
    return result

def perform_parse(html):
    print(html)
    html = html.decode('GBK')
#     p = re.compile(r'<P>【\d】.*?</P>')
#     list = p.findall(html)
#     list = re.findall(r'<P>【\d】.*?</P>', html)
    li = re.finditer(r'<P>【\d*】.*?</P>', html)
    i = 0

    index = []
    for m in li:
        pos = m.start()
        index.append(pos)
        
        if(i > 0):
            part = html[index[i-1]:pos]
            parse_part(part)
#         print(m.start())
#         print(m.group())
        i += 1
    return ''

def parse_part(html):
    
    print()

parse('http://www.dapenti.com/blog/more.asp?name=xilei&id=79405')
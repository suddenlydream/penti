# coding: utf-8
'''
Created on 2013-7-8
@author: huqiming
'''

import urllib2
import ts_content
import re

__host_url__ = 'http://www.dapenti.com/blog/'

'''
图说的简要信息
'''
class ts_summary:
    '''
    链接地址
    '''
    link = ''
    '''
    标题
    '''
    title = ''
    '''
    日期
    '''
    date = ''
    
    def __init__(self, title, link, date):
        self.title = title
        self.link = link
        self.date = date
    
    def __str__(self):
        return 'title: ' + self.title + ' link: ' + self.link

def parse_summary(url):
    page = urllib2.urlopen(url)
    html = page.read()
    source = html.decode('GBK')
    result = perform_parse_summary(source)
    return result

def perform_parse_summary(html):
    p = re.compile(r'<li><a href=.*?</a></li>')
    
    infos = p.findall(html)
    
    results = []
    for item in infos:
        it = parse_summary_item(item)
        results.append(it)
    return results

def parse_summary_item(item):
    p = re.compile(r"((<li><a href=)|</a></li>)")
    tmp = p.sub('', item)
    infos = re.split('>', tmp)
    t_info = parse_title(infos[1])
    result = ts_summary(t_info[0], __host_url__ + infos[0], t_info[1])
#     result.content = ts_content.parse(result.link)
#     print(content)
    return result

def parse_title(title):
    m = re.search(ur'\u3010.*?\u3011', title)
    print m
    if m:
        t = title[m.end() : len(title)]
        d = m.group()
        mm = re.search(r'\d+', d)
        date = mm.group()
        return [t, date]

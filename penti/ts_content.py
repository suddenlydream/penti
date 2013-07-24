# coding: utf-8
'''
Created on 2013-7-8
@author: huqiming
'''
import json
import re
import urllib2
'''
图说内容
'''
class ts_content:
    '''
    图说标题
    '''
    title = ''
    '''
    图说日期
    '''
    date = ''
    '''
    图说段落
    '''
    parts = []
    def __str__(self):
        return 'parts: ' + str(self.parts)

'''
图说段落
'''
class ts_content_part(json.JSONEncoder):
    '''
    段落标题
    '''
    title = ''
    '''
    段落的子内容
    '''
    items = []
    def __str__(self):
        return 'title: ' + self.title + ' items: ' + str(self.items)

class ts_content_part_item(json.JSONEncoder):
    txt_info = ''
    img_url = ''
    
    def __init__(self, txt, img):
        if txt :
            self.txt_info = txt
        if img :            
            self.img_url = img
        
    def __str__(self):
        return 'info: ' + self.txt_info + ' img: ' + self.img_url
    
def parse_content(url):
#     print(url)
    page = urllib2.urlopen(url)
    html = page.read()
    source = html.decode('GBK')
    
    parts = perform_parse_content(source)
    result = ts_content()
    
    result.parts = parts;
    return result

def perform_parse_content(source):
    li = re.finditer(ur'<P>\u3010\d*\u3011.*?</P>', source)
    i = 0

    index = []
    res = []
    for m in li:
        title = m.group()
        part = ts_content_part()
        part.title = remove_tags(title)
        res.append(part)
        
        pos = m.start()
        index.append(pos)
        
        if(i > 0):
            part_source = source[index[i - 1]:pos]
            res_item = parse_content_part(part_source)
            res[i - 1].items = res_item
        i += 1
        
    part_source = source[pos:source.index('<P>&nbsp;</P>')]
    res_item = parse_content_part(part_source)
    res[i - 1].items = res_item
    
    return res

def parse_content_part(source):
    li = re.finditer(r'<(P|DIV)>.*?</(P|DIV)>', source)
    res = []
    for m in li:
        item = m.group()
        img = parse_img_src(item)
        txt = remove_tags(item)
        res_item = ts_content_part_item(txt, img)
#         print(res_item)
        res.append(res_item)
        
    return res

def parse_img_src(source):
    m = re.search(r'<IMG.*?>', source)
    if m:
        img_tag = m.group()
        img_m = re.search(r'src=".*?"', img_tag)
        if img_m:
            src = img_m.group()
            src = src[5:-1]
            return src

def remove_tags(source):
    p = re.compile(r"(<.*?>|</.*?>|<|/>|&nbsp;)")
    return p.sub('', source)

# res = parse('http://www.dapenti.com/blog/more.asp?name=xilei&id=79405')
# from ts_json import json_encode
# ss = json_encode().encode(res)
# print(ss)

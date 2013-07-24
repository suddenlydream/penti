# coding: utf-8
'''
Created on 2013-7-11
@author: huqiming
'''

from ts_content import ts_content, ts_content_part, ts_content_part_item
from ts_summary import ts_summary

def json_decode(o):
        if isinstance(o, ts_summary):
            dic = {}
            dic['title'] = o.title
            dic['link'] = o.link
            dic['date'] = o.date
            return dic
        elif isinstance(o, ts_content):
            dic = {}
            dic['title'] = o.title
            dic['parts'] = o.parts
            dic['date'] = o.date
            return dic
        elif isinstance(o, ts_content_part):
            dic = {}
            dic['title'] = o.title
            dic['items'] = o.items
            return dic
        elif isinstance(o, ts_content_part_item):
            dic = {}
            dic['text'] = o.txt_info
            dic['image'] = o.img_url
            return dic
    

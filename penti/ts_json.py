'''
Created on 2013-7-11

@author: huqiming
'''

from ts_content import ts_content, ts_content_part, ts_content_part_item
from ts_summary import ts_summary
# import json
    
# class json_encode(json.JSONEncoder):
# 
#     def default(self, o):
#         if isinstance(o, ts_summary):
#             dic = {}
#             dic['title'] = o.title
#             dic['link'] = o.link
#             dic['content'] = o.content
#             return dic
#         elif isinstance(o, ts_content):
#             dic = {}
#             dic['parts'] = o.parts
#             return dic
#         elif isinstance(o, ts_content_part):
#             dic = {}
#             dic['title'] = o.title
#             dic['items'] = o.items
#             return dic
#         elif isinstance(o, ts_content_part_item):
#             dic = {}
#             dic['text'] = o.txt_info
#             dic['image'] = o.img_url
#             return dic
#         else:
#             return json.JSONEncoder.default(self, o)

def json_decode(o):
        if isinstance(o, ts_summary):
            dic = {}
            dic['title'] = o.title
            dic['link'] = o.link
            return dic
        elif isinstance(o, ts_content):
            dic = {}
            dic['title'] = o.title
            dic['parts'] = o.parts
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
    

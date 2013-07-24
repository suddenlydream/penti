# coding: utf-8
'''
Created on 2013-7-19
@author: huqiming
''' 
import ts_db
import json
import re
import ts_kvdb
from ts_json import json_decode
from ts_content import parse_content
from ts_summary import parse_summary 

def start_fetch(url):
    res = parse_summary(url)
#     item = res[0]
#     info = parse_title(item.title)
    res_json = json.dumps(res, default=json_decode, indent=2)
    ts_kvdb.save_summary(res_json)
    
    for item in res:
#         data = ts_db.query_content(item.date)
        data = ts_kvdb.get_tushuo(item.date)
        if data is None:
            content = parse_content(item.link)
            content.title = item.title
            content.date = item.date
            res_str = json.dumps(content, default=json_decode)
            ts_db.add_tushuo(content.title, res_str, content.date)
            data = res_str
        ts_kvdb.save_tushuo(item.date, data)
#     ts_db.create_table()

# start_fetch();
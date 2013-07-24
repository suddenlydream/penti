# coding: utf-8
'''
Created on 2013-7-8
@author: huqiming
'''

import json
import ts_db
import ts_kvdb
from ts_json import json_decode
from ts_content import parse_content
from ts_fetcher import start_fetch
from ts_summary import parse_summary, ts_summary

__penti_url__ = 'http://www.dapenti.com/blog/blog.asp?subjectid=70&name=xilei'
# __penti_url__ = 'http://www.dapenti.com/blog/blog.asp?name=xilei&subjectid=70&page=3'

def get_summary():
    return ts_kvdb.get_summary();

def get_content(date):
    data = ts_kvdb.get_tushuo(date)
    if data is None:
#         return ts_db.query_content(date)
        return 'kvdb is null'
    else:
        return data

def fetch():
    start_fetch(__penti_url__)
    return 'begain fetch info'
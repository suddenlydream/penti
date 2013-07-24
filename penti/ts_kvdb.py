# coding: utf-8
'''
Created on 2013-7-20

@author: dreaner
'''

import sae.kvdb

def save_tushuo(date, content):
    kv = sae.kvdb.KVClient()
    kv.set(date.encode('utf-8'), content)
    
def delete_tushuo(date):
    kv = sae.kvdb.KVClient()
    kv.delete(date.encode('utf-8'))
    
def get_tushuo(date):
    kv = sae.kvdb.KVClient()
    return kv.get(date.encode('utf-8'))
    
def save_summary(summary):
    kv = sae.kvdb.KVClient()
    kv.set('summary', summary)
    
def get_summary():
    kv = sae.kvdb.KVClient()
    return kv.get('summary')

# coding: utf-8
'''
Created on 2013-7-12
@author: huqiming
'''
import sae.const
import MySQLdb

# DB      = 'penti'       # 数据库名
# USER    = 'guest'       # 用户名
# PWD     = '123456'      # 密码
# HOST    = '127.0.0.1'   # 主库域名（可读写）
# PORT    = '3306'        # 端口，类型为，请根据框架要求自行转换为int

DB      =  sae.const.MYSQL_DB      # 数据库名
USER    =  sae.const.MYSQL_USER    # 用户名
PWD     =  sae.const.MYSQL_PASS    # 密码
HOST    =  sae.const.MYSQL_HOST    # 主库域名（可读写）
PORT    =  sae.const.MYSQL_PORT    # 端口，类型为，请根据框架要求自行转换为int

SQL_CREATE_TABLE = 'create table IF NOT EXISTS tushuo(id int PRIMARY KEY AUTO_INCREMENT , title varchar(100), info TEXT)'
SQL_INSERT = 'insert into tushuo(title, info, date) values(%s, %s, %s)'
SQL_DROP_TABLE = 'drop table tushuo'
SQL_QUERY_SUMMARY = 'select date, title from tushuo order by date desc'
SQL_QUERY_CONTENT = 'select info from tushuo where date = %s'

def connect_db():
    conn = MySQLdb.connect(host=HOST, user=USER , passwd=PWD, port=int(PORT))
    conn.select_db(DB)
    conn.set_character_set('utf8')
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(SQL_DROP_TABLE)
    cur.execute(SQL_CREATE_TABLE)
    conn.close() 

def add_tushuo(title, info, date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(SQL_INSERT, (title, info, date))
    conn.commit()
    conn.close()
    
def query_summary():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(SQL_QUERY_SUMMARY)
    datas = cur.fetchall()
    conn.close()
    return datas

def query_content(date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(SQL_QUERY_CONTENT, (date))
    data = cur.fetchone()
    conn.close()
    return data
    
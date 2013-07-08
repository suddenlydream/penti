'''
Created on 2013-7-8

@author: huqiming
'''

from ts_summary import parse 
__penti_url__ = 'http://www.dapenti.com/blog/blog.asp?subjectid=70&name=xilei'

result = parse(__penti_url__)

for item in result:
    print(item)
    
print(result)

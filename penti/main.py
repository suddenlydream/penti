'''
Created on 2013-7-8

@author: huqiming
'''

from ts_summary import parse_summary 
# from ts_content import parse
import json
from ts_json import json_decode
from ts_content import parse_content
__penti_url__ = 'http://www.dapenti.com/blog/blog.asp?subjectid=70&name=xilei'

# result = parse(__penti_url__)

# for item in result:
#     print(item)
# str = json_encode().encode(result)

# res = parse('http://www.dapenti.com/blog/more.asp?name=xilei&id=79405')
res = parse_summary(__penti_url__)
# ss = json.dumps(res, default=json_decode, indent=2)
item = res[0]
conent = parse_content(item.link)
conent.title = item.title
ss = json.dumps(conent, default=json_decode, indent=2)
print(ss)

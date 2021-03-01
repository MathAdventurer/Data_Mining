#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/2/10
import time
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys
from lxml.builder import unicode

print(sys.getfilesystemencoding())
# reload(sys)
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'}
# sys.setdefaultencoding('utf-8')

'''重新运行之前请删除content.txt，因为文件操作使用追加方式，会导致内容太多。'''

def towrite(contentdict):
    f.writelines('回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines('回帖内容:' + unicode(contentdict['topic_reply_content']) + '\n')
    f.writelines('回帖人:' + contentdict['user_name'] + '\n\n')

def spider(url):
    html = requests.get(url,headers=header)
    print(html.text)
    selector = etree.HTML(html.text)
    print(selector)
    content_field = selector.xpath('//div[@class="l_post l_post_bright "]')
#     //*[@id="j_p_postlist"]/div[3]
#     //*[@id="j_p_postlist"]/div[3]
#     /html/body/div[5]/div/div/div[2]/div/div[4]/div[1]/div[3]/div[3]
    print(content_field)
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
        author = reply_info['author']['user_name']
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content "]/text()')[0]
        reply_time = reply_info['content']['date']
        print(content)
        print(reply_time)
        print(author)
        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time
        towrite(item)

# if __name__ == '__main__':
pool = ThreadPool(16)
f = open('content.txt','a')
time1 = time.time()
page = []
for i in range(1,21):
    newpage = 'https://tieba.baidu.com/p/6074068853?pn=' + str(i)
    page.append(newpage)
results = pool.map(spider, page)
pool.close()
pool.join()
f.close()
time2 = time.time()
print(str(time2-time1))
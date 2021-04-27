import requests
from lxml import etree
import json
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Referer': 'https://www.douban.com/'
}

url = 'https://search.jd.com/Search?keyword=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&wq=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&psort=3&click=1'
response = requests.get(url, headers=headers)
text = response.text
html = etree.HTML(text)
ul = html.xpath('//*[@id="J_goodsList"]/ul')
price=ul[0].xpath('//*/strong/i/text()')[0:10]
name=ul[0].xpath('//*/div[@class["p-img"]]/a/@title')[0:10]
#pinglun=ul[0].xpath('//*/div[@class="p-bookdetails"]/div[@class="p-commit"]/strong/a//text()')[0:10]
ac=ul[0].xpath('//*/span/a[1]/text()')[0:20]
author=[]
chubanshe=[]
for i in range(20):
    if i%2!=0:
        author.append(ac[i])
    else:
        chubanshe.append((ac[i]))
print(name)
print(chubanshe)
print(price)
print(chubanshe)
with open('编程书籍基本信息.csv', 'w', newline='', encoding='utf-8-sig')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['书名', '价格', '作者', '出版社'])
    for k in  range(10):
        book=[[name[k],price[k],author[k],chubanshe[k]]]
        f_csv.writerows(book)
f.close()
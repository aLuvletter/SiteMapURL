# -*- codeing = utf-8 -*-

import requests
import re
import os

inputurl = input("例：https://www.chiser.cc/sitemap.xml\n请输入网站地图XML链接：")
response = requests.get(inputurl, headers=headers)
html = response.text
url = str(re.findall('<loc>(.*?)</loc>', html))
url1 = url.replace('[','').replace(',','\n').replace('\'',"").replace(" ", "") #去除多余符号
f = open("SiteMapURL.txt", "w")  # 打开文件写入数据
f.write(str(url1))
f.close  # 关闭文件
print('SiteMapURL本已生成')
os.system('pause')

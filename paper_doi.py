#!/usr/bin/env python3
#coding: utf-8
# Date: 2019-01-10 22:19:48
#Author: zheng_oh
#email: 894389673@qq.com
import requests
from bs4 import BeautifulSoup as BS
import re
import urllib.request
title='Protein breakdown and release of antioxidant peptides during simulated gastrointestinal digestion and the absorption by everted intestinal sac of rapeseed proteins'
# title='Study of the fermentation conditions and the antiproliferative activity of rapeseed peptides by bacterial and enzymatic cooperation'
title_=title.replace(' ','+')
url="http://xueshu.baidu.com/s?wd=+"+title_+"&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_from=&sc_as_para=sc_lib%3A&rsv_n=2&rsv_sug2=0"
print('论文标题为：{0}'.format(title))
r=requests.get(url)
soup=BS(r.text,'lxml')
print(soup)
k=soup.find_all('a',attrs={"data-url": re.compile("doi")})
if len(k):
	print("wozhixingif")
	doi=k[0]['data-url']
else:
	k.append(soup.find_all('a',href=re.compile("doi")))
	# href="".join(k[0]['href'])
	# k[0]= urllib.unquote(href)
	print("wozhixingelseif")
	doi=k[0][0]['href']
	# doi=re.findall(r"10.+", doi)
	doi=urllib.request.unquote(doi)
	doi=re.findall(r"10.(.+?)&",doi)
	doi='10.'+doi[0]
print("-"*100)
print(type(doi))
print("-"*100)
print(doi)

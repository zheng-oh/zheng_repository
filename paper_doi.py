#!/usr/bin/env python3
#coding: utf-8
#Date: 2019-01-18 17:58:11
#Author: zheng_oh
#email: 894389673@qq.com
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
title= input("请输入论文标题:")
title_=title.replace(' ','+')
url="http://xueshu.baidu.com/s?wd=+"+title_+"&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_from=&sc_as_para=sc_lib%3A&rsv_n=2&rsv_sug2=0"
<<<<<<< HEAD
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(url)
html=driver.page_source
# print(html)
driver.close()
driver.quit()
# doi=re.findall()
soup=BS(html,'lxml')
p=soup.select('div.main-info > div.c_content > div.doi_wr > p.kw_main')
doi=p[0].text.lstrip()
n=len(doi)
print('-'*n)
print("论文的doi：{0}".format(doi))
=======
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
>>>>>>> 687c0b9bbb632e8b706b41af1e38244d9241b7e3

#!/usr/bin/env python3
#coding: utf-8
#Date: 2019-01-20 16:34:51
#Author: zheng_oh
#email: 894389673@qq.com
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import re
from PIL import Image
def set_headers():
	global headers,cookies
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	           'Accept - Encoding':'gzip, deflate',
	           'Accept-Language':'zh-CN, zh; q=0.9',
	           'Connection':'Keep-Alive',
	           'host':'twin.sci-hub.tw',
	           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
def get_doi():
	global n
	title_=title.replace(' ','+')
	url="http://xueshu.baidu.com/s?wd=+"+title_+"&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_from=&sc_as_para=sc_lib%3A&rsv_n=2&rsv_sug2=0"
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options)
	driver.get(url)
	html=driver.page_source
	driver.close()
	driver.quit()
	soup=BS(html,'lxml')
	p=soup.select('div.main-info > div.c_content > div.doi_wr > p.kw_main')
	if p:
		doi=p[0].text.lstrip()
		doi=re.findall(r"10.+", doi)
		doi=doi[0]
		n=len(doi)
		print('-'*n)
		print("论文的doi：{0}".format(doi))
		get_pdf_src(doi)
	else:
		print("对不起！输入有误或数据库未找到(>_<)")
def get_pdf_src(doi):
	doi_url='http://www.sci-hub.fun/'+doi
	# print(doi_url)
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options)
	driver.get(doi_url)
	html=driver.page_source
	driver.close()
	driver.quit()
	soup=BS(html,'lxml')
	pdf_src=soup.select('#pdf')
	if pdf_src:
		pdf_src=pdf_src[0]['src']
		# print(pdf_src)
		download_pdf(pdf_src)
	else:
		print("对不起！数据库中没有此文献，请根据doi号自行下载：{0}(>_<)".format(doi))
def download_pdf(pdf_src):
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options)
	driver.get(pdf_src)
	html_pdf=driver.page_source
	soup_pdf=BS(html_pdf,'lxml')
	p=soup_pdf.select('body > div > table > tbody > tr > td > form > input[type="text"]:nth-child(3)')
	if p:
		print("需要验证")
		driver.save_screenshot('验证码.png')
		img = Image.open("验证码.png")
		cropped = img.crop((0,150,800,370))  # (left, upper, right, lower)
		cropped.save("验证码.png")
		yzm=input("请根据图片输入验证码：")
		driver.find_element_by_name('answer').send_keys(u'{0}'.format(yzm))
		driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/form/p[2]/input').click()
		driver.close()
		driver.quit()
		download_pdf(pdf_src)	
	else:
		try:
			driver.close()
			driver.quit()
			print("验证成功")
			print('-'*n)
			print("正在下载.....")
			r=requests.get(pdf_src)
			loading(r)
		except Exception as e:
			print("您的网络不通畅，请使用此地址自行下载：{0}".format(pdf_src))
def loading(r):
	if r.status_code==200:
		filename=title+'.pdf'
		with open(filename, 'wb') as f:
		    f.write(r.content)
		print('-'*n)
		print("下载成功！")
		title= input("请输入论文标题:")
		get_doi()	
	else:
		time.sleep(5)
		print("网速有点慢，请耐心等待.....")
		loading(r)
def input_id():
	global userid
	userid=input("请输入您的ID:")
	if userid in use_list:
		print("尊敬的{0}，欢迎您使用！".format(userid))
		global title
		title= input("请输入论文标题:")
		get_doi()
	else:
		print("ID错误，重新输入或请联系微信：zheng_oh")
		input_id()
if __name__ == '__main__':
	headers=set_headers()
	try:
		url="https://raw.githubusercontent.com/zheng-oh/zheng_repository/master/users.txt"
		use_rep=requests.get(url,timeout=5)
		l=use_rep.text
		use_list=l.split()
		input_id()
	except BaseException as e:
		print("貌似网络不通畅(>_<)")

	
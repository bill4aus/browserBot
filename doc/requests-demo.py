# -*- coding: utf-8 -*-
import browserBot
import json
import time
import re
from requests_html import HTML

bot = browserBot.requests()

proxy = {'http':'http://H99BF0149RU3K52P:5BE76E4D56AB0010@http-pro.abuyun.com:9010'}
bot.setProxy(proxy)

ua = browserBot.randomua()
header = browserBot.headerGen(ua,'games.sina.cn','http://games.sina.com.cn/news/')
bot.setHeader(header)


# headers ={
# 		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 		'Accept-encoding': 'gzip, deflate',
# 		'Accept-language': 'zh-CN,zh;q=0.9',
# 		'Connection': 'keep-alive',
# 		'Cache-Control':' max-age=0',
# 		# 'Cookie': 'SINAGLOBAL=7'+randomnumber(10)+'51.894.156'+randomnumber(5)+'88833; SCF='+randomstring(6)+'-'+randomstring(14)+'-'+randomstring(7)+'-'+randomstring(12)+'_'+randomstring(29)+'-'+randomstring(14)+'.; SUHB='+randomstring(10)+'_mNL; ALF=159'+randomnumber(7)+'; _s_tentry=login.sina.com.cn; Apache='+randomnumber(13)+'.571.15689'+randomnumber(13)+'; ULV=15689'+randomnumber(13)+':3:1:1:'+randomnumber(13)+'.571.1568'+randomnumber(13)+':15668'+randomnumber(13)+'; SUB=_2Ak'+randomstring(13)+'oRz2_ka'+randomstring(13)+'l-yT'+randomstring(13)+'M-v'+randomstring(9)+'tI_'+randomstring(13)+'; SUBP=00'+randomstring(13)+'-Ws9jqgMF5'+randomstring(13)+'W'+randomstring(13)+'; WBtopGlobal_register_version=307744aa77dd5677; UOR=,,www.techweb.com.cn; login_sid_t='+randomstring(15)+'895'+randomstring(7)+'07; cross_origin_proto=SSL',
# 		# 'upgrade-insecure-requests':1,
# 		'Referer':'http://games.sina.com.cn/news/',
# 		'Host':'games.sina.cn',
# 		'User-Agent': ua,
# }

# 科技
# 旅游
# 家居
# 教育
# 美食
# 民生
# 汽车
# 时尚
# 时政
# 体育
# 医疗
# 玩乐
# 游戏
# 艺术

purllist = []
pagelist = browserBot.pageUrlGen('http://games.sina.cn/pc/newslist.d.html?page=','&pagesize=53',1,2)
for turl in pagelist:
	print(turl)
	page=bot.open(turl)
	print(page.status_code)
	print(page.html.find('title', first=True).text)
	postdivlist = page.html.find('.hp_newslist li  a')
	print(page.html.find('#content_wrapper',first=True).html)
	for pdiv in postdivlist:
		purl = pdiv.attrs['href']
		print(purl)
		purllist.append(purl)
	time.sleep(1)

# purllist = []
# # 4243
# starcount =1
# everytimepages = 200

# startpagenumber = (starcount-1)*everytimepages
# endpagenumber = startpagenumber+everytimepages
# pagelist = range(startpagenumber,endpagenumber)
# # print(pagelist)
# for pnumber in pagelist:
# 	# print(pnumber)
# 	turl = 'http://games.sina.cn/pc/newslist.d.html?page='+str(pnumber)+'&pagesize=53'
# 	# print(turl)
# 	page=bot.open(turl)
# 	print(page.status_code)
# 	print(page.html.find('title', first=True).text)
# 	postdivlist = page.html.find('#content_wrapper  .tabody .tli .hp_newslist li  a')
# 	for pdiv in postdivlist:
# 		purl = pdiv.attrs['href']
# 		# print(purl)
# 		purllist.append(purl)
# 	time.sleep(1)




# start to crawl
for purl in purllist:
	print(purl)
	ppage=bot.open(purl)
	# print(ppage.html.find('.detail',first=True).text)
	# contentdivlist=ppage.html.find('.entry-content p span')
	# print(len(contentdivlist))
	# for cdiv in contentdivlist:
	# 	print(cdiv.text)
	# contenttext = ''.join([cdiv.text for cdiv in contentdivlist])
	filename = browserBot.randomstring(8)
	with open('yuliao/'+filename+'.txt','w+') as f:
		try:
			# htmls = str(ppage.html.find('.crticalcontent #artibody ',first=True).html)
			# # print(htmls)
			# doc  = re.sub(r'<(script).*?>[\s\S]*?<\/\1>', '',str(htmls))
			# doc  = re.sub(r'<div.*class="page_fenye">.*?</div>', '',str(doc))
			# # print(doc)
			# mhtml = HTML(html=doc)
			# contenttext = mhtml.find('.n_show',first=True).text


			contenttext=ppage.html.find('.crticalcontent #artibody',first=True).text

			print(contenttext)
			

			f.write(contenttext)
		except Exception as e:
			# raise e
			pass
		
# coding:utf-8
from datetime import datetime
import os
# from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler
# from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
import random
import json

from selenium.webdriver.common.keys import Keys


# def getPureDomainCookies(cookies):
# 	domain2cookie={}  #做一个域到cookie的映射
# 	for cookie in cookies:
# 		domain=cookie['domain']
# 		if domain in domain2cookie:
# 			domain2cookie[domain].append(cookie)
# 		else:
# 			domain2cookie[domain]=[]
# 	maxCnt=0
# 	ansDomain=''
# 	for domain in domain2cookie.keys():
# 		cnt=len(domain2cookie[domain])
# 		if cnt > maxCnt:
# 			maxCnt=cnt
# 			ansDomain=domain
# 	ansCookies=domain2cookie[ansDomain]
# 	return ansCookies


class chrome():
	def __init__(self):
		
		self.browser= webdriver.Chrome()
		# self.browser.maximize_window()
		# self.browser.set_page_load_timeout(5)
		# self.browser.set_script_timeout(5)
		self.random = random
		self.Keys = Keys
		self.curhandle = None
		time.sleep(2)
	def open(self,url,waittime=None,cookiefile=None):
		self.url = url
		
		self.browser.get(self.url)
		self.msleep()

		if cookiefile==None:
			pass
		else:
			# cookies
			self.load_cookie(cookiefile)
			self.msleep()

			self.browser.refresh()

		if waittime==None:
			pass
			self.msleep(0.3)
			# time.sleep(random.random())
		else:
			print('sleep {} seconds'.format(waittime))
			self.msleep(waittime)

		self.curhandle = self.browser.current_window_handle

	def openwithsource(self,openurlstring,refer,waittime=None):
		
		# # 带跳转的打开方式
		try:
			self.browser.get(refer)
		except Exception as e:
			# raise e
			self.browser.quit()
		
		time.sleep(3)

		try:
			set_wyswyg_js = 'location.href="'+openurlstring+'";'
			self.javascript(set_wyswyg_js)
		except Exception as e:
			# self.browser.quit()
			pass

		
		if waittime==None:
			pass
			self.msleep(0.3)
			# time.sleep(random.random())
		else:
			print('sleep {} seconds'.format(waittime))
			self.msleep(waittime)
			
		# self.screen("./wechat.png")
		# time.sleep(3)

		# try:
		# 	self.check_website()
		# except Exception as e:
		# 	# raise e
		# 	self.browser.quit()

		# while True:
		# 	print('code check and  recognise .......')

		# 	if self.check_vertifycode()==None:
		# 		pass
		# 		print("cotinune")
		# 		time.sleep(5)
		# 		self.screen("./wechat.png")
		# 	else:
		# 		break;

	def close(self):
		self.browser.quit()
	def save_cookie(self,cookiefile):
		cookies= self.browser.get_cookies()
		self.save_to_local_cookies(cookiefile,cookies)
	def load_cookie(self,cookiefile):
		pass

		cookielist = self.get_local_cookies(cookiefile)
		# cookielist = getPureDomainCookies(cookielist)
		for coo in  cookielist:
			# print(coo)
			if 'expiry' in coo:
				del coo['expiry']
			if coo['domain'][1:] in self.browser.current_url:
				self.browser.add_cookie(coo)
	# def get_cookie_str_from_broswer(self):
	# 	bcokkies = self.browser.get_cookies()
	# 	# cookie = [item["name"] + "=" + item["value"] for item in bcokkies]
	# 	# cookiestring = '; '.join(item for item in taobaocookie)
	# 	return bcokkies
	def save_to_local_cookies(self,filename,cookiedict):
		fw=open(filename,'w')
		json.dump(cookiedict,fw)
		fw.close()
	#获取本地cookie
	def get_local_cookies(self,cookiefile):
		try:
			frr=open(cookiefile,'r')
			frr.close()
		except:
			frr=open(cookiefile,'w')
			frr.close()
		fr=open(cookiefile,'r')
		
		try:
			jsontext = fr.read()
			cookielist=json.loads(jsontext)
		except:
		   cookielist=[]
		fr.close()
		#print(cookielist)
		return cookielist

	def trytofind(self,cssrule):
		try:
			if self.browser.find_element_by_css_selector(cssrule).is_displayed():
				# print('表情按钮 找到了')
				return True
			else:
				# print('表情按钮 没找到')
				return False
		except Exception as e:
			# raise e
			# print('表情按钮 没找到')
			return False
	def screen(self,screen_file):
		self.browser.save_screenshot(screen_file)
	def javascript(self,jsfunction):
		self.browser.execute_script(jsfunction)
	def getelementbycss(self,css_selector):
		# try:
		# 	res=WebDriverWait(source,0.5).until(lambda source:self.browser.find_element_by_css_selector(css_selector) , " open fail")

		# 	if res==False:
		# 		return None
		# 	else:
		# 		elem=self.browser.find_element_by_css_selector(css_selector)
		# 		return elem
		# except Exception, e:
		# 	return None
		elem=self.browser.find_element_by_css_selector(css_selector)
		return elem
	def getelementsbycss(self,css_selector):
		# try:
		# 	res=WebDriverWait(source,0.5).until(lambda source:self.browser.find_elements_by_css_selector(css_selector) , " open fail")
		# 	if res==False:
		# 		return []
		# 	else:
		# 		elem=self.browser.find_elements_by_css_selector(css_selector)
		# 		return elem
		# except Exception, e:
		# 	return []
		elem=self.browser.find_elements_by_css_selector(css_selector)
		if elem:
			return elem
		else:
			return []
	def sendkey(self,sdkey,cssrule=None):
		# if cssrule==None:
		# 	pass
		# else:
		# 	self.browser.switch_to.active_element.send_keys(sdkey)
		self.browser.switch_to.active_element.send_keys(sdkey)
	def dataload_by_json(self,jsonfile):
		f_tiezi=open(jsonfile,'r')
		jsontext = f_tiezi.read()
		jsontext = jsontext.replace('\n','')
		tiebaList=json.loads(jsontext)
		return tiebaList
	def dataload_by_line(self,filename):
		corpus = []
		with open(filename,'r',encoding='utf-8') as f:
			for cps in f.readlines():
				corpus.append(cps)
		return corpus

	def trytofind_byhand(self,cssrule):
		# global facebutton
		# 
		# 试探
		facebutton = None
		while 1:
			try:
				x = input('x:')
				y = input('y:')
				z = input('z:')
				time.sleep(0.5)
				x = int(x)
				y = int(y)
				z = int(z)
				# print('试着点击 表情按钮')
				# print(startx,starty)
				if z==1:
					self.click_locxy([x,y],left_click=True)
					time.sleep(2)
				else:
					self.click_locxy([x,y],left_click=False)
				# time.sleep(1)

				time.sleep(2)
				try:
					self.trytofind(cssrule)
					# buttonfound =True
					print('button找到 {},{}'.format(x,y))
					# facebutton.append((x,y))
					facebutton=(x,y)
					print(facebutton)
					break
				except Exception as e:
					print(str(e))
					print('button没找到')
					pass
				
				

			except Exception as e:
				# raise e
				print(str(e))
				pass
		return facebutton
	def move_mouse(self,xr,yr):
		pass
		# 移动鼠标
		x_pos = random.randint(xr[0], xr[1])
		y_pos = random.randint(yr[0], yr[1])
		# bdbrowser.execute(Command.MOVE_TO,{'xoffset':x_pos,'yoffset':y_pos})

		ActionChains(self.browser).move_by_offset(x_pos,y_pos).perform()
		# time.sleep(random.random())
		time.sleep(random.random())
		ActionChains(self.browser).move_by_offset(x_pos,y_pos).perform()
		time.sleep(0.2)
		ActionChains(self.browser).move_by_offset(-x_pos, -y_pos).perform()
	# def send_key(self):
	# 	pass
	# 	try:
	# 		pass
	# 		# bdbrowser.find_element_by_css_selector('.body-container-focus').send_keys("就是的")
	# 	except Exception as e:
	# 		# raise
	# 		pass
	# 	else:
	# 		pass
	# 		# js_kind = 'document.getElementById("#ueditor_replace").innerHTML="就是的" '
	# 		# bdbrowser.execute_script(js_kind)
	# 	finally:
	# 		pass
	# 		# bdbrowser.find_element_by_css_selector('#ueditor_replace').attr('innerHTML','妈的')
	def click_locxy(self, face_pos, left_click=True):
		'''
		dr:浏览器
		x:页面x坐标
		y:页面y坐标
		left_click:True为鼠标左键点击，否则为右键点击
		'''
		x=face_pos[0]
		y=face_pos[1]

		if left_click:
			ActionChains(self.browser).move_by_offset(x, y).click().perform()
			time.sleep(random.random())
			
			# 关闭误操作打开的窗口
			self.keep_one_window()
		else:
			ActionChains(self.browser).move_by_offset(x, y).context_click().perform()
			# time.sleep(0.5)
			# ActionChains(bdbrowser).send_keys(Keys.ESCAPE).perform()
			# bdbrowser.switch_to.active_element.send_keys(Keys.ESCAPE)
			# elem = bdbrowser.find_element_by_css_selector('body').click()
			# time.sleep(1)
			# bdbrowser.switch_to.active_element.send_keys(Keys.ESCAPE)
			# 
			# it works
			# ActionChains(bdbrowser).drag_and_drop(bdbrowser.find_element_by_css_selector('#ueditor_replace'), bdbrowser.find_element_by_css_selector('body')).perform()
			# time.sleep(0.2)
		ActionChains(self.browser).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前
	def scroll(self,top_margin):
		pass
		# 鼠标滚动
		js="var q=document.documentElement.scrollTop="+str(top_margin)
		self.browser.execute_script(js)
		time.sleep(random.random())
	def msleep(self,sint=None):
		# time.sleep(random.random())
		if sint==None:
			time.sleep(random.random())
		else:
			time.sleep(sint)

	def keep_one_window(self):
		# print(len(self.browser.window_handles))
		while len(self.browser.window_handles) >1:
			for handle in self.browser.window_handles:
				if handle != self.curhandle:
					self.browser.switch_to_window(handle)
					self.browser.close()
		self.browser.switch_to_window(self.browser.window_handles[0])
	def find_by_xy(self,facebutton,obj_cssrule):
		for _x,_y in facebutton:
			try:
				print('try:{},{}'.format(_x,_y))
				self.click_locxy([_x,_y],left_click=True)
				time.sleep(2)

				# # 关闭误操作打开的窗口
				# self.keep_one_window()

				if self.trytofind(obj_cssrule):
					# buttonfound = True
					# startx = _x
					# starty = _y
					print('目标元素已经找到')
					return True,_x,_y
				else:
					print('没找到呀，下一个再试')
					buttonfound = False
					# ActionChains(bdbrowser).drag_and_drop(bdbrowser.find_element_by_css_selector('#ueditor_replace'), bdbrowser.find_element_by_css_selector('body')).perform()
					
			except Exception as e:
				# raise e
				pass

		print('没找目标元素')
		# 关闭误操作打开的窗口
		self.keep_one_window()
		return False,None,None
	def quit(self):
		# 关闭文件
		# f.close()
		# 关闭浏览器 好像退出后,进程还在?需要确认,占用内存
		try:
			self.browser.quit()
		except Exception as e:
			# raise e
			pass
		# self.browser.quit()
		# 退出python进程
		exit()
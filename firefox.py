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

from selenium.webdriver.common.keys import Keys

class chrome():
	def __init__(self):
		
		self.browser= webdriver.Chrome()
		self.browser.maximize_window()
		self.browser.set_page_load_timeout(5)
		self.browser.set_script_timeout(5)
		time.sleep(2)
	def open(self,url):
		self.url = url
		self.browser.get(self.url)
		time.sleep(2)
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
	def send_key(self):
		pass
		try:
			pass
			# bdbrowser.find_element_by_css_selector('.body-container-focus').send_keys("就是的")
		except Exception as e:
			# raise
			pass
		else:
			pass
			# js_kind = 'document.getElementById("#ueditor_replace").innerHTML="就是的" '
			# bdbrowser.execute_script(js_kind)
		finally:
			pass
			# bdbrowser.find_element_by_css_selector('#ueditor_replace').attr('innerHTML','妈的')
	def click_locxy(self, x, y, left_click=True):
		'''
		dr:浏览器
		x:页面x坐标
		y:页面y坐标
		left_click:True为鼠标左键点击，否则为右键点击
		'''

		if left_click:
			ActionChains(self.browser).move_by_offset(x, y).click().perform()
			time.sleep(random.random())
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
	def scroll(self):
		pass
		# 鼠标滚动
		js="var q=document.documentElement.scrollTop="+str(random.randint(10,400))
		bdbrowser.execute_script(js)
		time.sleep(random.random())

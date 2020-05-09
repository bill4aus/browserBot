# coding:utf-8

import browserBot
import json

def faceButton(startx,starty):
	face_dict = {
		'dianzan':(startx-110,starty+110),
		'tiaopi':(startx-110,starty+80),
		'weixiao':(startx-210,starty+80),
		'daxiao':(startx-160,starty+80),
		'kaixin':(startx-60,starty+130),
		'weisuo':(startx,starty+130),
		'hua':(startx+50,starty+170),
		'ku':(startx,starty+50),
		}
	facelist = ['dianzan','tiaopi','weixiao','daxiao','kaixin','weisuo','hua','ku']
	return face_dict,facelist

bot = browserBot.chrome()

# 登陆
bot.open('https://tieba.baidu.com',20,'./cookie.broswer')
bot.save_cookie('./cookie.broswer')

corpus = bot.dataload_by_line('./corpus.txt')

# 表情按钮位置 试错列表
face_turnon_button_pos =[(750,550),(850,380),(480,350),(515, 295)]

while 1:
	# 加载 帖子列表
	tiebaList=bot.dataload_by_json('tiezi.txt')

	# 执行点赞任务
	for tie in tiebaList:

		tieba = tie['tieba']
		tiezi = tie['tiezi']

		bot.open(tieba,2)
		bot.open(tiezi,1)

		# 如果没有权限发帖，跳过
		if bot.trytofind('.poster_warning'):
			continue

		# bot.scroll(bot.random.randint(400,900))
		bot.scroll('document.body.clientHeight')

		bot.msleep(2)

		# 手工寻找按钮位置
		# f_btn = bot.trytofind_byhand('.edui-dropdown-menu .emotion_container')
		# if f_btn == None:
		# 	pass
		# else:
		# 	facebutton.append(f_btn)

		buttonfound,button_startx,button_starty = bot.find_by_xy(face_turnon_button_pos,'.edui-dropdown-menu .emotion_container')
		

		if buttonfound:
			face_dict,facelist = faceButton(button_startx,button_starty)
			facename = bot.random.choice(facelist)
			face_pos = face_dict[facename]
			print('表情为 {}'.format(facename))
			print('找到以后，直接选择 表情,位置：{},{}'.format(face_pos[0],face_pos[1]))
			try:
				bot.click_locxy(face_pos,left_click=True)
				bot.msleep(0.5)
				# 点击
				print('点击 发布')
				bot.sendkey(bot.random.choice(corpus))
				# bot.browser.switch_to.active_element.send_keys(bot.random.choice(corpus))
				bot.msleep(0.5)
				bot.sendkey(bot.Keys.CONTROL + bot.Keys.ENTER)
				# bot.browser.switch_to.active_element.send_keys(bot.Keys.CONTROL + bot.Keys.ENTER)

			except Exception as e:
				# raise e
				pass
				print('出错，并没有找到')
				print(str(e))
				# buttonfound =False
				# 是否需要缓一缓？？
				# time.sleep(random.randint(30,60))

		# 每一个帖子 暂停 1-10秒
		bot.msleep(bot.random.randint(1,10))

	# 每一轮 暂停1-2分钟
	bot.msleep(bot.random.randint(60,120))

bot.close()

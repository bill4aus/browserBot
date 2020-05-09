
from nonebot import on_command,CommandSession

from nonebot import get_bot



import requests
import json
import urllib
import time
import re
import selenium
from selenium import webdriver
from urllib import parse
#from apscheduler.schedulers.blocking import BlockingScheduler

from datetime import datetime

import nonebot

from aiocqhttp.exceptions import Error as CQHttpError
import random

import json








#淘宝相关function

def get_tao_kou_ling(text):
    res = re.findall(r"[￥($]?[a-zA-Z0-9]{11}[￥)$]?",text)
    #official_res = re.findall(r"[a-zA-Z0-9]{11}",text)
    #tkl = '￥'+str(official_res[0])+'￥'
    return res[0]
#print(get_tao_kou_ling('伊利149元-50 20点￥pklc15juS6F￥'))





def get_objurl_by_clickurl(click_url):
    if click_url == None:
        return None
    chrom_opt = webdriver.ChromeOptions()
    prefs = { "profile.managed_default_content_settings.images": 2 }
    chrom_opt.add_experimental_option("prefs", prefs)
    driver= webdriver.Chrome(chrome_options = chrom_opt)
    driver.get(click_url)
    time.sleep(0.9)
    obj_url = driver.current_url
    if 'coupon' in obj_url:
        try:
            driver.find_element_by_css_selector("#J_wrap .item-info-con a").click()
            time.sleep(0.9)
            obj_url = driver.current_url
        except:
            driver.quit()
    driver.quit()
    #print(obj_url)
    return obj_url

'''
def get_clickurl_by_taokouling(kouling_str):
    userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    ApiUrl = "https://www.taokouling.com/index/taobao_tkljm"
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept - Encoding':'gzip, deflate, br',
                   'Accept-Language':'zh-CN,zh;q=0.9',
                   'Connection':'Keep-Alive',
                   #'Host':'www.taokouling.com',
                   'Conent-Type':'application/x-www-form-urlencoded',
                   'User-Agent':userAgent,
                   'Referer':'https://www.taokouling.com/index/taobao_tkljm',
                   'Cookie':'PHPSESSID=3f22tl7rtb2f4olii1l6ova4mv; UM_distinctid=1709049bae828d-0696aa68f0ec36-36664c08-1fa400-1709049baeb71f; CNZZDATA1261806159=1096058281-1582968109-https%253A%252F%252Fwww.baidu.com%252F%7C1582973528; Hm_lvt_73f904bff4492e23046b74fe0d627b3d=1582968716,1582974365; Hm_lpvt_73f904bff4492e23046b74fe0d627b3d=1582974376',
                   'X-Requested-With':'XMLHttpRequest'
               }

    params = {"text":kouling_str}
        
    r = requests.post(ApiUrl, data=params,headers=headers, timeout=3)
    rdata=json.loads(r.text)
    newurl = rdata['data']['url']
    #print(newurl)
    return newurl
'''
def get_clickurl_by_taokouling(kouling_str):

    #重新处理下，这个要求严格
    official_res = re.findall(r"[a-zA-Z0-9]{11}",kouling_str)
    tkl = '￥'+str(official_res[0])+'￥'
    
    userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    ApiUrl = "http://api-test.shihuizhu.com/tool/revertTkc"
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept - Encoding':'gzip, deflate, br',
                   'Accept-Language':'zh-CN,zh;q=0.9',
                   'Connection':'Keep-Alive',
                   #'Host':'www.taokouling.com',
                   'Conent-Type':'application/x-www-form-urlencoded',
                   'User-Agent':userAgent,
                   #'Referer':'https://www.taokouling.com/index/taobao_tkljm',
                   'Cookie':'PHPSESSID=3f22tl7rtb2f4olii1l6ova4mv; UM_distinctid=1709049bae828d-0696aa68f0ec36-36664c08-1fa400-1709049baeb71f; CNZZDATA1261806159=1096058281-1582968109-https%253A%252F%252Fwww.baidu.com%252F%7C1582973528; Hm_lvt_73f904bff4492e23046b74fe0d627b3d=1582968716,1582974365; Hm_lpvt_73f904bff4492e23046b74fe0d627b3d=1582974376',
                   'X-Requested-With':'XMLHttpRequest'
               }

    params = {"tkl":tkl}
    r = requests.get(ApiUrl, params=params,headers=headers, timeout=3)
    print(r.text)
    rdata=json.loads(r.text)
    newurl = rdata['data']
    if newurl == '':
        return None
    else:
        #print(newurl)
        return newurl





def get_myurlinfo_by_objurl(obj_url):
    global taobaocookiestring
    userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

    ApiUrl = "https://pub.alimama.com/openapi/json2/1/gateway.unionpub/pub.xt.entry?"
    #ApiUrl = "https://pub.alimama.com/openapi/json2/1/gateway.unionpub/pub.xt.entry?_data_=%7B%22floorId%22%3A30677%2C%22refpid%22%3A%22mm_42846524_36726195_131660144%22%2C%22variableMap%22%3A%7B%22url%22%3A%22https%3A%2F%2Fdetail.tmall.com%2Fitem.htm%3Fid%3D559925534261%26ali_trackid%3D2%3Amm_127554927_524900174_108925300450%3A1582968830_265_1289644110%26spm%3Da2159r.13376465.0.0%26ak%3D25635011%26ut_sk%3D1.utdid_24779903_1582959411561.TaoPassword-Outside.taoketop%22%7D%2C%22t%22%3A1582971112814%2C%22_tb_token_%22%3A%223b793eee54575%22%2C%22pvid%22%3Anull%7D"

    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept - Encoding':'gzip, deflate, br',
                   'Accept-Language':'zh-CN,zh;q=0.9',
                   'Connection':'Keep-Alive',
                   #'Host':'pub.alimama.com',
                   'Conent-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                   'User-Agent':userAgent,
                   'Referer':'https://pub.alimama.com/manage/links/index.htm?spm=a219t.11816985.1998910419.db62784001.610175a5NX4KSS',
                   'Cookie':taobaocookiestring,
                   'X-Requested-With':'x-requested-with'
               }

    params = {"_data_":{"floorId":30677,"refpid":"mm_42846524_36726195_131660144","variableMap":{"url":obj_url},"t":1582971112814,"_tb_token_":"3b793eee54575","pvid":"null"}}
    paramsStr = urllib.parse.urlencode(params)


    r = requests.get(ApiUrl+paramsStr, headers=headers, timeout=3)
    print(r.text)
    resjson = json.loads(r.text)

    mycode = None
    if resjson['data'].get('couponLinkTaoToken')==None:
        pass
        mycode = resjson['data'].get('taoToken')
    else:
        mycode = resjson['data'].get('couponLinkTaoToken')
    return mycode



def get_my_taobao_url_by_kouling(adstring):
    kouling = get_tao_kou_ling(adstring)
    if kouling ==None:
        return None
    else:
        return adstring
    '''
    click_url =get_clickurl_by_taokouling(kouling)
    obj_url = get_objurl_by_clickurl(click_url)
    if obj_url==None:
        pass
        newadstring=None
    else:
        my_taobao_code = get_myurlinfo_by_objurl(obj_url)
        newadstring = adstring.replace(kouling,my_taobao_code)
    return newadstring
    '''


#淘宝相关function






#京东相关function


def get_realurl_by_adurl(ad_url):
    chrom_opt = webdriver.ChromeOptions()
    prefs = { "profile.managed_default_content_settings.images": 2 }
    chrom_opt.add_experimental_option("prefs", prefs)
    
    driver= webdriver.Chrome(chrome_options = chrom_opt)
    
    driver.get(ad_url)
    time.sleep(0.9)
    obj_url = driver.current_url

    if 'jingfen' in obj_url:
        try:
            driver.find_element_by_css_selector(".skuWrap a").click()
            time.sleep(0.9)
            obj_url = driver.current_url
        except:
            driver.quit()
        
    
    driver.quit()
    #print(obj_url)
    return obj_url


def get_productid_by_realurl(realurl):
    url_change = parse.urlparse(realurl)
    productid=None

    res = re.findall(r"\/\d{1,}\.html",url_change.path)
    
    if len(res)>0:
        pass
        res = re.findall(r"\/\d{1,}\.html",url_change.path)
        productid = res[0].replace('/','').replace('.html','')
        
    else:
                
        paramdict = {}
        for paramstr in url_change.query.split('&'):
            params=paramstr.split('=')
            paramdict[params[0]] = params[1]
        try:
            productid=paramdict['wareId']
        except:
            productid=None
    #print(productid)
    return productid


def get_productid_by_adurl(ad_url):
    realurl = get_realurl_by_adurl(ad_url)
    productid = get_productid_by_realurl(realurl)
    return productid


def get_myurl_by_productid(productid):
        
    query_url = 'https://union.jd.com/proManager/index?pageNo=1&keywords='+productid
    jdbrowser.get(query_url)
    time.sleep(1)
    jdbrowser.find_element_by_xpath("//button[@id='first_sku_btn']").click()
    time.sleep(1)
    myurl = jdbrowser.find_element_by_xpath("//*[@id='pane-0']/div/div[2]/div/input").get_attribute('value')
    jdbrowser.get(jd_tool_4_query)
    #print(myurl)
    return myurl


def get_adurl_by_adstring(adstring):
    res = re.findall(r"https:\/\/\S{1,}\.jd\.com\/\S{6}",adstring)
    return res[0]

def get_myurl_by_adstring(adstring):
    adurl = get_adurl_by_adstring(adstring)
    productid = get_productid_by_adurl(adurl)
    #print(productid)
    if productid ==None:
        newadstring==None
    else:
        myurl =get_myurl_by_productid(productid)
        newadstring = adstring.replace(adurl,myurl)
    return newadstring



#京东相关function






#区别是京东还是淘宝 的推广

def is_jd_or_taobao(messagetext):
    res1 = re.findall(r"[￥($][a-zA-Z0-9]{11}[￥)$]",messagetext)
    res2 = re.findall(r"https:\/\/\S{1,}\.jd\.com\/\S{6}",messagetext)
    
    if len(res1)>0:
        return 'taobao'
    elif len(res2)>0:
        return 'jd'
    else:
        return None


def get_cookie_str_from_broswer(taobaobrowser):
    tb_cokkies = taobaobrowser.get_cookies()
    taobaocookie = [item["name"] + "=" + item["value"] for item in tb_cokkies]
    taobaocookiestring = '; '.join(item for item in taobaocookie)
    #return taobaocookiestring
    #print(tb_cokkies)
    return tb_cokkies,taobaocookiestring



#获取本地cookie
def get_local_cookies(cookiefile):
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
def save_to_local_cookies(filename,cookiedict):
    fw=open(filename,'w')
    json.dump(cookiedict,fw)
    fw.close()

def js_aotu_refresh(driver,which):
    if which == 'jd':
        pageurl = random.choice(['https://union.jd.com/index'])
        pass
    elif which=='taobao':
        pass
        pageurl = random.choice(['https://pub.alimama.com/','https://pub.alimama.com/promo/search/index.htm','https://pub.alimama.com/manage/selection/list.htm','https://pub.alimama.com/manage/effect/overview.htm','https://pub.alimama.com/manage/overview/index.htm'])

    driver.get(pageurl)
    #time.sleep(0.5)
    #driver.execute_script("interval1=setInterval(function(){location.reload() },1000*16);");

userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
pubheaders = {
    'User-Agent':userAgent,
    }

#先把商品查询api工具打开，备用



#jd
jd_tool_4_query = 'https://union.jd.com/index'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
jdbrowser= webdriver.Chrome(options=chrome_option)
jd_cookies = get_local_cookies('./jd.cookie')
for jcookie in jd_cookies:
    if jcookie['domain'] == '.jd.com':
        print(jcookie)
        #jdbrowser.add_cookie(jcookie)
time.sleep(3)
jdbrowser.get(jd_tool_4_query)
#time.sleep(2)
#js = "inputFocus('#loginname')"
#jdbrowser.execute_script(js)
#jdbrowser.find_element_by_css_selector('.fore1 input').send_keys("qy1120319")
#jdbrowser.find_element_by_css_selector('.fore2 input').send_keys("Cyqy1929")
time.sleep(30)

jdcookies ,jdcookiestr= get_cookie_str_from_broswer(jdbrowser)
save_to_local_cookies('./jd.cookie',jdcookies)




# #taobao
# taobao_tool_query = 'https://pub.alimama.com/'
# #taobao_tool_query ='https://www.alimama.com/member/login.htm?forward=http%3A%2F%2Fpub.alimama.com%2Fmyunion.htm'

# chrome_option = webdriver.ChromeOptions()
# #chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式
# chrome_option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
# #options=chrome_option
# taobaobrowser= webdriver.Chrome(options=chrome_option)
# taobao_cookies = get_local_cookies('./taobao.cookie')
# for tcookie in taobao_cookies:
#     print(tcookie)
#     #taobaobrowser.add_cookie(tcookie)
# time.sleep(3)
# taobaobrowser.get(taobao_tool_query)
# time.sleep(1)
# #beforeWin = taobaobrowser.current_window_handle





time.sleep(30)
#taobaobrowser.find_element_by_xpath('//*[@id="magix_vf_header"]/div/div[2]/div[1]/ul/li[1]/a').click()
#time.sleep(10)



taobaocookies ,taobaocookiestring= get_cookie_str_from_broswer(taobaobrowser)
save_to_local_cookies('./taobao.cookie',taobaocookies)



bot = get_bot()



jd_workiing = 0

tasklist =[]


@bot.on_message('group')  #监听所有群组消息
async def handle_group_message(ctx):
    global jd_workiing
    global jdbrowser
    global taobaobrowser
    

    
    
    
    #group_list = await session.bot.get_group_list()
    #for group in group_list:
    #    print(group)

    #刷新，避免cookie过期
    js_aotu_refresh(jdbrowser,'jd')
    js_aotu_refresh(taobaobrowser,'taobao')


    
    #print("group ctx>>",ctx)
    #print(ctx)

    
    if ctx['message_type'] == 'group':
        pass
        messagetext = str(ctx['message'].extract_plain_text())
        socketmessage = {'message_type':ctx['message_type'],'group_id':ctx['group_id'],'user_id':ctx['user_id'],'message':messagetext}
    



    #or ctx['group_id']==1002300170
    if ctx['message_type']=='group' and (ctx['group_id']==884050926 or ctx['group_id']==761223071 or ctx['group_id']==866299255):
        #await session.bot.send_group_msg(group_id=798301708,message='收到消息，消息为：xxx')
        #await bot.send_group_msg(group_id=798301708, message='收到消息，消息为：'+str(ctx['raw_message'])) # 发送群消息
        messagetext = str(ctx['message'].extract_plain_text())
        #messagetext = str(ctx['raw_message'])

        #tasklist.append(messagetext)
        
        
        if jd_workiing == 0:
            pass
            jd_workiing=1
        else:
            return False
        
        
        whichone=is_jd_or_taobao(messagetext)
        print(whichone)
        if whichone == None:
            pass
            jd_workiing=0
        else:
            if whichone=='taobao':
                # try:
                #     mytaobaoadinfo=get_my_taobao_url_by_kouling(messagetext)
                #     if mytaobaoadinfo==None:
                #         pass
                #     else:
                #         await bot.send_group_msg(group_id=798301708, message=str(mytaobaoadinfo)) # 发送群消息
                # except Exception as e:
                #     print(str(e))
                #     pass
                jd_workiing=0
                
            elif whichone=='jd':
                try:
                    myjdadinfo=get_myurl_by_adstring(messagetext)
                    if myjdadinfo == None:
                        pass
                    else:
                        await bot.send_group_msg(group_id=798301708, message=str(myjdadinfo)) # 发送群消息
                except  Exception as e:
                    print(str(e))
                    pass
                jd_workiing=0
                
        
        



@on_command('get_msg', aliases=('刷新',))
async def get_msg(session: CommandSession):
    #group_list = await session.bot.get_group_list()
    #for group in group_list:
    #    print(group)
    global jdbrowser
    global taobaobrowser

    #刷新，避免cookie过期
    #jdbrowser.get(jd_tool_4_query)
    js_aotu_refresh(jdbrowser,'jd')
    #taobaobrowser.get(taobao_tool_query)
    js_aotu_refresh(taobaobrowser,'taobao')
        


@on_command('send_group_msg', aliases=('群发',))
async def send_group_msg(session: CommandSession):
    await session.bot.send_group_msg(group_id=798301708,message='大家好，欢迎大家上车！我是发车小能手，嘻嘻~~~')


'''
@nonebot.scheduler.scheduled_job('cron', second='30')
async def _():
    global jdbrowser
    global taobaobrowser
    
    #刷新，避免cookie过期
    #jdbrowser.get(jd_tool_4_query)
    js_aotu_refresh(jdbrowser,'jd')
    #taobaobrowser.get(taobao_tool_query)
    js_aotu_refresh(taobaobrowser,'taobao')

'''



'''
def task_name():
    if len(tasklist) == 0:
        print('null')
        return False
    else:
        print('ok')
        pass
    newtask = tasklist.pop()
    whichone=is_jd_or_taobao(newtask)
    print(whichone)
    if whichone == None:
        pass
    else:
        if whichone=='taobao':
            mytaobaoadinfo=get_my_taobao_url_by_kouling(messagetext)
            bot.send_group_msg(group_id=798301708, message=str(mytaobaoadinfo)) # 发送群消息
        elif whichone=='jd':
            myjdadinfo=get_myurl_by_adstring(messagetext)
            bot.send_group_msg(group_id=798301708, message=str(myjdadinfo)) # 发送群消息





scheduler = BlockingScheduler()
scheduler.add_job(task_name, 'interval', seconds=20)
scheduler.start()

'''
    

'''
@bot.on_message("group")

async def group(ctx):

    msgType =ctx["message"][0]["type"]

    print("msgType=="+msgType)

    pass
'''

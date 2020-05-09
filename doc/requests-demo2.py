# coding:utf-8
#!/usr/bin/python
from tasklist import baseClass
# import common
import commonFuc
import requests
import json

# import MyBrowser as browser
# import useragent as ua
# import msgextractor
import time
import datetime

# mongodb = common.mongoConnection()
# r = common.redisConnection()
# mysql = common.mysqlclient()

import threading
# import _thread
import os


from requests_html import HTMLSession
import random
import re
import urllib

def generate_url():
    # keywords_apiurl =' http://micropub.cdsb.com/api1/getWeiboCrawlConf'
    # keywordlist = json.loads(requests.get(keywords_apiurl).text)
    '''
        {
          "title": "成都突发",
          "keywords": "成都 预警,成都 发生 事件,成都 发生 枪击,成都 发生 车祸,成都 抢险,成都 发生 火灾,成都 发生 爆炸,成都 发生 泄露,成都 跳楼,成都 火灾,成都 车祸,成都 垮塌"
        },
        {
          "title": "政府",
          "keywords": "成都 新政,成都 市 工商局,成都 市 卫计委,成都 市 食药监局,成都 市委 市 政府,成都 市 质监,成都 市 协议,成都气象,成都发布,成都晚报"
        },
        {
          "title": "投诉",
          "keywords": "成都 投诉,成都 曝光,成都 赔偿,成都 起诉,成都 维权,成都 气愤,成都 陷阱,成都 爆料 扰民,成都 圈套,成都 爆料 骗,成都 黑幕,成都 官司"
        },
        {
          "title": "明星",
          "keywords": "成都 演唱会,成都 亮相,成都 现身,曝 出轨,恋情 曝,离婚 曝,分手 曝"
        },
        {
          "title": "热门视频",
          "keywords": "视频 成都,视频 惊险,视频 萌,视频 创意,视频 走红"
        },
        {
          "title": "旅游交通",
          "keywords": "成都旅游,成都交通,四川 公路 通,四川 景点 新,成都 景  开通"
        },
        {
          "title": "地震",
          "keywords": ""
        }

    '''

    '''
    新的
    {
      "title": "事件突发",
      "keywords": "跳楼,失联,死亡,事件,成都 抢险,袭击,爆炸,起火,发生 车祸,发生 火灾,发生 事件,垮塌,涉嫌,损毁,感染,案件,发生,垮塌,惊险"
    },
    {
      "title": "政府机构",
      "keywords": "新政,市 食药监局,违规 违纪,取消,宣布,市 协议,市委 市 政府,开幕,禁止,约谈,宣布"
    },
    {
      "title": "投诉举报",
      "keywords": "举报,投诉,抗议,起诉,拖欠,索赔,陷阱,维权,圈套,黑幕,爆料 骗"
    },
    {
      "title": "明星",
      "keywords": "曝 出轨,离婚 曝,恋情 曝,曝 出轨,恋情 曝,离婚 曝,分手 曝"
    },
    {
      "title": "社会",
      "keywords": "不正当,熊孩子,回应,反被,秒杀,警告,造假,上线,调查,致歉,遭到,涉嫌,声明,出炉,条款,亮相,进展,争议,引 热议,诈骗,创意"
    },
    {
      "title": "旅游交通",
      "keywords": "成都旅游,成都交通,四川 公路 通,四川 景点 新,成都 景  开通"
    },

    '''

    #经常用的报道词
    # 引 
    # 发生 
    # 曝

    keywordlist ={
        "server": [{
            "name": "weibo_crawl_server_101.37.39.65",
            "value": {
                "last_timestamp": 1528336725
            }
        }, {
            "name": "weibo_crawl_server_114.55.118.145",
            "value": {
                "last_timestamp": 1508228495
            }
        }, {
            "name": "weibo_crawl_server_114.55.149.19",
            "value": {
                "last_timestamp": 1531650255
            }
        }],
        "category": [
        {
          "title": "事件突发",
          # "keywords": "跳楼,失联,死亡,事件,抢险,袭击,爆炸,起火,发生 车祸,发生 事件,垮塌,涉嫌,损毁,感染,案件,发生,垮塌,惊险,被拘,失踪,事故,否认,猝死"
          #new
          "keywords": "跳楼,失联,死亡,事件,抢险,袭击,爆炸,起火,车祸,事件,垮塌,涉嫌,损毁,感染,案件,发生,垮塌,惊险,被拘,失踪,事故,否认,猝死,不 正当,熊孩子,回应,反被,警告,造假,上线,调查,致歉,遭到,涉嫌,声明,出炉,条款,进展,争议,热议,诈骗,创意,被拒,未成年,获刑,第一,咬伤,被罚,危险,奇特,遭,举报,投诉,抗议,起诉,索赔,陷阱,维权,黑幕,新政,违规,违纪,取消,宣布,市 协议,开幕,禁止,约谈,问责,出轨,离婚,恋情,分手"
          # "keywords": "跳楼,失联"
        },
        # {
        #   "title": "政府机构",
        #   "keywords": "新政,违规 违纪,取消,宣布,市 协议,开幕,禁止,约谈,问责"
        # },
        # {
        #   "title": "投诉举报",
        #   "keywords": "举报,投诉,抗议,起诉,索赔,陷阱,维权,黑幕"
        # },
        # {
        #   "title": "明星",
        #   "keywords": "曝 出轨,离婚 曝,恋情 曝,分手 曝"
        # },
        #秒杀,亮相,
        # {
        #   "title": "社会",
        #   "keywords": "不正当,熊孩子,回应,反被,警告,造假,上线,调查,致歉,遭到,涉嫌,声明,出炉,条款,进展,争议,引 热议,诈骗,创意,被拒,未成年,获刑,第一,咬伤,被罚,危险,奇特,遭"
        #   # "keywords": "不正当,熊孩子"
        # }

        ]
        
    }


    words = []

    for kw in keywordlist['category']:
      for kwd in kw['keywords'].split(','):
        if len(kwd) > 0 :
            words.append((kw['title'],kwd))

    random.shuffle(words)

    urllist = []
    catesets = set()

    count=1
    for cate,wd in words:
      keywd = urllib.parse.quote(wd, safe='/', encoding=None, errors=None)
      # 'Refer=g'
      # Refer=index
      # Refer=SWeibo_box


      today = datetime.datetime.today()
      mmnb= '0'+str(today.month) if len(str(today.month))<2 else today.month
      ddnb= '0'+str(today.day) if len(str(today.day))<2 else today.day
      tdzero='{}-{}-{}-0'.format(today.year,mmnb,ddnb)
      tdend=''
      pamlist=[]
      pamlist.append('q='+keywd)
      pamlist.append('xsort=hot')
      pamlist.append('timescope=custom:'+tdzero+':'+tdend)
      pamlist.extend(random.sample(['suball=1','vip=1','Refer=index','display=0','retcode=6102','scope=ori'],3))
      
      paramstring = '&'.join(pamlist)
      url = 'http://s.weibo.com/weibo?'+paramstring #Refer=index
      # url = 'http://s.weibo.com/weibo?q='+keywd+'&vip=1&Refer=index&display=0' #Refer=index
      print({'url':url,'cate':cate})
      urllist.append({'url':url,'cate':cate,'count':count})
      catesets.add(cate)
      count+=1

    random.shuffle(urllist)
    return urllist

def time_analyse(this_timestring):
    # analysetime = ''
    # '钟前' in this_timestring or '秒前' in this_timestring or '今天' in this_timestring 
    if '分钟前' in this_timestring:
        minite = int(this_timestring.replace('分钟前',''))
        now = datetime.datetime.now()
        delta = datetime.timedelta(minutes=-minite)
        minutesbefore = now + delta
        analysetime = minutesbefore
    elif '秒前' in this_timestring:
        second = int(this_timestring.replace('秒前',''))
        now = datetime.datetime.now()
        delta = datetime.timedelta(seconds=-second)
        secondbefore = now + delta
        analysetime = secondbefore
    elif '今天' in this_timestring:
        [hours,minutes] = this_timestring.replace('今天','').split(':')
        today = datetime.datetime.today()
        todayzero = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
        delta = datetime.timedelta(hours=int(hours),minutes=int(minutes))
        todaytime = todayzero + delta
        analysetime = todaytime
    if '刚刚' in this_timestring:
        now = datetime.datetime.now()
        analysetime = now
    return analysetime.strftime('%Y-%m-%d %H:%M:%S')
    # return analysetime
def randomstring(num):
    return ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba0123456789',num))
def randomnumber(num):
    return ''.join(random.sample('01234567890123456789012345678901234567890123456789',num))
def randomua():
    ualist = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36','Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1']
    return random.choice(ualist)
#微博唯一ID
def getwbunikey(this_link):
    
    if this_link != 'unknown':
        # urlstruct=this_link.split('/')
        # wbid=urlstruct[2].split('?')[0]
        # wb_key = urlstruct[1]+wbid
        # wbid=urlstruct[2].split('?')[0]

        #new key
        try:
            urlstruct=this_link.split('?')
            wb_key_=urlstruct[0]
            wb_key = wb_key_.split('/')[2]

        except Exception as e:
            # raise e
            wb_key = None
    else:
        wb_key = None
    return wb_key
def getwbuserId(this_link):
    
    if this_link != 'unknown':
        # urlstruct=this_link.split('/')
        # wbid=urlstruct[2].split('?')[0]
        # wb_key = urlstruct[1]+wbid
        # wbid=urlstruct[2].split('?')[0]

        #new key
        try:
            urlstruct=this_link.split('?')
            wb_key_=urlstruct[0]
            wb_key = wb_key_.split('/')[1]

        except Exception as e:
            # raise e
            wb_key = None
    else:
        wb_key = None
    return wb_key

#自定义 哪一个网站   tanzi还是micropub
class articleUp(baseClass.iTask):

    def __init__(self,dataBaseConfig):
        super(articleUp,self).__init__(dataBaseConfig)
        # 任务类型 free count fetch
        self.taskType = 'free'
        self.taskName = 'robottest'

        # self.headers,self.proxies,self.browser = self.genBrowserInfo()

        # self.redis = dataBaseConfig['redis']
        # self.db = dataBaseConfig['mongodb']
        self.mysql = dataBaseConfig['mysql']
        self.weibo_url_list = generate_url()

        self.browser = HTMLSession()

    # def genBrowserInfo(self):
    #     ua = 'Mozilla/5 .0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'#
    #     # ua = randomua()
    #     headers = {
    #         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #         'Accept-encoding': 'gzip, deflate, br',
    #         'Accept-language': 'zh-CN,zh;q=0.9',
    #         'Connection': 'keep-alive',
    #         # 'Cache-Control':' max-age=0',
    #         'Cookie': 'SINAGLOBAL=7'+randomnumber(10)+'51.894.156'+randomnumber(5)+'88833; SCF='+randomstring(6)+'-'+randomstring(14)+'-'+randomstring(7)+'-'+randomstring(12)+'_'+randomstring(29)+'-'+randomstring(14)+'.; SUHB='+randomstring(10)+'_mNL; ALF=159'+randomnumber(7)+'; _s_tentry=login.sina.com.cn; Apache='+randomnumber(13)+'.571.15689'+randomnumber(13)+'; ULV=15689'+randomnumber(13)+':3:1:1:'+randomnumber(13)+'.571.1568'+randomnumber(13)+':15668'+randomnumber(13)+'; SUB=_2Ak'+randomstring(13)+'oRz2_ka'+randomstring(13)+'l-yT'+randomstring(13)+'M-v'+randomstring(9)+'tI_'+randomstring(13)+'; SUBP=00'+randomstring(13)+'-Ws9jqgMF5'+randomstring(13)+'W'+randomstring(13)+'; WBtopGlobal_register_version=307744aa77dd5677; UOR=,,www.techweb.com.cn; login_sid_t='+randomstring(15)+'895'+randomstring(7)+'07; cross_origin_proto=SSL',
    #         # 'upgrade-insecure-requests':1,
    #         # 'Referer':,
    #         'Host':'s.weibo.com',
    #         'User-Agent': ua,
    #     }

    #     # 代理服务器
    #     proxyHost = "http-pro.abuyun.com"
    #     proxyPort = "9010"

    #     # self.prxxy('http-pro.abuyun.com','9010','H99BF0149RU3K52P','5BE76E4D56AB0010')
    #     # 代理隧道验证信息
    #     proxyUser = "H99BF0149RU3K52P"
    #     proxyPass = "5BE76E4D56AB0010"

    #     proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    #       "host" : proxyHost,
    #       "port" : proxyPort,
    #       "user" : proxyUser,
    #       "pass" : proxyPass,
    #     }

    #     proxies = {
    #         "http"  : proxyMeta,
    #         # "https" : proxyMeta,
    #     }

    #     session = HTMLSession()

    #     return headers,proxies,session

    def task(self):
        pass
        print('get weibo')
        # os.popen("python3 /var/www/cdsb/taskRunner/weibokmeans/new/kmeans.py")
        # print(len(self.datashare['urllist']))
        # return ''

        # todaynowtime = datetime.datetime.now()

        # if 6<=todaynowtime.hour  or todaynowtime.hour<=1:
        #     print('ok , start crawl')
        # else:
        #     print('no , stop crawl')
            

            # 以免晚上不抓,数据历史会出问题
            # os.system("python3 /var/www/cdsb/taskRunner/weibokmeans/new/kmeans.py ")
            # os.system("python3  /var/www/cdsb/taskRunner/weibokmeans/dbscan/run.py ")


            # if todaynowtime.hour ==5 and todaynowtime.minite>30:
            #     # os.system('sudo rm /var/www/cdsb/taskRunner/weibo.json')
            #     # os.system("echo '' > /var/www/cdsb/taskRunner/weibo.json")
            #     pass

            # return False

        # print(len(self.datashare['urllist']))
        # urlobj = self.datashare['urllist'].pop()
        # urlstring = urlobj['url']

        #理想状态 每次请求IP都换
        # for urlobj in self.datashare['urllist']:
        #     # print(urlobj)
        #     cate = urlobj['cate']
        #     urlstring = urlobj['url']
        #     # print(urlstring)
        #     # 多线程需要同时代理多个IP，每次访问IP都不一样,
        #     _thread.start_new_thread(print_time, ("Thread",urlstring))
        #     # threading.Thread(target=print_time,args=("Thread",urlstring))
        #     time.sleep(1)




        failedurl = [];

        
        
        # 一分钟内IP都一样  但是同时只有一个抓取在工作
        # try:
        #     with open('/var/www/cdsb/taskRunner/weibo.json','r') as rd:
        #         # dataraw = json.load(rd)
        #         dataraw = {'news':[]}
        # except Exception as e:
        #     dataraw = {'news':[]}
        
        # jsondataset = {'news':[]}  


        # # 微博保存dict,记录是否已经抓取过
        # wb_dict={}
        # daset = {}
        
        # #导入今天所有抓取的微博
        # if len(dataraw['news'])>0:
        #     for newsitem in dataraw['news']:
        #         daset[newsitem['name']]=newsitem
        #         wb_dict[newsitem['name']]={}
        #         for weiboobj in newsitem['list']:
        #             _wbkey = getwbunikey(weiboobj['link'])
        #             if _wbkey==None:
        #                 wb_dict[newsitem['name']][weiboobj['link']]=weiboobj
        #             else:
        #                 wb_dict[newsitem['name']][_wbkey]=weiboobj
        # else:
        #     for caname in self.datashare['catesets']:
        #         daset[caname]={'name':caname,'list':[]}
        #         wb_dict[caname]={}
        


        conn = self.mysql.connection()
        



        cc = 1
        # [0:-1]
        for urlobj in self.weibo_url_list:
            print(urlobj)
            cate = urlobj['cate']
            urlstring = urlobj['url']
            countnum = urlobj['count']


            # # 要访问的目标页面
            # targetUrl = "http://test.abuyun.com"
            # #targetUrl = "http://proxy.abuyun.com/switch-ip"
            # #targetUrl = "http://proxy.abuyun.com/current-ip"


            # 测试函数
            #{"ip":"123.4.231.114","locale":""}
            # urlstring = 'http://test.abuyun.com'
            proxy = {'http':'http://H99BF0149RU3K52P:5BE76E4D56AB0010@http-pro.abuyun.com:9010'}



            # ua = 'Mozilla/5 .0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'#
            ua = randomua()
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-encoding': 'gzip, deflate, br',
                'Accept-language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                # 'Cache-Control':' max-age=0',
                'Cookie': 'SINAGLOBAL=7'+randomnumber(10)+'51.894.156'+randomnumber(5)+'88833; SCF='+randomstring(6)+'-'+randomstring(14)+'-'+randomstring(7)+'-'+randomstring(12)+'_'+randomstring(29)+'-'+randomstring(14)+'.; SUHB='+randomstring(10)+'_mNL; ALF=159'+randomnumber(7)+'; _s_tentry=login.sina.com.cn; Apache='+randomnumber(13)+'.571.15689'+randomnumber(13)+'; ULV=15689'+randomnumber(13)+':3:1:1:'+randomnumber(13)+'.571.1568'+randomnumber(13)+':15668'+randomnumber(13)+'; SUB=_2Ak'+randomstring(13)+'oRz2_ka'+randomstring(13)+'l-yT'+randomstring(13)+'M-v'+randomstring(9)+'tI_'+randomstring(13)+'; SUBP=00'+randomstring(13)+'-Ws9jqgMF5'+randomstring(13)+'W'+randomstring(13)+'; WBtopGlobal_register_version=307744aa77dd5677; UOR=,,www.techweb.com.cn; login_sid_t='+randomstring(15)+'895'+randomstring(7)+'07; cross_origin_proto=SSL',
                # 'upgrade-insecure-requests':1,
                # 'Referer':,
                'Host':'s.weibo.com',
                'User-Agent': ua,
            }

            try:
                page = self.browser.get(url=urlstring,proxies=proxy,headers=headers)
                print(page.text)
            except Exception as e:
                failedurl.append(urlstring)
                continue
            
            # exit()

            
            # page = self.browser.get(urlstring,headers=self.headers,proxies=self.proxies)
            # # titlediv =  page.html.find('title', first=True)
            # alist =  page.html.find('a')
            # for a in alist:
            #   print(''.join(a.text))
            #   print(a.attrs['href'])
            # # print(titlediv.text)
            # print(page.html.text)
            # time.sleep(3)
            # # useragent=ua.ua(False)
            # continue

            # try:
            #     # page = self.browser.get(urlstring,headers=self.headers,proxies=self.proxies)
            #     page = self.browser.request(urlstring)
            # except Exception as e:
            #     # raise e
            #     print('changing ip ...')
            #     self.headers,self.proxies,self.browser = self.genBrowserInfo()
            #     time.sleep(5)
            #     page = self.browser.get(urlstring,headers=self.headers,proxies=self.proxies)

            # # print(len(self.datashare['urllist']))


            # print(page)
            # print(page.text)
            # print(page.html)
            print(page.status_code)
            weibolist =  page.html.find('.m-main .m-wrap .card-wrap .card')
            # print(len(weibolist))
            

            # print(len(self.datashare['urllist']))


            for w in weibolist:
                # print(w.text)
                try:
                    this_timestring  = w.find('.content .from a', first=True).text
                except Exception as e:
                    # print(str(e))
                    
                    print('**************************cant get time string*********************************')
                    continue

                if '钟前' in this_timestring or '秒前' in this_timestring or '今天' in this_timestring :
                    pass
                else:
                    # print('not today')
                    continue

                try:
                    this_author = w.find('a.name', first=True).text
                except Exception as e:
                    this_author = 'unknown'

                try:
                    this_weibo = w.find('p.txt', first=True).text

                    this_weibo= re.sub(r'[\U00010000-\U0010ffff]', '',this_weibo)
                    this_weibo = re.sub(r'[\"\']', '',this_weibo)

                except Exception as e:
                    this_weibo = 'unknown'
                    # print(e)

                try:
                    this_level = w.find('.info div a[title]', first=True).text
                except Exception as e:
                    this_level = 'unknown'

                statelist=w.find('.card-act ul li')
                collect = statelist[0].find('a', first=True).text.replace('收藏','').replace(' ','')
                shares = statelist[1].find('a', first=True).text.replace('转发','').replace(' ','')
                comments = statelist[2].find('a', first=True).text.replace('评论','').replace(' ','')
                likes = statelist[3].find('a', first=True).text


                try:
                    this_shares = 0 if shares=='' else shares
                except Exception as e:
                    this_shares = 0

                try:
                    this_comments = 0 if comments == ''  else comments
                except Exception as e:
                    this_comments = 0

                try:
                    this_likes = 0 if likes=='' else likes
                except Exception as e:
                    this_likes = 0

                #

                try:
                    this_time = time_analyse(this_timestring)
                    # 时间戳
                    this_time = commonFuc.timeStamp(this_time)
                except Exception as e:
                    this_time = time.time()
                    # print(e)

                try:
                    this_link =  w.find('.from a', first=True).attrs['href'].replace('//','')
                except Exception as e:
                    this_link = 'unknown'

                #微博唯一ID
                wb_key = getwbunikey(this_link)
                wb_user_id = getwbuserId(this_link)


                imgsrc = 'unknown'
                imgsrclist = w.find('.content img')
                for ximg in imgsrclist:
                    xsrc = ximg.attrs['src']
                    if 'miaopai' in xsrc:
                        imgsrc = xsrc
                    if 'sinaimg' in xsrc:
                        imgsrc = xsrc
                        continue
                    else:
                        imgsrc = xsrc
                if '[{' in imgsrc:
                    imgsrc='unknown'
                # print(this_author)
                # print(this_level) #innerHTML #.get_attribute('title')
                # print(this_weibo)
                # print(this_time)
                # print(this_link)
                # print(imgsrc)
                # print(this_shares)
                # print(this_comments)
                # print(this_likes)

                # print('\n')

                weibo = {
                            'cate':cate,
                            'author':this_author,
                            'text':this_weibo,
                            'posttime':str(this_time),
                            'link':this_link,
                            'level':this_level,
                            'shares':int(this_shares),
                            'comments':int(this_comments),
                            'likes':int(this_likes),
                            'img':imgsrc.replace('//','')
                            }


                # 保存在dict中,再生成list?
                print(wb_key)
                # if wb_key==None:
                #     wb_dict[cate][this_link]=weibo
                # else:
                #     wb_dict[cate][wb_key]=weibo

                # mysql
                if wb_key!=None:
                    #save mysql
                    try:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO clue_list (id,weiboid,bigvid,weibo_url,org,ptime,content,ref_content,image,video,inner_share,inner_comment,inner_likeit,outer_share,outer_comment,outer_likeit,status) VALUES (NULL,'"+str(wb_key)+"','"+wb_user_id+"','"+weibo['link']+"','"+weibo['author']+"',"+weibo['posttime']+",'"+weibo['text']+"','','"+weibo['img']+"','"+weibo['img']+"',0,0,0,"+str(weibo['shares'])+","+str(weibo['comments'])+","+str(weibo['likes'])+",1)")
                        conn.commit()
                        cursor.close()

                    except Exception as e:
                        # raise e
                        # print(str(e))
                        try:
                            pass
                            #update
                            cursor = conn.cursor()
                            cursor.execute("UPDATE clue_list SET outer_share="+str(weibo['shares'])+", outer_comment="+str(weibo['comments'])+", outer_likeit="+str(weibo['likes'])+",  where weiboid = "+str(wb_key))
                            conn.commit()
                            cursor.close()

                        except Exception as ee:
                            # raise ee
                            print(str(e))
                            pass
                        
                    

            # for wbk in wb_dict[cate]:
            #     daset[cate]['list'].append(wb_dict[cate][wbk])

            # wb_dict[cate]={}
            time.sleep(7)   # 5+3 = 8 秒一个URL,15分钟,有8分钟是计算,7分钟抓取
            # mybrowser.quit()

            # print(urlstring)
            
        # for caname in daset:
        #     jsondataset['news'].append(daset[caname])

        # # print(jsondataset)
        # with open('/var/www/cdsb/taskRunner/weibo.json','w') as w:
        #     json.dump(jsondataset,w)




        # conn = self.mysql.connection()
        # cursor = conn.cursor()

        # for cate in jsondataset['news']:
        #     # if cate['name'] != catename:
        #     #     continue
        #     # else:
        #     #     print(catename)
        #     weibolist=cate['list']
        #     # print(len(weibolist))
        #     for weibo in weibolist:
        #         weibo['text'] = re.sub(r'[\U00010000-\U0010ffff]', '',weibo['text'])
        #         weibo['text'] = re.sub(r'[\"\']', '',weibo['text'])
        #         # text_seg = segment_sentence(weibo['text'])
        #         # if text_seg == '':
        #         #     continue
        #         # weibo['segment'] = text_seg
        #         # weibo['origintext'] = weibo['text']
        #         # 测试用
        #         # weibo['text'] = text_seg
        #         # corpus_weibo.append(weibo)
        #         cursor.execute("INSERT INTO topics (id,link,org,ptime,content,image,video,share,comment,likeit,status) VALUES (NULL,'"+weibo['link']+"','"+weibo['author']+"',"+weibo['posttime']+",'"+weibo['text']+"','"+weibo['img']+"',"+weibo['img']+","+str(weibo['shares'])+","+str(weibo['comments'])+","+str(weibo['likes'])+",1)")

        # self.mysql
        # conn = self.mysql.connection()
        # cursor = conn.cursor()
        # cursor.execute("")
        # cursor.close()
        # conn.close()

        # cursor.close()
        conn.close()

        #失败的url
        print(failedurl)
        print('failed url number: {}'.format(len(failedurl)))
        print('this time over')

        # print('start autukmeans')
        # os.system("python3 /var/www/cdsb/taskRunner/weibokmeans/onetime/autokmeans.py ")
        # os.system("python3 /var/www/cdsb/taskRunner/weibokmeans/cloop/cloop.py ")
        # os.system("python3 /var/www/cdsb/taskRunner/weibokmeans/bowkmeans/kmeansbow.py ")
        with open('/var/log/weibocrawl.log','a+') as f:
            localtimestr = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
            f.write(localtimestr+'\n')

        #os.system("python3 /var/www/cdsb/taskRunner/weibokmeans/new/kmeans.py ")
        # os.system("python3  /var/www/cdsb/taskRunner/weibokmeans/dbscan/run.py ")


                  
            



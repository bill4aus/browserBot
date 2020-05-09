import random
from requests_html import HTML
import re

def randomstring(num):
    return ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba0123456789',num))
def randomnumber(num):
    return ''.join(random.sample('01234567890123456789012345678901234567890123456789',num))
def randomua():
    ualist = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36','Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1']
    return random.choice(ualist)




def headerGen(ua,host,reffer):
	if ua ==None:
		ua = randomua()
	testHeader ={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
			'Accept-encoding': 'gzip, deflate',
			'Accept-language': 'zh-CN,zh;q=0.9',
			'Connection': 'keep-alive',
			'Cache-Control':' max-age=0',
			# 'Cookie': 'SINAGLOBAL=7'+randomnumber(10)+'51.894.156'+randomnumber(5)+'88833; SCF='+randomstring(6)+'-'+randomstring(14)+'-'+randomstring(7)+'-'+randomstring(12)+'_'+randomstring(29)+'-'+randomstring(14)+'.; SUHB='+randomstring(10)+'_mNL; ALF=159'+randomnumber(7)+'; _s_tentry=login.sina.com.cn; Apache='+randomnumber(13)+'.571.15689'+randomnumber(13)+'; ULV=15689'+randomnumber(13)+':3:1:1:'+randomnumber(13)+'.571.1568'+randomnumber(13)+':15668'+randomnumber(13)+'; SUB=_2Ak'+randomstring(13)+'oRz2_ka'+randomstring(13)+'l-yT'+randomstring(13)+'M-v'+randomstring(9)+'tI_'+randomstring(13)+'; SUBP=00'+randomstring(13)+'-Ws9jqgMF5'+randomstring(13)+'W'+randomstring(13)+'; WBtopGlobal_register_version=307744aa77dd5677; UOR=,,www.techweb.com.cn; login_sid_t='+randomstring(15)+'895'+randomstring(7)+'07; cross_origin_proto=SSL',
			# 'upgrade-insecure-requests':1,
			'Referer':reffer,
			'Host':host,
			'User-Agent': ua,
	}


def pageUrlGen(url_prefix,url_endwith,starttimecount=1,everytimepages=200):

	purllist = []
	starcount =starttimecount

	startpagenumber = (starcount-1)*everytimepages
	endpagenumber = startpagenumber+everytimepages
	pagenumberlist = range(startpagenumber,endpagenumber)
	for pgnumber in pagenumberlist:

		turl = url_prefix+str(pgnumber)+url_endwith
		purllist.append(turl)
	return purllist


def htmlReplace(htmlstring,zzrule,retarget):
	if zzrule ==None:
		zzrule=r'<(.*?)>'
	doc  = re.sub(zzrule, retarget,str(htmlstring))
	mhtml = HTML(html=doc)
	return mhtml
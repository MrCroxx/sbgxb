# -*- coding:utf-8 -*-

import urllib
import urllib2
import datetime

'''
# post_blog 提交博客
params:
	vtoken : 登陆后返回的vtoken
	cookie : 登陆后返回的cookie
	blog_title : 博客标题
	blog_body : 博客内容

returns:
	code : 状态代码 B06001博文发表成功 B07005操作太频繁 更多详见 http://blog.csdn.net/zfrong/article/details/6147566

example usage:

# 这个token和cookie是假的 大家替换成自己的

# from sina_post import post_blog

# vtoken="YOUR VTOKEN"
# cookie = "YOUR COOKIE"
# blog_title="哈哈哈哈"
# blog_body="嘿嘿嘿嘿"
# post_blog(vtoken,cookie,blog_title,blog_body)

'''

def post_blog(vtoken,cookie,blog_title,blog_body):
	url = 'http://control.blog.sina.com.cn/admin/article/article_post.php'

	date_pub = datetime.datetime.now().strftime("%Y-%m-%d")
	time = datetime.datetime.now().strftime("%X")
	
	conlen=len(blog_body)


	'''Content-Length:619'''
	headers = {
		
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",

	"Content-Type":"application/x-www-form-urlencoded",
	"Cookie":cookie,
	"Host":"control.blog.sina.com.cn",
	"Origin":"http://control.blog.sina.com.cn",
	"Referer":"http://control.blog.sina.com.cn/admin/article/article_add.php",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",

	}

	values = {
		
		"ptype":"",
		"teams":"",
		"worldcuptags":"",
		"album":"",
		"albun_cite":"",
		"blog_id":"",
		"is_album":"",
		"old365":"0",
		"stag":"",
		"sno":"",
		"book_worksid":"",
		"channel_id":"",
		"url":"",
		"channel":"",
		"newsid":"",
		"fromuid":"",
		"wid":"",
		"articletj":"",
		"vtoken": vtoken,
		"is_media":"0",
		"is_stock":"0",
		"is_tpl":"0",
		"assoc_article":"",
		"assoc_style":"0",
		"assoc_article_data":"",
		"article_BGM":"",
		"xRankStatus":"",
		"commentGlobalSwitch" : "",
		"commenthideGlobalSwitch" : "",
		"articleStatus_preview" : "1",
		"source" : "",
		"topic_id" : "0",
		"topic_channel" : "0",
		"topic_more" : "",
		"utf8" : "1",
		"conlen" : conlen,
		"date_pub" : date_pub,
		"time" :time,
		"new_time" : "",
		"isTimed" : "0",
		"immediatepub" : "0",
		"blog_title" : blog_title,
		"blog_body" : blog_body,
		"blog_class" : "00",
		"tag" : "",
		"x_cms_flag" : "0",
		"sina_sort_id" : "117",

	}

	data = urllib.urlencode(values)

	print data

	req = urllib2.Request(url,data,headers)
	res = urllib2.urlopen(req)

	print res.read()

# vtoken="3ba8ff6a1e464032b1fa9eabbdaa26e2"
# cookie = "EditorToolType=base; SINAGLOBAL=106.39.41.170_1496504418.867980; UOR=www.baidu.com,www.sina.com.cn,; SGUID=1496648001029_78295224; SCF=AouQMZqfLW3ISxVaCaucj0izlJP1kzjsg3SJG7h-3njTsAijR66WrZC3K5DaOO3CxCgzyNrXCRuiKxh-Fg0vMn4.; sso_info=v02m6alo5qztYOcpr24noKVhY2SlLiNkpS4joKVhY2ylLmNgpS5kaKZtZqWkL2No4i2jpOguIyjmLiMsMDA; U_TRS1=000000ea.e295473b.593579d3.48749d72; _s_loginStatus=6269882683; Apache=106.39.41.170_1496764699.87464; ULV=1496764699819:4:4:4:106.39.41.170_1496764699.87464:1496764699136; U_TRS2=000000aa.8d3511ed.5936d11e.19c257d6; ALF=1528300704; SUB=_2A250MqFwDeRhGeBM7VsZ-CzKwz-IHXVXSZW4rDV_PUJbm9BeLWfkkW8SUnsmGifzjY-R-9lsij7VszoQpA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhEIYOO8yZxjor5Wjdi_OFg5NHD95Qceoq41hnESon0Ws4DqcjPBNiawGnLxK-L1h-L1hnLxKML1KBL1-qt; SessionID=dlmlk9l8ue9sdt3eb2bkihsrr0; SINABLOGNUINFO=6269882683.175b6d13b.0; _s_loginuid=6269882683; lxlrttp=1496631457; rotatecount=7; BLOG_TITLE=Croxx%E5%85%88%E7%94%9F%E7%9A%84%E5%8D%9A%E5%AE%A2"
# blog_title="哈哈哈哈"
# blog_body="嘿嘿嘿嘿"

# post_blog(vtoken,cookie,blog_title,blog_body)

def view_blog():


	url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=175b6d13b0102xykg&ref=http%3A%2F%2Fblog.sina.com.cn%2Fs%2Farticlelist_6269882683_0_1.html&varname=requestId_58884373'

	headers = {
			
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",

		"Content-Type":"application/x-www-form-urlencoded",
		"Cookie":'',
		"Host":"control.blog.sina.com.cn",
		"Origin":"http://control.blog.sina.com.cn",
		"Referer":"http://control.blog.sina.com.cn/admin/article/article_add.php",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",

		}

	req = urllib2.Request(url,headers=headers)
	res = urllib2.urlopen(req)

	print res.read()

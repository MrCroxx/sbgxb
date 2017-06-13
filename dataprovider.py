# -*- coding:utf-8 -*-

from sina_post import post_blog,view_blog
import time
import json
import datetime

vtoken="3ba8ff6a1e464032b1fa9eabbdaa26e2"
cookie = 'EditorToolType=base; _s_loginuid=6269882683; SINAGLOBAL=106.39.41.170_1496504418.867980; UOR=www.baidu.com,www.sina.com.cn,; SGUID=1496648001029_78295224; SCF=AouQMZqfLW3ISxVaCaucj0izlJP1kzjsg3SJG7h-3njTsAijR66WrZC3K5DaOO3CxCgzyNrXCRuiKxh-Fg0vMn4.; U_TRS1=000000ea.e295473b.593579d3.48749d72; lxlrtst=1496805761_o; _s_loginStatus=6269882683; lxlrttp=1496894899; BLOGUSERNNNNAME=undefined; LiRe=true; onceloggedonblog=1497196800000; sso_info=v02m6alo5qztYOcpr24noKVhY2SlLiNkpS4joKVhY2ylLmNgpS5kaKZtZqWkL2No4i2jpOguIyjmLiMsMDA; U_TRS2=00000092.8e446d7c.593e2c17.5013acdf; SUB=_2A250OlxIDeRhGeBM7VsZ-CzKwz-IHXVXTsqArDV_PUNbm9BeLUX4kW8iv2cstqS1FKMkjddE94Mod_6ISA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhEIYOO8yZxjor5Wjdi_OFg5NHD95Qceoq41hnESon0Ws4DqcjPBNiawGnLxK-L1h-L1hnLxKML1KBL1-qt; ALF=1528782744; SessionID=14na9vk85ciqm1oa1ku67kguc1; IDC_LOGIN=BJ%3A1497246744; SINABLOGNUINFO=6269882683.175b6d13b.; rotatecount=1; Apache=106.39.41.146_1497246745.544294; BLOG_TITLE=Croxx%E5%85%88%E7%94%9F%E7%9A%84%E5%8D%9A%E5%AE%A2; ULV=1497246746448:24:24:8:106.39.41.146_1497246745.544294:1497246742582'

# blog_title="哈哈哈哈"
# blog_body="嘿嘿嘿嘿"

# post_blog(vtoken,cookie,blog_title,blog_body)

f = open('chinadaily.json','r+')

news = json.load(f)

offset = input("Please input offset (from 0):")

global num

num = offset

for item in news[offset:]:
	
	#global num

	try:

		num += 1

		view_blog()

		title = '佳作分享 -- ChinaDaily新闻选 ： '
		for t in item['title']:
			title += str(t)
		content = ''

		content += title + '<br/>' 

		for i in item['info']:
			content += str(i) + '<br/>'

		for c in item['content']:
			content += str(c) + '<br/>'

		print title
		print content
		#content = item['title'][0]+'<br/>'+item['info'][0]+'<br/>'+item['content'][0]
		post_blog(vtoken, cookie, title, content)

		#num += 1

		print "****************************************"
		print "                 Submit                 "
		print "                 "+str(num-1)+"                 "
		print "****************************************"
		for i in range(15):
			time.sleep(60)
			print datetime.datetime.now()

	except Exception,e:
		print "****************************************"
		print "                  Error                 "
		print "                 "+str(num-1)+"                 "
		print "****************************************"
		continue

# http://blog.sina.com.cn/s/blog_175b6d13b0102xykg.html

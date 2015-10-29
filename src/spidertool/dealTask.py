#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
import SQLTool
from lxml import etree as etree
from lxml.html import fromstring
import lxml.html
import lxml.html.soupparser
try:
	from bs4 import UnicodeDammit             # BeautifulSoup 4

	def decode_html(html_string):
		converted = UnicodeDammit(html_string)
		if not converted.unicode_markup:
			raise UnicodeDecodeError("Failed to detect encoding, tried [%s]",', '.join(converted.tried_encodings))
# print converted.original_encoding
		return converted.unicode_markup

except ImportError:
	from BeautifulSoup import UnicodeDammit   # BeautifulSoup 3

	def decode_html(html_string):
		converted = UnicodeDammit(html_string, isHTML=True)
		if not converted.unicode:
			raise UnicodeDecodeError("Failed to detect encoding, tried [%s]",', '.join(converted.triedEncodings))
# print converted.originalEncoding
		return converted.unicode
	
	
class dealTask(TaskTool):
	##处理任务类，通过将爬虫爬回来的网页信息进行进一步的处理
	def __init__(self):
		TaskTool.__init__(self)

		self.connectpool=connectpool.ConnectPool()

	def task(self,req,threadname):
		print threadname+'执行任务中'+str(datetime.datetime.now())
		ans = self.makesqlit(req[1])

		print threadname+'任务结束'+str(datetime.datetime.now())
		return ans

	def makesqlit(self,content):
		
		try:
			dom = lxml.html.fromstring(decode_html(content))
			ignore = lxml.html.tostring(dom, encoding='unicode')
		except UnicodeDecodeError:
			dom = lxml.html.soupparser.fromstring(content)
	#	page = etree.HTML(content)
		print dom[1].tag
		
#		print page[1].tag
		return content
if __name__ == "__main__":
	"""
	DealSQL=SQLTool.DBmanager()
	DealSQL.connectdb()
	(result,title,count,col)=DealSQL.searchtableinfo_byparams(['webdata'],['address','content','meettime'])
	DealSQL.closedb()
	#TODO 添加元组进去
	#ｕｒｌ也要存进去
	f = dealTask()
	f.set_deal_num(10)


	for data in result:
		f.add_work([(data[0],data[1])])
#		print data[1]

	f.start_task()
	while f.has_work_left():
		v,ans=f.get_finish_work()
		print ans
	while True:
		pass

	"""

	try:
		file_object = open('test.html')
		content = file_object.read( )
		file_object.close( )
	except Exception,e:
		print e
	TOOL=dealTask()
	TOOL.makesqlit(content)





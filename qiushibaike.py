# -*- coding: utf-8 -*-  
from pyquery import PyQuery as pq
import requests
import random
import re

'''user_agents = [
					'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
					'Opera/9.25 (Windows NT 5.1; U; en)',
					'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
					'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
					'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
					'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
					'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
					'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 '
			   ] 
agent = random.choice(user_agents)
webheaders = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Host':'Host:www.qiushibaike.com',
	'User-Agent':agent
}'''
webheaders = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
pageId = 1
while pageId <= 35:
	weburl = 'http://www.qiushibaike.com/text/page/' + str(pageId)
	pageId += 1
	
	webpage = requests.get(url = weburl, headers = webheaders).content.decode()

	pattern = '<div.*?class="content">.*?<span>(.*?)</span>.*?</div>'
	items = re.findall(pattern, webpage, re.S)
	#webpage = urllib.request.urlopen(req)
	#html = webpage.content
	with open('qiushi.txt','a') as f:
		for item in items:
			#item.replace('<br/>', '\r\n')
			f.write(item.replace('<br/>', '\r\n') + '\r\n\r\n')

	#d=pq(filename="D:\PythonWorkplace\load\movie.txt")
		
		'''d= pq(webpage)
		#con = d('#content').html()
		con = d('.main').html()
		#print(con)
		c = pq(con)
		#text = d('.article block untagged mb15').html()
		#print(text)
		for data in c('.content'):
			#print(data, file = f)
			#print('第'+ pageId-1 + '页', '作者：'+ data.find('.title').text(), '赞数'+data.find('stats-vote').find('i').text(), '评论'+data.find('stats-comments').find('i').text(), file = f)
			#print('赞数'+data.find('stats-vote').find('i').text(), '评论'+data.find('stats-comments').find('i').text(), file = f)
			print(data, file = f)
			print(file = f)'''


'''
import re
from urllib.request import *

class Spider:
	def __init__(self):
		self.page = 1
		# 记录访问的页码
		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
		# 伪装浏览器君
		self.headers = {'User-Agent': self.user_agent}
		self.stories = []
		# 存储段子
		self.enable = False

	def get_stories(self):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
			request = Request(url, headers = self.headers)
			# 构建request
			self.page += 1
			# 翻页
			response = urlopen(request)
			content = response.read().decode("UTF-8")
			pattern = re.compile('alt="(.*?)".*?"content">\n(.*?)\n</div>(.*?)<div class="stats".*?"number">(.*?).*?"numbers">(.*?)</i>', re.S)
			# 作者，内容，可能存在的图片信息，赞数，评论
			self.stories = re.findall(pattern, content)
			# 正则表达式匹配
			
		except URLError as e:
			if hasattr(e, "reason"):
				print ("获取失败，错误原因", e.reason) 
				# 错误信息
				return None

	def start(self):
		print ("{:^70}".format('正在读取糗事百科'))
		self.enable = True
		while self.enable:
			self.get_stories()
			# 获取一页段子
			for story in self.stories:
				# 遍历段子
				if not re.search('img', story[2]):
				# 去除带图段子
					Input = input("{:^70}".format('回车查看新段子, Q 键退出程序\n'))
					# 用户键入
					if Input is 'Q' or Input is 'q':
						print ("{:^70}".format('再见'))
						return
					print ('{:^70}'.format('第{}页 作者:{} 赞数{} 评论{}').format(self.page-1, story[0], story[3], story[4]))
					print ('{}\n'.format(story[1]))
			print ("{:^70}".format('翻个页 TwT'))
spider = Spider()
spider.start()
'''


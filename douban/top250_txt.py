#-*-coding:utf-8-*-
from pyquery import PyQuery as pq
import urllib.request

webheaders = {
	'Host':'Host:movie.douban.com',
	'User-Agent':'Mozilla/5.0'
}
pageId = 0
while pageId <= 225:
	weburl = 'https://movie.douban.com/top250?start=' + str(pageId)
	pageId += 25

	req = urllib.request.Request(url = weburl, headers = webheaders)
	#webpage = urllib.request.urlopen(req).read()
	with open('D:\PythonWorkplace\load\movie.txt','a', encoding = 'utf-8') as f:
		#html.write(webpage)

	#d=pq(filename="D:\PythonWorkplace\load\movie.txt")
		
		d= pq(url = weburl)
		for data in d('ol').items('li'):
	 		print(data.find('.hd').find('.title').eq(0).text(), data.find('.star').find('.rating_num').text(), file = f)
	 		#print(data.find('.star').find('.rating_num').text(), file = f)
	 		print(data.find('.quote').find('.inq').text(), file = f)
	 		print(file = f)
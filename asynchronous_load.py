#-*-coding:utf-8-*-
import re
import requests
import json
'''import gzip
from io import StringIO'''

url = 'http://www.qdaily.com/categories/17'
url_more = 'http://www.qdaily.com/categories/categorymore/17/'
webheader = {
	'Connection': 'Keep-Alive',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}
data = requests.get(url).content
html = data.decode('UTF-8')
last_key = re.search('lastkey="(.*?)"', html, re.S).group(1)
pic_url = re.findall('"pic imgcover"><img class="lazyload" data-src="(.*?)\?imageMogr2', html, re.S)
j = 1

for i in range(10):
	for each in pic_url:
	    print('now downloading:' + each)
	    pic = requests.get(each)
	    ext = re.split('[.?]', each)[-1]    #.或？分隔
	    fp = open('/Users/PythonWorkplace/load/pic/' + str(j) + '.' + str(ext),'wb')
	    fp.write(pic.content)
	    fp.close()
	    j += 1
	weburl = url_more + str(last_key) + '.json'
	data = requests.get(weburl, headers = webheader).content
	html = str(data.decode())
	#html = gzip.GzipFile(fileobj = StringIO(data.decode())).read()
	last_key = re.search('"last_key":(.*?),', html, re.S).group(1)
	pic_url = re.findall('"image":"(.*?)\?imageMogr2', html, re.S)

print('爬取完毕')

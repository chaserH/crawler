# -*-encoding: utf8-*-
import requests,re
import codecs
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
dest_filename = '电影.xlsx'
ws1 = wb.active
ws1.title = '电影top250'

DOWNLOAD_URL = 'https://movie.douban.com/top250'

def download_page(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	}
	data = requests.get(url, headers = headers).content
	return data

def get_li(doc):
	soup = BeautifulSoup(doc, 'html.parser')
	#ol = soup.find('ol', attrs = {'class':'grid_view'})
	ol = soup.select('.grid_view > li')
	name = []
	star_con = []
	score = []
	info_list = []
	#for i in ol.find_all('li'):
	for i in ol:
		detail1 = i.find('div', attrs = {'class': 'hd'})
		movie_name = detail1.find('span', attrs = {'class': 'title'}).get_text()
		detail2 = i.find('div', attrs = {'class': 'bd'})
		star_num = detail2.find(text = re.compile('评价'))
		level_star = detail2.find('span', attrs = {'class': 'rating_num'}).get_text()
		info = detail2.find('span', attrs = {'class':'inq'})
		name.append(movie_name)
		star_con.append(star_num)
		score.append(level_star)
		if info:
			info_list.append(info.get_text())
		else:
			info_list.append('无')
	page = soup.find('span', attrs = {'class': 'next'}).find('a')
	if page:
		return name, star_con, score, info_list, DOWNLOAD_URL+page['href']
	return name, star_con, score, info_list, None

def main():
	url = DOWNLOAD_URL
	name = []
	star_con = []
	score = []
	info = []
	while url:
		doc = download_page(url)
		movie_name, star_num, level_star, info_list, url = get_li(doc)
		name = name + movie_name
		star_con = star_con + star_num
		score = score + level_star
		info = info + info_list
	for(i,j,k,l) in zip(name,star_con,score,info):
		col_A = 'A%s'%(name.index(i)+1)
		col_B = 'B%s'%(name.index(i)+1)
		col_C = 'C%s'%(name.index(i)+1)
		col_D = 'D%s'%(name.index(i)+1)
		ws1[col_A] = i
		ws1[col_B] = j
		ws1[col_C] = k
		ws1[col_D] = l
	wb.save(filename = dest_filename)

if __name__ == '__main__':
	main()



#爬取网站上的图片 

#-*-coding:utf8-*-

import urllib.request    
# import socket    
import re    
# import sys    
import os    

#targetDir = r"/Users/PythonWorkplace/load/pic"  #文件保存路径  
def destFile(path, targetDir):    
    if not os.path.isdir(targetDir):    
        os.mkdir(targetDir)    
    pos = path.rindex('/')    
    t = os.path.join(targetDir, path[pos+1:])    
    return t 
  
def main():
    print('请输入要爬取图片的网址')
    weburl = str(input())
    webname = re.findall('(?:http|https)://(.*?)/', weburl)[0]  #有冒号会导致文件夹无法创建
    targetDir = "/Users/PythonWorkplace/load/" + str(webname)  #文件保存路径 
    #print(targetDir)
    webheaders = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        } 
    req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头  
    webpage = urllib.request.urlopen(req)  #发送请求报头  
    contentBytes = webpage.read()
    print('开始爬取----')  
    for link in set(re.findall(r'(http[^\s]*?(?:jpg|png|gif))', str(contentBytes), re.S)):  #正则表达式查找所有的图片  
        print(link) 
        try: 
        #   urllib.request.urlretrieve(link, destFile(link))
            pic = urllib.request.urlopen(link)
            with open(destFile(link, targetDir),'wb') as fp:
                fp.write(pic.read())
        except:  
            print('失败') #异常抛出
    '''  
        pic = urllib.request.urlopen(link)
        with open('D:/PythonWorkplace/load/' + str(j) + '.jpg','wb') as fp:
            fp.write(pic.read())
        j += 1
    '''
      
if __name__ == "__main__":  #程序运行入口  
    main()

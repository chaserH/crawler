# -*-coding:utf8-*-
import requests
import os
import time
import json
from bs4 import BeautifulSoup
from PIL import Image

def login():
    url = 'https://www.zhihu.com'
    loginURL = 'https://www.zhihu.com/login/email'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "https://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }
    data = {
        'email': 'uname@email.com',
        'password': '******',
        'rememberme': "true",
    }
    #global s
    s = requests.session()
    #global xsrf
    if os.path.exists('cookiefile'):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req1 = s.get(url, headers=headers)
        soup = BeautifulSoup(req1.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        # 建立一个zhihu.html文件,用于验证是否登陆成功
        with open('zhihu.html', 'wb') as f:
            f.write(req1.content)
            print('html文件已生成')
    else:
        req = s.get(url, headers=headers)
        print(req)
        soup = BeautifulSoup(req.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        data['_xsrf'] = xsrf
        timestamp = int(time.time() * 1000)
        captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
        print(captchaURL)
        with open('zhihu_captcha.gif', 'wb') as f:
            captchaREQ = s.get(captchaURL, headers=headers)
            f.write(captchaREQ.content)
        #用pillow的Image显示验证码
        #如果没有安装pillow，到源代码所在的目录去找到验证码然后手动输入
        try:
            im = Image.open('zhihu_captcha.gif')
            im.show()
            im.close()
        except:
            print('请到 %s 目录找到zhihu_captcha.gif 手动输入' %os.path.abspath('zhihu_captcha.gif'))
        loginCaptcha = input('input captcha:\n').strip()
        data['captcha'] = loginCaptcha
        print(data)
        loginREQ = s.post(loginURL, headers=headers, data=data)
        if not loginREQ.json()['r']:
            print(s.cookies.get_dict())
            with open('cookiefile', 'w') as f:
                json.dump(s.cookies.get_dict(), f)
        else:
            print('login fail')

if __name__ =='__main__':
    login()


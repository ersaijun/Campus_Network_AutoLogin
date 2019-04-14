# -*- coding: utf-8 -*-
__author__ = "kaspar.s"
__date__ = '2018/11/4 13:57'

import datetime,socket,requests,base64

LOGIN_PAGE_URL = "https://gw.buaa.edu.cn:804/beihanglogin.php?ac_id=1&url=http://gw.buaa.edu.cn:804/beihangview.php"
def is_net_ok():
        s = socket.socket()
        s.settimeout(3)
        try:
                status = s.connect_ex(('www.baidu.com',443))
                if status == 0 :
                        s.close()
                        return True
                else:
                        return False
        except:
                return False

def login_request(name , password):
        if not is_net_ok():
                print("[03] {} raspberry is offline ， request now... ".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                # password =  base64.b64encode(password.encode()).decode()     # 加密
                data1 = {"action": "login",
                        "username": name,
                        "password": password,
                        "ac_id": 1 ,
                        "save_me": 0,
                        "ajax": 1}
                try:
                        result = requests.post(LOGIN_PAGE_URL, data = data1)
                        # print(result.text)
                        print("[01] {} login success  ".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                except:
                        print("[00] {} requsest error ，raspberry isnot connected to WIFI ".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        else:
                print("[02] {} raspberry is online  ".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

if __name__ == "__main__":
        login_request("sy1507605", "z1992s")

import time
from typing import Any
import requests


class ZheJiang():

    """A Class for the completion of Zhejiang Youth University Study"""

    def __init__(self, nid, cardNo, openid, SendKey: str = None):
        """
        description: init the class
        :param nid: 团组织编号, 形如N003************
        :param cardNo: 打卡昵称, 可能为学号, 也可能为姓名
        :param openid: 微信openid
        :param SendKey: Server酱的SendKey

        all params are required except SendKey, all params are need to capture from the network
        """
        self.nid = nid
        self.cardNo = cardNo
        self.openid = openid
        self.SendKey = SendKey
        self.session = requests.session()
        self.access_token = self.getAccessToken()
        time.sleep(5)
        self.current_course = self.getCurrentCourse()
        time.sleep(5)
        self.result = None
        self.msg = None


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        description: call the class
        :param args: args
        :param kwds: kwds
        :return: True if success, False if failed
        """
        self.sign()
    

    def getAccessToken(self) -> str:
        """
        description: get the access_token
        :return: access_token
        """
        time_stamp = str(int(time.time()))  # 获取时间戳
        url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/login/we-chat/callback?callback=https%3A%2F%2Fqczj" \
          ".h5yunban.com%2Fqczj-youth-learning%2Findex.php&scope=snsapi_userinfo&appid=wx56b888a1409a2920&openid=" + \
          self.openid + "&nickname=ZhangSan&headimg=&time=" + time_stamp + "&source=common&sign=&t=" + time_stamp
        
        res = self.session.get(url)
        access_token = res.text[45:81]
        print("获取到AccessToken:", access_token)
        return access_token
    
    
    def getCurrentCourse(self):
        """
        description: get the current course
        :return: current course
        """
        url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/common-api/course/current?accessToken=" + self.access_token
        res = self.session.get(url)
        if (res.status_code == 200):  # 验证正常
            print("获取到最新课程代号:", res.json()["result"]["id"])
            return res.json()["result"]["id"]
        else:
            print("获取最新课程失败！")
            print(res.text)
            return False
        

    def sign(self):
        """
        description: sign the current course
        :return: True if success, False if failed
        """
        data = {
            "course": self.current_course,
            "subOrg": None,
            "nid": self.nid,
            "cardNo": self.cardNo
        }
        url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/user-api/course/join?accessToken=" + self.access_token
        res = self.session.post(url, json=data)
        status = int(res.json()["status"])
        self.msg = res.json()["message"]
        print(res.text)
        if (res.status_code == 200 and status == 200):
            self.result = True
        else:
            self.result = False
            
        

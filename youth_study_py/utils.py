# Tools for the main program
import requests


def push(func):
    def warp(x):
        objs: tuple = func(x)
        for obj in objs:
            if obj.result:
                print("签到成功!")
                text = '已为您完成青年大学习，请登入青春浙江-大学习-个人中心-网上团课学习记录，进行检查'
            else:
                print("签到失败!")
                text = '青年大学习打卡失败，请检查本程序或手动打卡, 日志: ' + obj.msg
                
            url = f'https://sctapi.ftqq.com/{obj.SendKey}.send?'
            payload = {
                'title': '「您的青年大学习通知」',
                'desp': text,
                'channel': '9'
            }  
            if obj.SendKey:
                print(text)
                requests.post(url=url, params=payload)


    return warp

@push
def job(*jobs) -> None:
    """
    description: job function
    :param ZheJiangs: ZheJiang instances
    :return: None
    """
    for job in jobs:
        job()
    return jobs
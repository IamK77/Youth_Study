import time

from schedule import every, repeat, run_pending

from youth_study_py.zhejiang import ZheJiang
from youth_study_py.utils import job


@repeat(every(1).wednesday.at("18:00"))
def do():
    zj = ZheJiang(nid="ur_nid", cardNo="ur_cardNo", openid="ur_openid", SendKey='ur_SendKey')
    job(zj)

if __name__ == '__main__':
    while True:
        run_pending()
        time.sleep(1)

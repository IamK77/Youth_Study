# ***Youth Study***

用于青年大学习的简单工具

目前仅支持浙江地区

注意本库只能作为学习用途, 造成的任何问题与本库开发者无关

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行

```python
import time

from schedule import every, repeat, run_pending

from youth_study_py.zhejiang import ZheJiang
from youth_study_py.utils import job


@repeat(every(1).wednesday.at("20:45"))
def do():
    zj = ZheJiang(nid="ur_nid", cardNo="ur_cardNo", openid="ur_openid", SendKey='ur_SendKey')
    job(zj)

if __name__ == '__main__':
    while True:
        run_pending()
        time.sleep(1)
```
在IDE中打开时, 鼠标悬停在`ZheJiang`上, 会有提示框提示参数, job可以接受多个参数


运行:
```bash
python main.py
```

### 获取参数

获取参数的方法请依照[此处](./docs/WH.md)的说明

### 定时任务

自定义定时请自行查阅Schedule的[文档](https://schedule.readthedocs.io/en/stable/index.html)


或者使用默认即可

## API

文档请参考[此处](./docs/api.md)

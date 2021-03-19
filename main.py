# encoding:utf-8
import json
import requests
import time
import schedule
import datetime

with open("config.json", encoding='utf-8') as f:
    config = json.load(f)


def send_message(text):
    api = "https://sctapi.ftqq.com/SCT21003TBu9KqhuNDRLFDlDBPab79XBQ.send"
    title = u"打卡情况"
    #content = """测试消息1\n测试消息2"""
    openid = "HeQingHua"

    data = {
        "text": title,
        "desp": text,
        "openid": openid
    }
    message = requests.post(api, data=data)
    print(message)


def covid19_auto_report():
    url = 'https://reserve.25team.com/wxappv1/yi/addReport'

    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html",
        "token": config["何清华"]["token"],
        "Connection": "keep-alive",
        "Host": "reserve.25team.com"
    }
    r = requests.post(url, headers=headers, json=config["何清华"])
    output = r.json()
    print(output["msg"])
    send_message(output["msg"])


if __name__ == "__main__":
    covid19_auto_report()
    schedule.every().day.at("08:00").do(covid19_auto_report)

    a = 60
    while True:
        if(a == 60):
            dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("I'm working        "+dtime)
            a = 0
        schedule.run_pending()
        time.sleep(60)
        a += 1

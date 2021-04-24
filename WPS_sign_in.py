# encoding: utf-8
import random, os, json
import requests

try:
    wps_sid = os.getenv('WPS_SID').strip()

    s = requests.session()
    question = 'https://vip.wps.cn/checkcode/signin/question'
    r = s.get(question, cookies = {'wps_sid': wps_sid})

    data = {'platform': '2',
            'answer': '1',
            'auth_type': 'answer'}

    answer = 'https://vip.wps.cn/sigin/do'
    r = s.post(answer, cookies = {'wps_sid': wps_sid}, data = data)
except:
    print('没有配置SID，如需积分签到，请到 settings->secrets 中配置 WPS_SID')


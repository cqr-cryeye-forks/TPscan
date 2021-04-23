import argparse
from urllib.parse import urlparse

import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='address [url: http://example.xyz or https://example.xyz]', type=str)
    return parser.parse_args()


def get_pocdict(vulnname: str) -> dict:
    return {
        'vulnname': vulnname.split('.')[-1],
        'isvul': False,
        'vulnurl': None,
        'payload': None,
        'proof': None,
        'response': None,
        'exception': None,
    }


def parse_base_url(url: str):
    scheme, netloc, *_ = urlparse(url=url)
    return f'{scheme}://{netloc}'


def acknowledge_url(url: str):
    try:
        requests.get(url=url, verify=False)
        return True
    except requests.exceptions.InvalidSchema as e:
        print(f'An error occurred. Description below.\n'
              f'Invalid format of passed url: {url}.\n'
              f'[valid format of url is: http://example.xyz]\n'
              f'Error: {e}')
    except requests.exceptions.ConnectionError as e:
        print(f'An error occurred. Description below.\n'
              f'Unreachable host. Check your internet connection just in case.\n'
              f'Error: {e}')
    except BaseException as e:
        print(f'An error occurred. Unexpected behavior.\n'
              f'Error: {e}')


def parse_results(results: list) -> list:
    output = []
    for item in results:
        if isinstance(item, dict) and item.get('isvul'):
            print(f'Vuln found: {item.get("vulnname")}, url: {item.get("vulnurl")}')
            output.append(item)
        elif isinstance(item, list):
            results.extend(item)
    return output

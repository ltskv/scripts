#! /usr/bin/python
from argparse import ArgumentParser

import requests


def my_ipv6():
    r = requests.get('https://api6.ipify.org', params={
        'format': 'json'
    })
    return r.json()['ip']


def my_ipv4():
    r = requests.get('https://api.ipify.org', params={
        'format': 'json'
    })
    return r.json()['ip']


if __name__ == '__main__':

    ap = ArgumentParser()
    ap.add_argument('--domain', action='append', required=True)
    ap.add_argument('--token', required=True, type=str)
    ap.add_argument('--verbose', action='store_true')
    sp = ap.add_subparsers(dest='cmd', required=True)
    txt = sp.add_parser('txt')
    txt.add_argument('text', type=str)
    ip = sp.add_parser('ip')
    ip.add_argument('-4', dest='ipv4', nargs='?', const='', type=str)
    ip.add_argument('-6', dest='ipv6', nargs='?', const='', type=str)
    clear = sp.add_parser('clear')

    args = ap.parse_args()

    params = {'domains': args.domain, 'token': args.token,
              'verbose': args.verbose}

    if args.cmd == 'clear':
        params['clear'] = True
    elif args.cmd == 'txt':
        params['txt'] = args.text
    elif args.cmd == 'ip':
        if args.ipv4 is None and args.ipv6 is None:
            ap.error('You must specify which IP you want to update')
        elif args.ipv4 is not None and args.ipv6 is None:
            params['ip'] = args.ipv4
        elif args.ipv4 is None and args.ipv6 is not None:
            params['ipv6'] = args.ipv6 or my_ipv6()
        elif args.ipv4 is not None and args.ipv6 is not None:
            params['ip'] = args.ipv4 or my_ipv4()
            params['ipv6'] = args.ipv6 or my_ipv6()

    r = requests.get('https://www.duckdns.org/update', params=params)
    print(r.text)

#!/usr/bin/python3

try:
    from json import loads
    from requests import post
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def json_resp_handler(resp):
    return loads(resp)


def decode_response(resp):
    return resp.decode(encoding='utf-8')


def perform_post_query(url, data):
    try:
        resp = post(url, data=data)
        return resp.content
    except Exception as e:
        print("[!]Error : {}".format(str(e)))
        return ""


def get_langs(key, resp_lang, base_url='https://translate.yandex.net/api/v1.5/tr.json/getLangs'):
    resp = perform_post_query(base_url, [('key', key), ('ui', resp_lang)])
    if(not resp):
        return {}
    return json_resp_handler(decode_response(resp)).get('langs', {})


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler for yandex translate :)')
    exit(0)
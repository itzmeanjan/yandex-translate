#!/usr/bin/python3

try:
    from requests import post
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def perform_post_query(url, data):
    try:
        resp = post(url, data=data)
        return resp.json()
    except Exception as e:
        return {'error': str(e)}


'''
    resp_lang is one of those language codes supported by yandex translate, in which you will get response.
'''


def get_langs(key, resp_lang, base_url='https://translate.yandex.net/api/v1.5/tr.json/getLangs'):
    return perform_post_query(base_url, [('key', key), ('ui', resp_lang)])


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler for yandex translate :)')
    exit(0)

#!/usr/bin/python3

try:
    from requests import post
    from sys import path
    from os.path import realpath, dirname
    path.append(dirname(realpath(__file__)))
    from check_lang_code import check_code
    from push_into_db import push
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
    By default it's set to en -> English
'''


def get_langs(key, resp_lang='en', base_url='https://translate.yandex.net/api/v1.5/tr.json/getLangs', db_name='lang_codes'):
    if(resp_lang != 'en'):
        if(check_code(db_name, resp_lang)):
            resp = perform_post_query(base_url, [('key', key), ('ui', resp_lang)])
        else:
            resp = perform_post_query(base_url, [('key', key), ('ui', 'en')])    
    else:
        resp = perform_post_query(base_url, [('key', key), ('ui', 'en')])
    langs = resp.get('langs', {})
    if(not langs):
        return resp
    push(db_name, langs)
    return langs


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler for yandex translate :)')
    exit(0)

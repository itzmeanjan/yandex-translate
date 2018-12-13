#!/usr/bin/python3

try:
    from sys import path
    from os.path import realpath, dirname
    path.append(dirname(realpath(__file__)))
    from get_lang_list import perform_post_query
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


'''
    hint should be a list of possible language codes that's supported by yandex translate.
    Languages in hint will be prioratized during detecting language of text.
'''


def detect_lang(key, text, hint=[], base_url='https://translate.yandex.net/api/v1.5/tr.json/detect'):
    if(hint):
        return perform_post_query(base_url, [('key', key), ('text', text), ('hint', ','.join(hint))])
    else:
        return perform_post_query(base_url, [('key', key), ('text', text)])


if __name__ == "__main__":
    print('[!]This module is designed to be used as a backend handler for yandex translate :)')
    exit(0)

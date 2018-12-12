#!/usr/bin/python3

try:
    from yandex_translate.get_lang_list import perform_post_query, decode_response, json_resp_handler
    from urllib.parse import urlencode
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def detect_lang(key, text, hint=[], base_url='https://translate.yandex.net/api/v1.5/tr.json/detect'):
    resp = ''
    if(hint):
        resp = perform_post_query(base_url, [('key', key), ('text', urlencode([('text', text)]).split('=')[1]), ('hint', ','.join(hint))])
    else:
        resp = perform_post_query(base_url, [('key', key), ('text', urlencode([('text', text)]).split('=')[1])])
    if(not resp):
        return {}
    return json_resp_handler(decode_response(resp))


if __name__ == "__main__":
    print('[!]This module is designed to be used as a backend handler for yandex translate :)')
    exit(0)

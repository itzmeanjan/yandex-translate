#!/usr/bin/python3


try:
    from sys import path
    from os.path import realpath, dirname
    path.append(dirname(realpath(__file__)))
    import detect_lang as yan
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


'''
    This function performs a post query at yandex translate and returns a python dict, holding response.
    If a blank dict gets returned, some error has occurred.
    
    format paramter has got a default value of 'plain', can also be 'html', in that case make you that you pass a html string as text parameter.
'''


def translate(key, text, lang, format='plain', base_url='https://translate.yandex.net/api/v1.5/tr.json/translate'):
    '''
        text to translate needs to be lesser than 10000 characters for post query
    '''
    if(len(text) > 10000):
        return {'text': 'Length of text more than 10000 characters'}
    return yan.perform_post_query(base_url, [('key', key), ('text', text), ('lang', lang), ('format', format)])


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler for yandex translate.')
    exit(0)
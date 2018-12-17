#!/usr/bin/python3

try:
    import plyvel as pl
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def check_code(name, code):
    try:
        db_handler = pl.DB(name, create_if_missing=True)
        if(not db_handler.get(code.encode('utf-8'), b'')):
            db_handler.close()
            return False
        db_handler.close()
        return True
    except pl.Error:
        return False
    except Exception:
        return False


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)

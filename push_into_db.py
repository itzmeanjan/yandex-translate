#!/usr/bin/python3

try:
    import plyvel as pl  # python3 api for using levelDB
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def push(name, data, create_if_missing=True):
    try:
        db_handler = pl.DB(name, create_if_missing=create_if_missing)
        for i, j in data.items():
            db_handler.put(i.encode('utf-8'), j.encode('utf-8'))
        db_handler.close()
    except pl.Error:
        return False
    except Exception:
        return False
    return True


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler.')
    exit(0)

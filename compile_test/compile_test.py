# -*- coding: utf-8 -*-

"""Main module."""

import pkgutil

def res(p='compile_test', v='resource.txt'):
    return pkgutil.get_data(p, v)

def main():
    print 'loaded main'
    print res()
    from IPython import embed
    embed()

if __name__ == '__main__':
    main()

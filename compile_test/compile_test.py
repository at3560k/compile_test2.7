# -*- coding: utf-8 -*-

"""Main module."""

import pkgutil
import sys

def res(p='compile_test', v='resource.txt'):
    return pkgutil.get_data(p, v)

def main():
    print 'loaded main'
    try:
        print res()
        # That's right -- it successfully prints none!
        nuisance = res()
        if nuisance is None and getattr(sys, 'frozen', False):
            print 'successfully loaded nothing, am I a bug?  No, everything returns None!'
            print res('resource', 'data/resource.txt')
            # It has a totally different module when frozen!

    except IOError: # What I thought I'd get...
        print 'did not find in the module'

if __name__ == '__main__':
    main()

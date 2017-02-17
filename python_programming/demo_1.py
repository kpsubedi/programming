#!/usr/bin/python

import sys


def usage():
    print('program <arg>')
    exit(1)

def welcome(who):
    print('Hello {}'.format(who))

if len(sys.argv) <=1:
    usage()
welcome(sys.argv[1])



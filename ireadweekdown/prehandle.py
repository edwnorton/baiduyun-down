#!/home/tq/py_env/django/bin/python3
# -*- coding: utf-8 -*-
import os, sys, time
spath = os.path.dirname(os.path.realpath(__file__))
sfile = os.path.join(spath, 'book.log')
prehandle_txt = os.path.join(spath, 'prehandle.txt')
with open (sfile, 'r') as s, open (prehandle_txt, 'w') as f:
    lines = s.readlines()
    for i in lines:
        bookdir = str(i).rstrip('\n')
        bookpath = os.path.dirname(i)
        f.write(bookpath + '\n')

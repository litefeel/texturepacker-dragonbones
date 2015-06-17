#!/usr/bin/python
# coding=utf-8

import os, os.path
import sys
from optparse import OptionParser


def getpath():
    dir = '.'
    if len(sys.argv) == 2:
        dir = sys.argv[1]
    return os.path.abspath(dir)

def readfile(filename):
    if not os.path.exists(filename):
        return None
    with open(filename) as f:
        data = f.read()
        f.close()
        return data

def writefile(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
        f.close()

def convert2utf8(path):
    if path.endswith(('.xml', '.json')):
        data = readfile(path)
        data = data.decode(sys.getfilesystemencoding())
        data = data.encode('utf8')
        writefile(path, data)


# -------------- main --------------
if __name__ == '__main__':
    usage = "usage: %prog [file or directory]"
    parser = OptionParser(usage=usage)
    (opts, args) = parser.parse_args()
    if len(args) > 1 :
        parser.error("only accept one path!")

    path = args[0] if len(args) == 1 else '.'
    path = os.path.abspath(path)

    if os.path.isfile(path):
        convert2utf8(path)
    else:
        for root, dirs, files in os.walk(path):
            for f in files:
                convert2utf8(os.path.join(root, f))

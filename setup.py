#!/usr/bin/env python3

from distutils.core import setup
import os

if os.system('./autogen.sh') == 1:
    print("\nautogen failed")
    os.exit(1)

if os.system('./configure') == 1:
    print("\nconfigure failed")
    os.exit(1)

if os.system('make') == 1:
    print("\nmake failed")
    os.exit(1)

if os.system('make check') == 1:
    print("\nmake check failed")
    os.exit(1)

if os.system('make distcheck') == 1:
    print("\nmake distcheck failed")
    os.exit(1)

###setup(
###    setup_requires=['d2to1'],
###    extras_require={'test': ['nose', ]},
###    d2to1=True
###)
#

#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize
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

setup(name='pycangjie',
      version='1.0',
      description='Python binding to libcangjie',
      author='Cangjians',
      url='https://github.com/Cangjians/pycangjie',
      packages=['cangjie'],
      ext_modules = cythonize("src/cangjie/*.pyx")
     )

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = []

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'name': 'CSS Cleaner',
    'description': 'A utility to clean your CSS files',
    'author': 'Tarun Arora and Manish Gill',
    'url': 'https://github.com/gobelinus/csscleaner',
    'version': '0.0.1',
    'install_requires': requirements,
    'packages': ['csscleaner', 'tests'],
    'scripts': [],
    'long_description': read('README.md')
}

setup(**config)


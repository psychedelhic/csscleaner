#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_requirements():
    return [elem.strip() for elem in
            read('requirements.txt').splitlines()
            if elem.strip() and not elem.startswith('#')]

config = {
    'name': 'CSS Cleaner',
    'description': 'A utility to clean your CSS files',
    'author': 'Tarun Arora and Manish Gill',
    'url': 'https://github.com/gobelinus/csscleaner',
    'version': '0.0.1',
    'license': 'GPL',
    'install_requires': get_requirements(),
    'packages': find_packages(),
    'scripts': [],
    'long_description': read('README.md')
}

setup(**config)


#!/usr/bin/python

from distutils.core import setup

args = {
    'name': 'dctrl2xml',
    'version': '0.9',
    'description': 'Debian control data to XML converter',
    'author': 'Frank S. Thomas',
    'author_email': 'fst@debian.org',
    'scripts': ['dctrl2xml'],
    'license': 'GPL-3+'
}

if __name__ == '__main__':
    setup(**args)

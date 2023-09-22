# -*- coding: utf-8 -*-

import sys
from setuptools import setup

requires = ['pyyaml']
if float('%d.%d' % sys.version_info[:2]) < 2.7:
    requires.append('ordereddict')

setup(
    name='yamlordereddictloader',
    version='0.4.2',
    author='François Ménabé',
    author_email='francois.menabe@gmail.com',
    url='https://github.com/fmenabe/python-yamlordereddictloader',
    download_url='https://github.com/fmenabe/python-yamlordereddictloader',
    license='MIT License',
    description='YAML loader and dumper for PyYAML allowing to keep keys order.',
    long_description=open('README.rst').read(),
    keywords=['YAML', 'loader', 'dumper', 'ordered', 'OrderedDict', 'pyyaml'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'Intended Audience :: System Administrators',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Topic :: Utilities'],
    py_modules=['yamlordereddictloader'],
    install_requires=requires)

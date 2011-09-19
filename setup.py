#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name		= 'python-yubico',
      version		= '0.0.5',
      description	= 'Python code for talking to Yubico\'s YubiKeys',
      author		= 'Cornelius Koelbel (Fredrik Thulin)',
      author_email	= 'cornelius.koelbel@lsexperts.de (fredrik@yubico.com)',
      url		= 'http://www.lsexperts.de (http://www.yubico.com/)',
      license		= 'BSD',
      packages		= ['yubico'],
      package_dir	= {'': 'Lib'},
      tests_require	= "nose >=0.10.0b1",
      test_suite	= "nose.collector",
     )

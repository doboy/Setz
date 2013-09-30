#!/usr/bin/python
# Copyright (c) 2013 Huan Do, http://huan.do
"""
Queries set operators from files using python syntax

Usage:
  setz "query" [a.txt b.txt ..]

  --help for more info
"""

import os
from setuptools import setup

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name="Setz",
  version="0.0.1",
  author="Huan Do",
  author_email="doboy0@gmail.com",
  description=("Queries set operators from files using python syntax"),
  long_description=read("README.md"),
  url="https://github.com/Doboy/Setz",
  py_modules=['setz', 'setz_funcs'],
  scripts=["bin/setz"])

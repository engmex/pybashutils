#!/usr/bin/env python
from setuptools import setup

req = ['nose','colorama','binaryornot']

setup(name='pythonutils',
      packages=['pythonutils'],
      author='Michael Hirsch, Ph.D.',
      description='Cross-platform utilities for computer maintenance',
      url='https://github.com/scivison/pybashutils',
	  install_requires=req,
	  )

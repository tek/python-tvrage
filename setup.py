#!/usr/bin/env python

import os

from setuptools import setup
from tvrage import __version__, __author__, __license__

setup(name='tvrampage',
      description='python client for the tvrage.com XML API',
      long_description=open(
          os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      license=__license__,
      version=__version__,
      author=__author__,
      author_email='herr.kreutzer@gmail.com',
      url='https://github.com/ckreutzer/python-tvrage',
      packages=['tvrage'],
      install_requires=["beautifulsoup4"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Operating System :: OS Independent'
      ]
      )

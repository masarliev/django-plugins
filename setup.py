#!/usr/bin/env python

from distutils.core import setup
import stalwart
setup(name='stalwart',
      version=stalwart.__version__,
      description='Stalwart plugins',
      author='Mitko Masarliev',
      author_email='mitko@masalriev.net',
      url='http://masarliev.net/',
      packages=['stalwart', 'stalwart.piecemaker', 'stalwart.livelog'],
     )
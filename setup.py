#!/usr/bin/env python

from distutils.core import setup

setup(
    name='relaax',
    version='1.0',
    description='RELAAX solution',
    author='Stanislav Volodarskiy',
    author_email='stanislav@dplrn.com',
    url='http://www.dplrn.com/',
    packages=['relaax'],
    requires=[],
    provides=['relaax'],
    scripts=[
        'bin/relaax-parameter-server',
        'bin/relaax-rlx-server',
        'bin/relaax-client-ale',
        'bin/relaax-client-gym'
    ]
)

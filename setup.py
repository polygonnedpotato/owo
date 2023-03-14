#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'owo',
    version = '0.0.0-alpha0',
    description = 'tool to get information on just about everything',
    author = 'arris kathery',
    python_requires = '>=3.10',
    packages = ['owo'],
    package_dir = {'owo': 'owo'},
    package_data = {'owo': [
        'res/locale/*.yaml'
    ]}
)

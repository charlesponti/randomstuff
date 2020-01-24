# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pontistuff',
    version='0.1.0',
    description='a bunch of random stuff',
    long_description=readme,
    author='Charles Ponti',
    author_email='cj@ponti.io',
    url='https://github.com/charlesponti/randomstuff',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
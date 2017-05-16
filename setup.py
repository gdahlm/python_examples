# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python_examples',
    version='0.1.0',
    description='Example code for Python',
    long_description=readme,
    author='Greg Dahlman',
    url='https://github.com/gdahlman/python_examples',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


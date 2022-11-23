# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in healthpostapp/__init__.py
from healthpostapp import __version__ as version

setup(
	name='healthpostapp',
	version=version,
	description='Frappe application to manage.',
	author='healthpostapp Technologies Private Limited',
	author_email='healthpostapp@healthpostapp.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
#!/usr/bin/env python
import io
import os
import pandoc
from pip.req import parse_requirements
import re
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand
import sys


if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist bdist_wheel upload')
	sys.exit()


def read(*filenames, **kwargs):
	encoding = kwargs.get('encoding', 'utf-8')
	sep = kwargs.get('sep', '\n')
	buf = []
	for filename in filenames:
		with io.open(filename, encoding=encoding) as f:
			buf.append(f.read())
	return sep.join(buf)

def find_version(*file_paths):
	version_file = read(os.path.join(*file_paths))
	version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
	if version_match:
		return version_match.group(1)
	raise RuntimeError('Unable to find version string.')

try:
	pandoc.core.PANDOC_PATH = '/usr/bin/pandoc'

	doc = pandoc.Document()
	doc.markdown = open('README.md').read()
	with open('README.rst', 'w+') as rst:
		rst.write(doc.rst)
	long_description = read('README.rst')
except:
	long_description = read('README.md')

requires = [str(ir.req) for ir in parse_requirements('requirements/prod.txt')]

class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True

	def run_tests(self):
		import pytest

		errcode = pytest.main(self.test_args)
		sys.exit(errcode)

setup(
	name='stock-me',
	version=find_version('stock-me', '__init__.py'),
	description='Auto-generated description',
	long_description=long_description,
	keywords='stock-me',
	author='@TheKevJames (auto-generated)',
	author_email='KevinJames@thekev.in (auto-generated)',
	url='git@github.com:TheKevJames/stock-me.git',
	license='MIT License',
	packages=find_packages(exclude=['test']),
	include_package_data=True,
	install_requires=requires,
	tests_require=['pytest'],
	zip_safe=False,
	classifiers=[
		'Programming Language :: Python',
		'Development Status :: 1 - Planning',
		'Natural Language :: English',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
	],
	test_suite='test',
	extras_require={
		'testing': ['pytest'],
	},
)

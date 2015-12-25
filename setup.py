# coding: utf-8
from __future__ import absolute_import, division, print_function

import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand  # noqa


INIT_FILE = 'spacetrack/__init__.py'
init_data = open(INIT_FILE).read()

metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_data))

VERSION = metadata['version']
LICENSE = metadata['license']
DESCRIPTION = metadata['description']
AUTHOR = metadata['author']
EMAIL = metadata['email']

requires = {
    'logbook>=0.12.3',
    'represent>=1.4.0',
    'requests',
    'six',
}

extras_require = dict()

extras_require['test'] = {
    'pytest>=2.7.3',
    # 'responses',
}

extras_require['dev'] = {
    'doc8',
    'flake8',
    'flake8-coding',
    'flake8-future-import',
    'pep8-naming',
    'plumbum',
    'pyenchant',
    'pytest-cov',
    'shovel',
    'sphinx',
    'sphinx_rtd_theme',
    'sphinxcontrib-spelling',
    'tox',
    'twine',
    'watchdog',
}

extras_require['dev'] |= extras_require['test']

# if sys.version_info[:2] < (3, 3):
#     extras_require['dev'] |= {'mock'}


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='spacetrack',
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.rst').read(),
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/python-astrodynamics/spacetrack',
    packages=find_packages(),
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    license=LICENSE,
    install_requires=requires,
    extras_require=extras_require,
    tests_require=extras_require['test'])
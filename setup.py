#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('description.txt') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click==6.0',
                'pandas==0.22.0',
                'numpy==1.14.0',
                'xlrd==1.1.0']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Franco Donati",
    author_email='f.donati@cml.leidenuniv.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description="A software to model Circular Economy policy and" +
                "technological interventions in Environmentally " +
                "Extended Input-Output Analysis (EXIOBASE V3.3)",
    entry_points={
        'console_scripts': [
            'pycirk=pycirk.pycirk_cli:main',
        ],
    },


    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pycirk',
    name='pycirk',
    packages=find_packages(include=['pycirk']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://bitbucket.org/CML-IE/pycirk/src/master/',
    version='1.0.0',
    zip_safe=False,
)

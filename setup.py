# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages

REQUIRES = [
    'configobj',
    'falcon',
    'setuptools >= 1.1.6',
    'six',
    'stoplight'
]

setup(
    name='dynamicNetworkConfig',
    version='0.2',
    description='Dynamic Network Configuration',
    license='Apache License 2.0',
    url='',
    author='Clockwerks Software, LLC',
    author_email='',
    install_requires=REQUIRES,
    test_suite='dynamicNetworkConfig',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'dnc_server = dynamicNetworkConfig.cmd.server:run',
            # 'dnc_client = dynamicNetworkConfig.cmd.client:run'
        ]
    },
    data_files=[
        ('config', ['examples/config.ini', 'examples/configspec.ini'])
    ],
    packages=find_packages(exclude=['tests*', 'dynamicNetworkConfig/tests*'])
)

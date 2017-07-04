#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name='onions',

    version='0.1',

    packages=find_packages(),

    author="Abhinav Biswas",

    author_email="iotdocktor@gmail.com",

    description="Display onion sites hosted",

    include_package_data=True,

    url='https://github.com/IotDockTor/container-torrify',

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: System :: Installation/Setup",
    ],


    entry_points={
        'console_scripts': [
            'onions = onions:main',
        ],
    },

    license="WTFPL",
)

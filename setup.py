#!/usr/bin/env python
import os
from setuptools import setup, find_packages


long_description = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.rst'
    )
).read()


setup(
    name='pymux',
    author='Jonathan Slenders',
    version='0.3',
    license='LICENSE',
    url='https://github.com/jonathanslenders/',
    description='Pure Python terminal multiplexer.',
    long_description=long_description,
    packages=find_packages('.'),
    install_requires = [
        'prompt_toolkit==0.57',
        'pyte>=0.4.10',
        'six>=1.9.0',
        'docopt>=0.6.2',
    ],
    entry_points={
        'console_scripts': [
            'pymux = pymux.entry_points.run_pymux:run',
        ]
    },
)

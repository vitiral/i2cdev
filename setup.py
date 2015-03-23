#!/usr/bin/env python

from setuptools import setup
from i2cdev import __version__

setup(
    name='i2cdev',
    version=__version__,
    description='Simple I2C Library for linux',
    author='Garrett Berg',
    author_email='garrett@cloudformdesign.com',
    url='https://github.com/cloudformdesign/i2cdev',
    py_modules=['i2cdev'],
    license='MIT',
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Operating System Kernels',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: System :: Hardware :: Hardware Drivers',
    ]
)

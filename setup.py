#!/usr/bin/env python

from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Gym is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

setup(
    name='safety_gym',
    packages=['safety_gym'],
    install_requires=[
        'gym>=0.18.3,<=0.21.0',
        'joblib',
        'mujoco_py==1.50.1.68',
        'numpy',
        'xmltodict',
    ],
)

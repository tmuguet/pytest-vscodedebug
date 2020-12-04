#!/usr/bin/env python
# -*- coding: utf-8 -*-

# flake8: noqa

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-vscodedebug",
    use_scm_version=True,
    author="Thomas Muguet",
    author_email="hi@tmuguet.me",
    maintainer="Thomas Muguet",
    maintainer_email="hi@tmuguet.me",
    license="MIT",
    url="https://github.com/tmuguet/pytest-vscodedebug",
    description="A pytest plugin to easily enable debugging tests within Visual Studio Code",
    long_description=read("README.rst"),
    py_modules=["pytest_vscodedebug"],
    python_requires=">=3.5",
    setup_requires=["setuptools_scm"],
    install_requires=["pytest>=3.5.0", "debugpy>=1.0.0rc2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Debuggers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "pytest11": [
            "vscodedebug = pytest_vscodedebug",
        ],
    },
)

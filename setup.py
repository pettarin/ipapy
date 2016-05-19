#!/usr/bin/env python
# coding=utf-8

"""
Set ipapy package up.
"""

from setuptools import setup, Extension

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Production"

setup(
    name="ipapy",
    packages=["ipapy", "ipapy.data"],
    package_data={"ipapy.data": ["*.dat"]},
    version="0.0.1.0",
    description="ipapy is a Python module to work with IPA strings",
    author="Alberto Pettarin",
    author_email="alberto@albertopettarin.it",
    url="https://github.com/pettarin/ipapy",
    license="MIT License",
    long_description=open("README.rst", "r").read(),
    install_requires=[],
    scripts=["bin/ipapy"],
    keywords=[
        "ipapy",
        "International Phonetic Alphabet",
        "IPA",
        "ASCII IPA",
        "ASCIIIPA",
        "ASCII-IPA",
        "Kirshenbaum",
        "Kirshenbaum IPA",
        "Unicode",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Documentation",
        "Topic :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
)

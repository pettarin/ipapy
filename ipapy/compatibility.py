#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function
import sys

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

PY2 = (sys.version_info[0] == 2)

def is_unicode_string(s):
    if PY2:
        return isinstance(s, unicode)
    return isinstance(s, str)

def int2unichr(n):
    if PY2:
        return unichr(n)
    return chr(n)

def hex2unichr(s):
    return int2unichr(int(s, base=16))




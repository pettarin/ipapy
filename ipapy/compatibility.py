#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This module defines constants and functions
to make ipapy compatible with both Python 2 and Python 3.
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
"""
``True`` if running on Python 2, and ``False`` otherwise
"""

def is_unicode_string(string):
    """
    Return ``True`` if the given string is a Unicode string,
    that is, of type ``unicode`` in Python 2 or ``str`` in Python 3.

    :param str string: the string to be checked
    :rtype: bool
    """
    if PY2:
        return isinstance(string, unicode)
    return isinstance(string, str)

def to_unicode_string(string):
    """
    Return a Unicode string out of the given string.
    
    On Python 2, it calls ``unicode`` with ``utf-8`` encoding.
    On Python 3, it just returns the given string.

    :param str string: the string to convert to Unicode
    :rtype: (Unicode) str
    """
    if PY2:
        return unicode(string, encoding="utf-8")
    return string

def int2unichr(codepoint):
    """
    Return the Unicode character with the given codepoint,
    given as an integer.

    :param int codepoint: the Unicode codepoint of the desired character
    :rtype: (Unicode) str
    """
    if PY2:
        return unichr(codepoint)
    return chr(codepoint)

def hex2unichr(hex_string):
    """
    Return the Unicode character with the given codepoint,
    given as an hexadecimal string.

    :param str hex_string: the Unicode codepoint of the desired character
    :rtype: (Unicode) str
    """
    return int2unichr(int(hex_string, base=16))




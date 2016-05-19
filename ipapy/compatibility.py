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
__status__ = "Production"

PY2 = (sys.version_info[0] == 2)
"""
``True`` if running on Python 2, and ``False`` otherwise
"""

def is_unicode_string(string):
    """
    Return ``True`` if the given string is a Unicode string,
    that is, of type ``unicode`` in Python 2 or ``str`` in Python 3.

    Return ``None`` if ``string`` is ``None``.

    :param str string: the string to be checked
    :rtype: bool
    """
    if string is None:
        return None
    if PY2:
        return isinstance(string, unicode)
    return isinstance(string, str)

def to_unicode_string(string):
    """
    Return a Unicode string out of the given string.
    
    On Python 2, it calls ``unicode`` with ``utf-8`` encoding.
    On Python 3, it just returns the given string.

    Return ``None`` if ``string`` is ``None``.

    :param str string: the string to convert to Unicode
    :rtype: (Unicode) str
    """
    if string is None:
        return None
    if is_unicode_string(string):
        return string
    # if reached here, string is a byte string 
    if PY2:
        return unicode(string, encoding="utf-8")
    return string.decode(encoding="utf-8")

def to_str(string):
    """
    Return the given string (either byte string or Unicode string)
    converted to native-str, that is,
    a byte string on Python 2, or a Unicode string on Python 3.

    Return ``None`` if ``string`` is ``None``.

    :param str string: the string to convert to native-str
    :rtype: native-str
    """
    if string is None:
        return None
    if isinstance(string, str):
        return string
    if PY2:
        return string.encode("utf-8")
    return string.decode("utf-8")

def int_to_unichr(codepoint):
    """
    Return the Unicode character with the given codepoint,
    given as an integer.

    Example::
        97 => a

    :param int codepoint: the Unicode codepoint of the desired character
    :rtype: (Unicode) str
    """
    if PY2:
        return unichr(codepoint)
    return chr(codepoint)

def hex_to_unichr(hex_string):
    """
    Return the Unicode character with the given codepoint,
    given as an hexadecimal string.

    Return ``None`` if ``hex_string`` is ``None`` or is empty.

    Example::
        "0061"   => a
        "U+0061" => a

    :param str hex_string: the Unicode codepoint of the desired character
    :rtype: (Unicode) str
    """
    if (hex_string is None) or (len(hex_string) < 1):
        return None
    if hex_string.startswith("U+"):
        hex_string = hex_string[2:]
    return int_to_unichr(int(hex_string, base=16))

def unicode_to_hex(unicode_string):
    """
    Return a string containing the Unicode hexadecimal codepoint
    of each Unicode character in the given Unicode string.

    Return ``None`` if ``unicode_string`` is ``None``.

    Example::
        a  => U+0061
        ab => U+0061 U+0062

    :param str unicode_string: the Unicode string to convert
    :rtype: (Unicode) str
    """
    if unicode_string is None:
        return None
    acc = []
    for c in unicode_string:
        s = hex(ord(c)).replace("0x", "").upper()
        acc.append("U+" + ("0" * (4 - len(s))) + s)
    return u" ".join(acc)




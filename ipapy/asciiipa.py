#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.compatibility import hex_to_unichr
from ipapy.data import load_csv_file
from ipapy.ipastring import IPAString

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Production"

ASCII_IPA_DATA_FILE_PATH = "asciiipa.dat"
"""
Path of the built-in IPA database,
relative to the ``data/`` directory
"""

def load_ascii_ipa_data():
    """
    Load the ASCII IPA data from the built-in ASCII IPA database, creating the following globals:

    1. ``ASCII_IPA_CHARS``: list of all ASCII IPA characters
    2. ``IPA_DESCRIPTORS_TO_ASCII_IPA``: dict mapping a canonical representation of an IPAChar to an ASCII string 
    """
    ascii_ipa_signs = []
    ipa_descriptors_to_ascii_ipa = {}
    for line in load_csv_file(ASCII_IPA_DATA_FILE_PATH, 4):
        # unpack line
        i_type, i_desc, i_unicode, i_ascii = line
        # if i_ascii is given as 4 hex chars (e.g., 00A1), convert it to unicode
        if ((len(i_ascii) == 4) and (i_ascii.startswith("00"))) or (i_ascii.startswith("U+")):
            i_ascii = hex_to_unichr(i_ascii)
        # get descriptors
        name = "%s %s" % (i_desc, i_type)
        descriptors = frozenset([p for p in name.split() if len(p) > 0])
        ipa_descriptors_to_ascii_ipa[descriptors] = i_ascii
        ascii_ipa_signs.append(i_ascii)
    return ascii_ipa_signs, ipa_descriptors_to_ascii_ipa
ASCII_IPA_SIGNS, IPA_DESCRIPTORS_TO_ASCII_IPA = load_ascii_ipa_data()

def unicode_string_to_ascii_string(unicode_string, ignore=False, single_char_parsing=False):
    """
    Convert the given Unicode string, representing an IPA string,
    to a string containing the corresponding ASCII IPA representation.

    Return ``None`` if ``unicode_string`` is ``None``.

    :param str unicode_string: the Unicode string to be parsed
    :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
    :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
    :rtype: str
    """
    if unicode_string is None:
        return None
    ipa_string = IPAString(unicode_string=unicode_string, ignore=ignore, single_char_parsing=single_char_parsing)
    return ipa_string_to_ascii_string(ipa_string=ipa_string, ignore=ignore)

def ipa_string_to_ascii_string(ipa_string, ignore=False):
    """
    Convert the given IPAString to a string
    containing the corresponding ASCII IPA representation.

    :param IPAString ipa_string: the IPAString to be parsed
    :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
    :rtype: str
    """
    acc = []
    for ipa_char in ipa_string:
        canonical = ipa_char.canonical_representation
        if canonical in IPA_DESCRIPTORS_TO_ASCII_IPA:
            acc.append(IPA_DESCRIPTORS_TO_ASCII_IPA[canonical])
        elif not ignore:
            raise ValueError("The IPA string contains an IPA character that is not mapped to ASCII IPA: '%s" % canonical)
    return u"".join(acc)




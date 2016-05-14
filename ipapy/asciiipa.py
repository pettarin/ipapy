#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.compatibility import hex2unichr
from ipapy.data import load_csv_file
from ipapy.ipachar import canonical_representation
from ipapy.ipastring import IPAString

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

ASCII_IPA_DATA_FILE_PATH = "asciiipa.dat"

def load_ascii_ipa_data():
    ascii_ipa_signs = []
    ipa_properties_to_ascii_ipa = {}
    for line in load_csv_file(ASCII_IPA_DATA_FILE_PATH, 4):
        # unpack line
        i_type, i_desc, i_unicode, i_ascii = line
        # if i_ascii is given as 4 hex chars (e.g., 00A1), convert it to unicode
        if (len(i_ascii) == 4) and (i_ascii.startswith("0")):
            i_ascii = hex2unichr(i_ascii)
        # get properties
        name = "%s %s" % (i_desc, i_type)
        properties = canonical_representation([p for p in name.split() if len(p) > 0])
        ipa_properties_to_ascii_ipa[properties] = i_ascii
        ascii_ipa_signs.append(i_ascii)
    return ascii_ipa_signs, ipa_properties_to_ascii_ipa
ASCII_IPA_SIGNS, IPA_PROPERTIES_TO_ASCII_IPA = load_ascii_ipa_data()

def unicode_string_to_ascii_string(unicode_string, ignore=False):
    ipa_string = IPAString(unicode_string=unicode_string, ignore=ignore)
    return ipa_string_to_ascii_string(ipa_string=ipa_string, ignore=ignore)

def ipa_string_to_ascii_string(ipa_string, ignore=False):
    acc = []
    for ipa_char in ipa_string:
        canonical = ipa_char.canonical_representation
        if canonical in IPA_PROPERTIES_TO_ASCII_IPA:
            acc.append(IPA_PROPERTIES_TO_ASCII_IPA[canonical])
        elif not ignore:
            raise ValueError("The IPA string contains an IPA character that is not mapped to ASCII IPA: '%s" % canonical)
    return u"".join(acc)




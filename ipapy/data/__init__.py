#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This module defines data constants and it loads the built-in IPA database.
"""

from __future__ import absolute_import
from __future__ import print_function
import io
import re
import os

from ipapy.compatibility import hex_to_unichr
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipachar import IPADiacritic
from ipapy.ipachar import IPASuprasegmental
from ipapy.ipachar import IPATone

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.2"
__email__ = "alberto@albertopettarin.it"
__status__ = "Production"

IPA_DATA_FILE_CODEPOINT_SEPARATOR = u" "
"""
Separator between Unicode codepoints or
Unicode compound strings for a given IPAChar
"""

IPA_DATA_FILE_COMMENT = u"#"
""" Ignore lines starting with this character """

IPA_DATA_FILE_COMPOUND_OPERATOR = u"+"
"""
Operator to specify Unicode compound strings,
e.g. 0070+032A = LATIN SMALL LETTER P + COMBINING BRIDGE BELOW
"""

IPA_DATA_FILE_FIELD_SEPARATOR = u","
""" Field separator for the data file """

IPA_DATA_FILE_NOT_AVAILABLE = u"N/A"
""" Placeholder for an IPAChar not encoded in Unicode """

IPA_DATA_FILE_PATH = u"ipa.dat"
"""
Path of the built-in IPA database,
relative to the ``data/`` directory
"""

def load_data_file(relative_file_path, comment_string, field_separator, values_per_line=None):
    """
    Load a comma-separated file, returning a list of tuples.

    It ignores lines starting with "#" or empty lines.

    If ``values_per_line`` is not ``None``,
    check that each line (tuple)
    has the prescribed number of values.

    :param str relative_file_path: path of the file to load, relative to this source code file
    :param int values_per_line: number of elements of each line; if ``None``, do not check
    :rtype: list of tuples
    """
    tuples = []
    file_path = os.path.join(os.path.dirname(__file__), relative_file_path)
    with io.open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if (len(line) > 0) and (not line.startswith(comment_string)):
                # unpack line
                values = line.split(field_separator)
                if (values_per_line is not None) and (len(values) != values_per_line):
                    raise ValueError("Data file '%s' contains a bad line: '%s'" % (file_path, line))
                tuples.append(tuple(values))
    return tuples

def load_ipa_data():
    """
    Load the IPA data from the built-in IPA database, creating the following globals:

    1. ``IPA_CHARS``: list of all IPAChar objects
    2. ``UNICODE_TO_IPA``: dict mapping a Unicode string (often, a single char) to an IPAChar
    3. ``UNICODE_TO_IPA_MAX_KEY_LENGTH``: length of a longest key in ``UNICODE_TO_IPA``
    4. ``IPA_TO_UNICODE``: map an IPAChar canonical representation to the corresponding Unicode string (or char)
    """
    ipa_signs = []
    unicode_to_ipa = {}
    ipa_to_unicode = {}
    max_key_length = 0
    for line in load_data_file(
        relative_file_path=IPA_DATA_FILE_PATH,
        comment_string=IPA_DATA_FILE_COMMENT,
        field_separator=IPA_DATA_FILE_FIELD_SEPARATOR,
        values_per_line=3
    ):
        # unpack data
        i_type, i_desc, i_unicode = line

        # create desc string and name string
        desc = "%s %s" % (i_desc, i_type)
        name = re.sub(r" [ ]*", " ", desc)

        # create a suitable IPACharacter obj
        if i_type == "consonant":
            obj = IPAConsonant(name=name, descriptors=desc)
        elif i_type == "vowel":
            obj = IPAVowel(name=name, descriptors=desc)
        elif i_type == "diacritic":
            obj = IPADiacritic(name=name, descriptors=desc)
        elif i_type == "suprasegmental":
            obj = IPASuprasegmental(name=name, descriptors=desc)
        elif i_type == "tone":
            obj = IPATone(name=name, descriptors=desc)
        else:
            raise ValueError("The IPA data file contains a bad line, defining an unknown type '%s': '%s'" % (i_type, line))
        ipa_signs.append(obj)

        # map Unicode codepoint to object, if the former is available
        primary_set = False
        for codepoint in i_unicode.split(IPA_DATA_FILE_CODEPOINT_SEPARATOR):
            # deal with compound symbols, like '||' = major-group suprasegmental
            key = None
            if not IPA_DATA_FILE_NOT_AVAILABLE in codepoint:
                key = u"".join([hex_to_unichr(c) for c in codepoint.split(IPA_DATA_FILE_COMPOUND_OPERATOR)])
            # if we have a key, map it
            if key is not None:
                if key in unicode_to_ipa:
                    raise ValueError("The IPA data file contains a bad line, redefining codepoint '%s': '%s'" % (codepoint, line))
                unicode_to_ipa[key] = obj
                if not primary_set:
                    primary_set = True
                    ipa_to_unicode[obj.canonical_representation] = key
                    obj.unicode_repr = key
                    max_key_length = max(max_key_length, len(key))
    return ipa_signs, unicode_to_ipa, max_key_length, ipa_to_unicode
IPA_CHARS, UNICODE_TO_IPA, UNICODE_TO_IPA_MAX_KEY_LENGTH, IPA_TO_UNICODE = load_ipa_data()




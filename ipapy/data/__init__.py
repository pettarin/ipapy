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
__email__ = "alberto@albertopettarin.it"

DATA_FILE_CODEPOINT_JOINER = u"_"
"""
Character to specify Unicode compound strings,
e.g. 0070_032A or U+0070_U+032A = LATIN SMALL LETTER P + COMBINING BRIDGE BELOW
"""

DATA_FILE_CODEPOINT_SEPARATOR = u" "
"""
Separator between Unicode codepoints or
Unicode compound strings for a given IPAChar
"""

DATA_FILE_COMMENT = u"#"
""" Ignore lines starting with this character """

DATA_FILE_FIELD_SEPARATOR = u","
""" Field separator for the data file """

DATA_FILE_VALUE_NOT_AVAILABLE = u"N/A"
""" Placeholder for an IPAChar not encoded in Unicode """

DATA_FILE_ASCII_NUMERICAL_CODEPOINT_START = u"00"
""" Numerical codepoints in ASCII fields must start with this string """

DATA_FILE_ASCII_UNICODE_CODEPOINT_START = u"U+"
""" Unicode codepoints in ASCII fields must start with this string """

def convert_unicode_field(string):
    """
    Convert a Unicode field into the corresponding list of Unicode strings.

    The (input) Unicode field is a Unicode string containing
    one or more Unicode codepoints (``xxxx`` or ``U+xxxx`` or ``xxxx_yyyy``),
    separated by a space.

    :param str string: the (input) Unicode field
    :rtype: list of Unicode strings
    """
    values = []
    for codepoint in [s for s in string.split(DATA_FILE_CODEPOINT_SEPARATOR) if s != DATA_FILE_VALUE_NOT_AVAILABLE]:
        if len(codepoint) > 0:
            values.append(u"".join([hex_to_unichr(c) for c in codepoint.split(DATA_FILE_CODEPOINT_JOINER)]))
    return values

def convert_ascii_field(string):
    """
    Convert an ASCII field into the corresponding list of Unicode strings.

    The (input) ASCII field is a Unicode string containing
    one or more ASCII codepoints (``00xx`` or ``U+00xx`` or
    an ASCII string not starting with ``00`` or ``U+``),
    separated by a space.

    :param str string: the (input) ASCII field
    :rtype: list of Unicode strings
    """
    values = []
    for codepoint in [s for s in string.split(DATA_FILE_CODEPOINT_SEPARATOR) if s != DATA_FILE_VALUE_NOT_AVAILABLE]:
        if (codepoint.startswith(DATA_FILE_ASCII_NUMERICAL_CODEPOINT_START)) or (codepoint.startswith(DATA_FILE_ASCII_UNICODE_CODEPOINT_START)):
            values.append(hex_to_unichr(codepoint))
        else:
            values.append(codepoint)
    return values

def convert_raw_tuple(value_tuple, format_string):
    """
    Convert a tuple of raw values, according to the given line format.

    :param tuple value_tuple: the tuple of raw values
    :param str format_string: the format of the tuple
    :rtype: list of tuples
    """ 
    values = []
    for v, c in zip(value_tuple, format_string):
        if v is None:
            # append None
            values.append(v)
        elif c == u"s":
            # string
            values.append(v)
        elif c == u"S":
            # string, split using space as delimiter
            values.append([s for s in v.split(u" ") if len(s) > 0])
        elif c == u"i":
            # int
            values.append(int(v))
        elif c == u"U":
            # Unicode
            values.append(convert_unicode_field(v))
        elif c == u"A":
            # ASCII
            values.append(convert_ascii_field(v))
        #elif c == u"x":
        #    # ignore
        #    pass
    return tuple(values)

def load_data_file(
    file_path,
    file_path_is_relative=False,
    comment_string=DATA_FILE_COMMENT,
    field_separator=DATA_FILE_FIELD_SEPARATOR,
    line_format=None
):
    """
    Load a data file, with one record per line and
    fields separated by ``field_separator``,
    returning a list of tuples.

    It ignores lines starting with ``comment_string`` or empty lines.

    If ``values_per_line`` is not ``None``,
    check that each line (tuple)
    has the prescribed number of values.

    :param str file_path: path of the data file to load
    :param bool file_path_is_relative: if ``True``, ``file_path`` is relative to this source code file
    :param str comment_string: ignore lines starting with this string
    :param str field_separator: fields are separated by this string
    :param str line_format: if not ``None``, parses each line according to the given format
                            (``s`` = string, ``S`` = split string using spaces,
                            ``i`` = int, ``x`` = ignore, ``U`` = Unicode, ``A`` = ASCII)
    :rtype: list of tuples
    """
    raw_tuples = []
    if file_path_is_relative:
        file_path = os.path.join(os.path.dirname(__file__), file_path)
    with io.open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if (len(line) > 0) and (not line.startswith(comment_string)):
                raw_list = line.split(field_separator)
                if len(raw_list) != len(line_format):
                    raise ValueError("Data file '%s' contains a bad line: '%s'" % (file_path, line))
                raw_tuples.append(tuple(raw_list))
    if (line_format is None) or (len(line_format) < 1):
        return raw_tuples
    return [convert_raw_tuple(t, line_format) for t in raw_tuples]

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
        file_path=u"ipa.dat",
        file_path_is_relative=True,
        line_format=u"ssU"
    ):
        # unpack data
        i_type, i_desc, i_unicode_keys = line

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
        if len(i_unicode_keys) > 0:
            # canonical Unicode string
            first_key = i_unicode_keys[0]
            ipa_to_unicode[obj.canonical_representation] = first_key
            obj.unicode_repr = first_key
            max_key_length = max(max_key_length, len(first_key))
            # add all Unicode strings 
            for key in i_unicode_keys:
                if key in unicode_to_ipa:
                    raise ValueError("The IPA data file contains a bad line, redefining codepoint '%s': '%s'" % (key, line))
                unicode_to_ipa[key] = obj
    return ipa_signs, unicode_to_ipa, max_key_length, ipa_to_unicode
IPA_CHARS, UNICODE_TO_IPA, UNICODE_TO_IPA_MAX_KEY_LENGTH, IPA_TO_UNICODE = load_ipa_data()




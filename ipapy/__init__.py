#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This module defines common functions and it exposes the built-in IPA database.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.data import IPA_CHARS
from ipapy.data import IPA_TO_UNICODE
from ipapy.data import UNICODE_TO_IPA
from ipapy.data import UNICODE_TO_IPA_MAX_KEY_LENGTH

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

__version__ = "0.0.7"
__status__ = "Production"

def split_using_dictionary(string, dictionary, max_key_length, single_char_parsing=False):
    """
    Return a list of (non-empty) substrings of the given string,
    where each substring is either:
    
    1. the longest string starting at the current index
       that is a key in the dictionary, or
    2. a single character that is not a key in the dictionary.

    If ``single_char_parsing`` is ``False``,
    parse the string one Unicode character at a time,
    that is, do not perform the greedy parsing.

    :param iterable string: the iterable object ("string") to split into atoms
    :param dict dictionary: the dictionary mapping atoms ("characters") to something else
    :param int max_key_length: the length of a longest key, in number of characters
    :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
    """
    def substring(string, i, j):
        if isinstance(string[i], tuple):
            # transform list of tuples with one element in a tuple with all elements
            return tuple([string[k][0] for k in range(i, j)])
        # just return substring
        return string[i:j]
    
    if string is None:
        return None
    if (single_char_parsing) or (max_key_length < 2):
        return [c for c in string]
    acc = []
    l = len(string)
    i = 0
    while i < l:
        found = False
        for j in range(min(i + max_key_length, l), i, -1):
            sub = substring(string, i, j)
            if sub in dictionary:
                found = True
                acc.append(sub)
                i = j
                break
        if not found:
            acc.append(string[i])
            i += 1
    return acc

def ipa_substrings(unicode_string, single_char_parsing=False):
    """
    Return a list of (non-empty) substrings of the given string,
    where each substring is either:
    
    1. the longest Unicode string starting at the current index
       representing a (known) valid IPA character, or
    2. a single Unicode character (which is not IPA valid).

    If ``single_char_parsing`` is ``False``,
    parse the string one Unicode character at a time,
    that is, do not perform the greedy parsing.

    For example, if ``s = u"\u006e\u0361\u006d"``,
    with ``single_char_parsing=True`` the result will be
    a list with a single element: ``[u"\u006e\u0361\u006d"]``,
    while ``single_char_parsing=False`` will yield a list with three elements:
    ``[u"\u006e", u"\u0361", u"\u006d"]``.

    Return ``None`` if ``unicode_string`` is ``None``.

    :param str unicode_string: the Unicode string to be parsed
    :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
    :rtype: list of str
    """
    return split_using_dictionary(
        string=unicode_string,
        dictionary=UNICODE_TO_IPA,
        max_key_length=UNICODE_TO_IPA_MAX_KEY_LENGTH,
        single_char_parsing=single_char_parsing
    )

def invalid_ipa_characters(unicode_string, indices=False):
    """
    Return the list of Unicode characters
    in the given Unicode string
    that are not IPA valid.

    Return ``None`` if ``unicode_string`` is ``None``.

    :param str unicode_string: the Unicode string to be parsed
    :param bool indices: if ``True``, return a list of pairs (index, invalid character),
                         instead of a list of str (characters).
    :rtype: list of str or list of (int, str) 
    """
    if unicode_string is None:
        return None
    if indices:
        return [(i, unicode_string[i]) for i in range(len(unicode_string)) if unicode_string[i] not in UNICODE_TO_IPA]
    return set([c for c in unicode_string if c not in UNICODE_TO_IPA])

def is_valid_ipa(unicode_string):
    """
    Check whether the given Unicode string contains characters
    that are not IPA valid.

    Return ``None`` if ``unicode_string`` is ``None``.

    :param str unicode_string: the Unicode string to be parsed
    :rtype: bool
    """
    if unicode_string is None:
        return None
    for c in unicode_string:
        if not c in UNICODE_TO_IPA:
            return False
    return True

def remove_invalid_ipa_characters(unicode_string, return_invalid=False, single_char_parsing=False):
    """
    Remove all Unicode characters that are not IPA valid
    from the given string,
    and return a list of substrings of the given string,
    each mapping to a (known) valid IPA character.

    Return ``None`` if ``unicode_string`` is ``None``.

    :param str unicode_string: the Unicode string to be parsed
    :param bool return_invalid: if ``True``, return a pair ``(valid, invalid)``,
                                where ``invalid`` is a list of Unicode characters
                                that are not IPA valid.
    :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
    :rtype: list of str
    """
    if unicode_string is None:
        return None
    substrings = ipa_substrings(unicode_string, single_char_parsing=single_char_parsing)
    valid = [s for s in substrings if s in UNICODE_TO_IPA]
    if return_invalid:
        return (valid, [s for s in substrings if s not in UNICODE_TO_IPA])
    return valid




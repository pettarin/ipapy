#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.data import IPA_SIGNS
from ipapy.data import IPA_TO_UNICODE
from ipapy.data import UNICODE_TO_IPA

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

def invalid_ipa_characters(unicode_string, indices=False):
    if indices:
        return [(i, unicode_string[i]) for i in range(len(unicode_string)) if unicode_string[i] not in UNICODE_TO_IPA]
    return set(sorted([c for c in unicode_string if c not in UNICODE_TO_IPA]))

def is_valid_ipa(unicode_string):
    for char in unicode_string:
        if not char in UNICODE_TO_IPA:
            return False
    return True

def remove_invalid_ipa_characters(unicode_string, return_invalid=False):
    valid = [c for c in unicode_string if c in UNICODE_TO_IPA]
    if return_invalid:
        return (valid, [c for c in unicode_string if c not in UNICODE_TO_IPA])
    return valid





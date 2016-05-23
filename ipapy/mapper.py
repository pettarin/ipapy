#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function
from collections import MutableMapping

from ipapy.compatibility import is_unicode_string
from ipapy.data import load_data_file
from ipapy.ipachar import variant_to_frozenset
from ipapy.ipastring import IPAString

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class Mapper(MutableMapping):
    """
    A Mapper contains
    a map from IPA descriptors
    to arbitrary strings.

    :param dict map_dictionary: a dictionary, mapping IPA descriptors to string
    """
    
    TAG = u"IPAMapper"

    def __init__(self, *args, **kwargs):
        self.ipadescriptors_to_str = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        key = self._check_key(key)
        return self.ipadescriptors_to_str[key]

    def __setitem__(self, key, value):
        key = self._check_key(key)
        self._check_value(value)
        self.ipadescriptors_to_str[key] = value

    def __delitem__(self, key):
        key = self._check_key(key)
        del self.ipadescriptors_to_str[key]

    def __iter__(self):
        return iter(self.ipadescriptors_to_str)

    def __len__(self):
        return len(self.ipadescriptors_to_str)

    def _check_key(self, key):
        try:
            return variant_to_frozenset(key)
        except:
            raise TypeError("The given key must be convertible to a frozen set of strings")

    def _check_value(self, value):
        if not is_unicode_string(value):
            raise TypeError("The given value must be a Unicode string")

    @property
    def signs(self):
        """
        Return the list of map values.

        :rtype: list of str
        """
        return list(self.ipadescriptors_to_str.values())

    @property
    def ipa_descriptors(self):
        """
        Return the list of map keys.

        :rtype: list of frozenset objects
        """
        return list(self.ipadescriptors_to_str.keys())

    def map_ipa_string(self, ipa_string, ignore=False, return_as_list=False):
        """
        Convert the given IPAString to a string
        containing the corresponding ASCII IPA representation.

        :param IPAString ipa_string: the IPAString to be parsed
        :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
        :param bool return_as_list: if ``True``, return as a list of strings, one for each IPAChar,
                                    instead of their concatenation (single str)
        :rtype: str 
        """
        acc = []
        for ipa_char in ipa_string:
            canonical = ipa_char.canonical_representation
            if canonical in self.ipadescriptors_to_str:
                acc.append(self.ipadescriptors_to_str[canonical])
            elif not ignore:
                raise ValueError("The IPA string contains an IPA character that is not mapped: '%s" % canonical)
        if return_as_list:
            return acc
        return u"".join(acc)

    def map_unicode_string(self, unicode_string, ignore=False, single_char_parsing=False, return_as_list=False):
        """
        Convert the given Unicode string, representing an IPA string,
        to a string containing the corresponding mapped representation.

        Return ``None`` if ``unicode_string`` is ``None``.

        :param str unicode_string: the Unicode string to be parsed
        :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
        :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
        :param bool return_as_list: if ``True``, return as a list of strings
        :rtype: str
        """
        if unicode_string is None:
            return None
        ipa_string = IPAString(unicode_string=unicode_string, ignore=ignore, single_char_parsing=single_char_parsing)
        return self.map_ipa_string(ipa_string=ipa_string, ignore=ignore, return_as_list=return_as_list)




#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function
from collections import MutableMapping

from ipapy import split_using_dictionary
from ipapy.compatibility import is_unicode_string
from ipapy.data import load_data_file
from ipapy.ipachar import variant_to_canonical_string
from ipapy.ipastring import IPAString

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class Mapper(MutableMapping):
    """
    A Mapper contains
    a map from IPA canonical representation 
    to arbitrary Unicode strings.

    :param dict map_dictionary: a dictionary, mapping IPA descriptors to string
    """
    
    TAG = u"IPAMapper"

    def __init__(self, *args, **kwargs):
        self.max_key_length = 0
        self.ipa_canonical_representation_to_mapped_str = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        key = self._check_key(key)
        return self.ipa_canonical_representation_to_mapped_str[key]

    def __setitem__(self, key, value):
        key = self._check_key(key)
        self._check_value(value)
        self.ipa_canonical_representation_to_mapped_str[key] = value
        self.max_key_length = max(self.max_key_length, len(key))

    def __delitem__(self, key):
        key = self._check_key(key)
        del self.ipa_canonical_representation_to_mapped_str[key]

    def __iter__(self):
        return iter(self.ipa_canonical_representation_to_mapped_str)

    def __len__(self):
        return len(self.ipa_canonical_representation_to_mapped_str)

    def _check_key(self, key):
        if isinstance(key, tuple):
            try:
                return tuple([variant_to_canonical_string(k) for k in key])
            except:
                raise TypeError("The given key must be a list or a set of descriptor strings, or a Unicode string.")
        else: 
            try:
                return variant_to_canonical_string(key)
            except:
                raise TypeError("The given key must be a list or a set of descriptor strings, or a Unicode string.")

    def _check_value(self, value):
        if not is_unicode_string(value):
            raise TypeError("The given value must be a Unicode string")

    @property
    def signs(self):
        """
        Return the list of map values.

        :rtype: list of str
        """
        return list(self.ipa_canonical_representation_to_mapped_str.values())

    @property
    def ipa_descriptors(self):
        """
        Return the list of map keys.

        :rtype: list of str
        """
        return list(self.ipa_canonical_representation_to_mapped_str.keys())

    def can_map_ipa_string(self, ipa_string):
        """
        Return ``True`` if the mapper can map all the IPA characters
        in the given IPA string.

        :param IPAString ipa_string: the IPAString to be parsed
        :rtype: bool
        """
        canonical = [(c.canonical_representation, ) for c in ipa_string]
        split = split_using_dictionary(canonical, self, self.max_key_length, single_char_parsing=False)
        for sub in split:
            if not sub in self.ipa_canonical_representation_to_mapped_str:
                return False
        return True

    def map_ipa_string(self, ipa_string, ignore=False, return_as_list=False, return_can_map=False):
        """
        Convert the given IPAString to a string
        containing the corresponding ASCII IPA representation.

        :param IPAString ipa_string: the IPAString to be parsed
        :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
        :param bool return_as_list: if ``True``, return as a list of strings, one for each IPAChar,
                                    instead of their concatenation (single str)
        :param bool return_can_map: if ``True``, return a pair ``(bool, str)``, where the first element
                                    says if the mapper can map all the IPA characters in the given IPA string,
                                    and the second element is either ``None`` or the mapped string/list
        :rtype: str or (bool, str) or (bool, list)
        """
        acc = []
        can_map = True
        canonical = [(c.canonical_representation, ) for c in ipa_string]
        split = split_using_dictionary(canonical, self, self.max_key_length, single_char_parsing=False)
        for sub in split:
            try:
                acc.append(self.ipa_canonical_representation_to_mapped_str[sub])
            except KeyError:
                if ignore:
                    can_map = False
                else:
                    raise ValueError("The IPA string contains an IPA character that is not mapped: %s" % sub)
        mapped = acc if return_as_list else u"".join(acc)
        if return_can_map:
            return (can_map, mapped)
        return mapped

    def map_unicode_string(self, unicode_string, ignore=False, single_char_parsing=False, return_as_list=False, return_can_map=False):
        """
        Convert the given Unicode string, representing an IPA string,
        to a string containing the corresponding mapped representation.

        Return ``None`` if ``unicode_string`` is ``None``.

        :param str unicode_string: the Unicode string to be parsed
        :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
        :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
        :param bool return_as_list: if ``True``, return as a list of strings, one for each IPAChar,
                                    instead of their concatenation (single str)
        :param bool return_can_map: if ``True``, return a pair ``(bool, str)``, where the first element
                                    says if the mapper can map all the IPA characters in the given IPA string,
                                    and the second element is either ``None`` or the mapped string/list
        :rtype: str or (bool, str) or (bool, list)
        """
        if unicode_string is None:
            return None
        ipa_string = IPAString(unicode_string=unicode_string, ignore=ignore, single_char_parsing=single_char_parsing)
        return self.map_ipa_string(
            ipa_string=ipa_string,
            ignore=ignore,
            return_as_list=return_as_list,
            return_can_map=return_can_map
        )




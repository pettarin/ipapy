#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function
from collections import MutableSequence

from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy import remove_invalid_ipa_characters
from ipapy.compatibility import is_unicode_string
from ipapy.compatibility import to_str
from ipapy.ipachar import is_list_of_ipachars
from ipapy.ipachar import IPAChar 

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class IPAString(MutableSequence):
    """
    An IPA string, that is, a list of IPAChar objects.

    If the ``ipa_char`` parameter is set, the IPAString
    will be built using the provided list of IPAChar objects.

    Otherwise, if the ``unicode_string`` parameter is set,
    the IPAString will be built by parsing it,
    respecting the ``ignore`` and ``single_char_parsing`` options.
    By default (``single_char_parsing == False``),
    this method builds the canonical representation of the IPA string,
    that is, the one composed by the (prefix) minimum number of IPAChar objects.

    :param list ipa_chars: the list of IPAChar objects
    :param str unicode_string: the Unicode string to be parsed
    :param bool ignore: if ``True``, ignore Unicode characters that are not IPA valid
    :param bool single_char_parsing: if ``True``, parse one Unicode character at a time
    """

    TAG = "IPAString"

    def __init__(self, ipa_chars=None, unicode_string=None, ignore=False, single_char_parsing=False):
        self.ipa_chars = []
        if ipa_chars is not None:
            self.ipa_chars = ipa_chars
        elif unicode_string is not None:
            if not is_unicode_string(unicode_string):
                raise ValueError("The given string is not a Unicode string.")
            if (not ignore) and (not is_valid_ipa(unicode_string)):
                raise ValueError("The given string contains characters not IPA valid. Use the 'ignore' option to ignore them.")
            substrings = remove_invalid_ipa_characters(
                unicode_string=unicode_string,
                return_invalid=False,
                single_char_parsing=single_char_parsing
            )
            self.ipa_chars = [UNICODE_TO_IPA[substring] for substring in substrings]

    def _check(self, value):
        if not isinstance(value, IPAChar):
            raise TypeError("The given value is not an IPAChar object: '%s'" % value)

    def __str__(self):
        return to_str(u"".join([c.__str__() for c in self.ipa_chars]))

    def __unicode__(self):
        return u"".join([c.__unicode__() for c in self.ipa_chars])

    def __repr__(self):
        return u"\n".join([c.__repr__() for c in self.ipa_chars])

    def __iter__(self):
        for ipa_char in self.ipa_chars:
            yield ipa_char

    def __len__(self):
        return len(self.ipa_chars)

    def __add__(self, other):
        if not isinstance(other, IPAString):
            raise TypeError("Cannot concatenate an object that is not an IPAString")
        return IPAString(ipa_chars=(self.ipa_chars + other.ipa_chars))

    def __getitem__(self, i):
        return self.ipa_chars[i]

    def __delitem__(self, i):
        del self.ipa_chars[i]

    def __setitem__(self, i, value):
        self._check(value)
        self.ipa_chars[i] = value

    def insert(self, i, value):
        self._check(value)
        self.ipa_chars.insert(i, value)

    @property
    def ipa_chars(self):
        """
        Return the list of IPAChar objects composing the IPA string

        :rtype: list of IPAChar
        """
        return self.__ipa_chars
    @ipa_chars.setter
    def ipa_chars(self, value):
        """
        Set the list of IPAChar objects composing the IPA string

        :param list value: list of IPAChar objects
        """
        if value is None:
            self.__ipa_chars = []
        else:
            if is_list_of_ipachars(value):
                self.__ipa_chars = value
            else:
                raise TypeError("ipa_chars only accepts a list of IPAChar objects")

    def is_equivalent(self, other, ignore=False):
        """
        Return ``True`` if the IPA string is equivalent to the ``other`` object.

        The ``other`` object can be:

        1. a Unicode string,
        2. a list of IPAChar objects, and
        3. another IPAString.

        :param variant other: the object to be compared against
        :param bool ignore: if other is a Unicode string, ignore Unicode characters not IPA valid
        :rtype: bool
        """
        def is_equivalent_to_list_of_ipachars(other):
            """
            Return ``True`` if the list of IPAChar objects
            in the canonical representation of the string
            is the same as the given list.

            :param list other: list of IPAChar objects
            :rtype: bool
            """
            my_ipa_chars = self.canonical_representation.ipa_chars
            if len(my_ipa_chars) != len(other):
                return False
            for i in range(len(my_ipa_chars)):
                if not my_ipa_chars[i].is_equivalent(other[i]):
                    return False
            return True

        if is_unicode_string(other):
            try:
                return is_equivalent_to_list_of_ipachars(IPAString(unicode_string=other, ignore=ignore).ipa_chars)
            except:
                return False
        if is_list_of_ipachars(other):
            try:
                return is_equivalent_to_list_of_ipachars(other) 
            except:
                return False
        if isinstance(other, IPAString):
            return is_equivalent_to_list_of_ipachars(other.canonical_representation.ipa_chars)
        return False

    @property
    def canonical_representation(self):
        """
        Return a new IPAString, containing the canonical representation of the current string,
        that is, the one composed by the (prefix) minimum number of IPAChar objects.

        :rtype: IPAString
        """
        return IPAString(unicode_string=u"".join([c.__unicode__() for c in self.ipa_chars]))

    @property
    def consonants(self):
        """
        Return a new IPAString, containing only the consonants in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if c.is_consonant])

    @property
    def vowels(self):
        """
        Return a new IPAString, containing only the vowels in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if c.is_vowel])

    @property
    def letters(self):
        """
        Return a new IPAString, containing only the consonants and the vowels in the current string.

        This property is an alias for ``cns_vwl``.

        :rtype: IPAString
        """
        return self.cns_vwl

    @property
    def cns_vwl(self):
        """
        Return a new IPAString, containing only:
        
        1. the consonants, and
        2. the vowels

        in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if c.is_letter])

    @property
    def cns_vwl_str(self):
        """
        Return a new IPAString, containing only:
        
        1. the consonants,
        2. the vowels, and
        3. the stress diacritics

        in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (c.is_letter) or (c.is_suprasegmental and c.is_stress)])

    @property
    def cns_vwl_str_len(self):
        """
        Return a new IPAString, containing only:
        
        1. the consonants,
        2. the vowels, and
        3. the stress diacritics, and
        4. the length diacritics

        in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (c.is_letter) or (c.is_suprasegmental and (c.is_stress or c.is_length))])

    @property
    def cns_vwl_str_len_wb(self):
        """
        Return a new IPAString, containing only:
        
        1. the consonants,
        2. the vowels, and
        3. the stress diacritics,
        4. the length diacritics, and
        5. the word breaks

        in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (c.is_letter) or (c.is_suprasegmental and (c.is_stress or c.is_length or c.is_word_break))])

    @property
    def cns_vwl_str_len_wb_sb(self):
        """
        Return a new IPAString, containing only:
        
        1. the consonants,
        2. the vowels, and
        3. the stress diacritics,
        4. the length diacritics,
        5. the word breaks, and
        6. the syllable breaks

        in the current string.

        :rtype: IPAString
        """
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (c.is_letter) or (c.is_suprasegmental and (c.is_stress or c.is_length or c.is_word_break or c.is_syllable_break))])




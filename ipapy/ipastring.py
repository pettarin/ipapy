#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy import remove_invalid_ipa_characters
from ipapy.compatibility import is_unicode_string

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

class IPAString(object):
    """
    An IPA string, that is, a list of IPAChar objects.

    If the ``ipa_char`` parameter is set, the IPAString
    will be built using the provided list of IPAChar objects.

    Otherwise, if the ``unicode_string`` parameter is set,
    the IPAString will be built by parsing it.

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

    def __str__(self):
        return u"".join([c.__str__() for c in self.ipa_chars])

    def __unicode__(self):
        return u"".join([c.__unicode__() for c in self.ipa_chars])

    def __repr__(self):
        return u"\n".join([c.__repr__() for c in self.ipa_chars])

    def __iter__(self):
        for ipa_char in self.ipa_chars:
            yield ipa_char

    def __len__(self):
        return len(self.ipa_chars)

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




#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.compatibility import is_unicode_string
from ipapy.ipachar import UNICODE_TO_IPA
from ipapy.ipachar import IPAPhone
from ipapy.ipachar import IPADiacritic
from ipapy.ipachar import IPASuprasegmental

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

class IPAString(object):

    def __init__(self, ipa_chars=None, unicode_string=None, ignore=False):
        self.ipa_chars = []
        if ipa_chars is not None:
            self.ipa_chars = ipa_chars
        elif unicode_string is not None:
            if not is_unicode_string(unicode_string):
                raise ValueError("The given string is not a Unicode string.")
            if (not ignore) and (not self.is_valid_ipa(unicode_string)):
                raise ValueError("The given string contains characters not IPA valid. Use ignore=True to ignore.")
            self.ipa_chars = [UNICODE_TO_IPA[c] for c in self.remove_invalid_ipa_characters(unicode_string)]

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
    def cns_vwl(self):
        return IPAString(ipa_chars=[c for c in self.ipa_chars if isinstance(c, IPAPhone)])

    @property
    def cns_vwl_str(self):
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (isinstance(c, IPAPhone)) or (isinstance(c, IPASuprasegmental) and c.is_char_of_type("s"))])

    @property
    def cns_vwl_str_len(self):
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (isinstance(c, IPAPhone)) or (isinstance(c, IPASuprasegmental) and c.is_char_of_type("sl"))])

    @property
    def cns_vwl_str_len_wb(self):
        return IPAString(ipa_chars=[c for c in self.ipa_chars if (isinstance(c, IPAPhone)) or (isinstance(c, IPASuprasegmental) and c.is_char_of_type("slw"))])

    @classmethod
    def invalid_ipa_characters(cls, unicode_string, indices=False):
        if indices:
            return [(i, unicode_string[i]) for i in range(len(unicode_string)) if unicode_string[i] not in UNICODE_TO_IPA]
        return set(sorted([c for c in unicode_string if c not in UNICODE_TO_IPA]))

    @classmethod
    def is_valid_ipa(cls, unicode_string):
        for char in unicode_string:
            if not char in UNICODE_TO_IPA:
                return False
        return True

    @classmethod
    def remove_invalid_ipa_characters(cls, unicode_string):
        return [c for c in unicode_string if c in UNICODE_TO_IPA]




#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This module contains the IPA to ARPABET (ASCII IPA) mapper.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.data import UNICODE_TO_IPA
from ipapy.data import load_data_file
from ipapy.mapper import Mapper

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class ARPABETMapper(Mapper):

    DATA_FILE_PATH = u"arpabet.dat"

    def __init__(self):
        super(ARPABETMapper, self).__init__(self._load_data())

    def _load_data(self):
        """
        Load the ARPABET ASCII IPA data from the built-in database.
        """
        ipa_canonical_string_to_ascii_str = dict()
        for line in load_data_file(
            file_path=self.DATA_FILE_PATH,
            file_path_is_relative=True,
            line_format=u"UA"
        ):
            i_unicode, i_ascii = line
            if (len(i_unicode) == 0) or (len(i_ascii) == 0):
                raise ValueError("Data file '%s' contains a bad line: '%s'" % (self.DATA_FILE_PATH, line))
            i_unicode = i_unicode[0]
            i_ascii = i_ascii[0]
            key = tuple([UNICODE_TO_IPA[c].canonical_representation for c in i_unicode])
            ipa_canonical_string_to_ascii_str[key] = i_ascii
        return ipa_canonical_string_to_ascii_str




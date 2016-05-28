#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This module contains the IPA to Kirshenbaum (ASCII IPA) mapper.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.data import load_data_file
from ipapy.ipachar import variant_to_canonical_string
from ipapy.mapper import Mapper

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class KirshenbaumMapper(Mapper):

    DATA_FILE_PATH = u"kirshenbaum.dat"

    def __init__(self):
        super(KirshenbaumMapper, self).__init__(self._load_data())

    def _load_data(self):
        """
        Load the Kirshenbaum ASCII IPA data from the built-in database.
        """
        ipa_canonical_string_to_ascii_str = dict()
        for line in load_data_file(
            file_path=self.DATA_FILE_PATH,
            file_path_is_relative=True,
            line_format=u"sxA"
        ):
            i_desc, i_ascii = line
            if len(i_ascii) == 0:
                raise ValueError("Data file '%s' contains a bad line: '%s'" % (self.DATA_FILE_PATH, line))
            key = (variant_to_canonical_string(i_desc),)
            ipa_canonical_string_to_ascii_str[key] = i_ascii[0]
        return ipa_canonical_string_to_ascii_str




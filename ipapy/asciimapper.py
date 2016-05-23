#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This module contains the IPA to ASCII (Kirshenbaum) mapper.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.data import load_data_file
from ipapy.mapper import Mapper

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class ASCIIMapper(Mapper):

    def __init__(self):
        super(ASCIIMapper, self).__init__(self._load_data())

    def _load_data(self):
        """
        Load the ASCII IPA data from the built-in ASCII IPA database.
        """
        ipadesc_to_ascii_str = dict()
        for line in load_data_file(
            file_path=u"asciiipa.dat",
            file_path_is_relative=True,
            line_format=u"ssxA"
        ):
            i_type, i_desc, i_ascii = line
            name = "%s %s" % (i_desc, i_type)
            descriptors = frozenset([p for p in name.split() if len(p) > 0])
            if len(i_ascii) == 0:
                raise ValueError("Data file '%s' contains a bad line: '%s'" % (ASCII_IPA_DATA_FILE_PATH, line))
            ipadesc_to_ascii_str[descriptors] = i_ascii[0]
        return ipadesc_to_ascii_str




#!/usr/bin/env python
# coding=utf-8

import unittest

from ipapy.arpabetmapper import ARPABETMapper
from ipapy.ipastring import IPAString

class TestARPABETMapper(unittest.TestCase):

    def test_can_map_ipa_string(self):
        mapper = ARPABETMapper()
        values = [
            (u"", True),
            (u"p", True),
            (u"p\u03B8", True),
            (u"\u027E", True),
            (u"\u0258\u026A", True),
            (u"p\u0258\u026A", True),
            (u"p\u0258\u026Aw", True),
            (u"p\u0258\u026A\u0258\u026Aw", True),
            (u"p\u0258\u026A\u0251w", True),
            (u"\u006A\u0075", True),
            (u"\u1DC6", False),   # valid IPA char, unmapped in Kirshenbaum
            (u"p\u1DC6b", False), # valid IPA char, unmapped in Kirshenbaum
        ]
        for v, e in values:
            self.assertEqual(mapper.can_map_ipa_string(IPAString(unicode_string=v)), e)

    def test_map_unicode_string(self):
        mapper = ARPABETMapper()
        values = [
            (None, None),
            (u"", u""),
            (u"p", u"P"),
            (u"p\u03B8", u"PTH"),
            (u"\u027E", u"DX"),
            (u"p\u0258\u026A", u"PEY"),
            (u"p\u0258\u026Aw", u"PEYW"),
            (u"p\u0258\u026A\u0258\u026Aw", u"PEYEYW"),
            (u"p\u0258\u026A\u0251w", u"PEYAAW"),
            (u"\u006A\u0075", u"YUW"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_unicode_string(v), e)

    def test_map_ipa_string(self):
        mapper = ARPABETMapper()
        values = [
            (u"", u""),
            (u"p", u"P"),
            (u"p\u03B8", u"PTH"),
            (u"\u027E", u"DX"),
            (u"p\u0258\u026A", u"PEY"),
            (u"p\u0258\u026Aw", u"PEYW"),
            (u"p\u0258\u026A\u0258\u026Aw", u"PEYEYW"),
            (u"p\u0258\u026A\u0251w", u"PEYAAW"),
            (u"\u006A\u0075", u"YUW"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_ipa_string(IPAString(unicode_string=v)), e)

    def test_map_unicode_string_ignore(self):
        mapper = ARPABETMapper()
        values = [
            (None, None),
            (u"", u""),
            (u"p", u"P"),
            (u"p\u03B8", u"PTH"),
            (u"\u027E", u"DX"),
            (u"p\u0258\u026A", u"PEY"),
            (u"p\u0258\u026Aw", u"PEYW"),
            (u"p\u0258\u026A\u0258\u026Aw", u"PEYEYW"),
            (u"p\u0258\u026A\u0251w", u"PEYAAW"),
            (u"\u006A\u0075", u"YUW"),
            (u"a\u006A\u0075", u"AEYUW"),
            (u"o\u006A\u0075", u"OHYUW"),
            (u"S\u006A\u0075", u"YUW"),
            (u"S\u006A\u0075\u02C8be", u"YUWBEH"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_unicode_string(v, ignore=True), e)

    def test_map_ipa_string_ignore(self):
        mapper = ARPABETMapper()
        values = [
            (u"", u""),
            (u"p", u"P"),
            (u"p\u03B8", u"PTH"),
            (u"\u027E", u"DX"),
            (u"p\u0258\u026A", u"PEY"),
            (u"p\u0258\u026Aw", u"PEYW"),
            (u"p\u0258\u026A\u0258\u026Aw", u"PEYEYW"),
            (u"p\u0258\u026A\u0251w", u"PEYAAW"),
            (u"\u006A\u0075", u"YUW"),
            (u"S\u006A\u0075", u"YUW"),
            (u"S\u006A\u0075\u02C8be", u"YUWBEH"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_ipa_string(IPAString(unicode_string=v, ignore=True), ignore=True), e)

    def test_map_unicode_string_single(self):
        mapper = ARPABETMapper()
        values = [
            (u"", u""),
            (u"p", u"P"),
            (u"p\u03B8", u"PTH"),
            (u"\u027E", u"DX"),
            (u"p\u0258\u026A", u"PEY"),
            (u"p\u0258\u026Aw", u"PEYW"),
            (u"p\u0258\u026A\u0258\u026Aw", u"PEYEYW"),
            (u"p\u0258\u026A\u0251w", u"PEYAAW"),
            (u"\u006A\u0075", u"YUW"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_unicode_string(v, single_char_parsing=True), e)




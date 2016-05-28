#!/usr/bin/env python
# coding=utf-8

import unittest

from ipapy.kirshenbaummapper import KirshenbaumMapper
from ipapy.ipastring import IPAString

class TestKirshenbaumMapper(unittest.TestCase):

    def test_can_map_ipa_string(self):
        mapper = KirshenbaumMapper()
        values = [
            (u"", True),
            (u"foo", True),
            (u"\u0070\u032A", True),
            (u"\u025F", True),
            (u"\u0294", True),
            (u"foo\u025F\u0294", True),
            (u"fo\u02C8o\u025F\u0294", True),
            (u"foo bar", True),
            (u"\u0261\u0067", True),
            (u"ma\u0272ana", True),
            (u"\u02A3", True),
            (u"\u02A7", True),
            (u"\u1DC6", False),       # valid IPA char, unmapped in Kirshenbaum
            (u"foo\u1DC6bar", False), # valid IPA char, unmapped in Kirshenbaum
        ]
        for v, e in values:
            self.assertEqual(mapper.can_map_ipa_string(IPAString(unicode_string=v)), e)

    def test_map_unicode_string(self):
        mapper = KirshenbaumMapper()
        values = [
            (None, None),
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_unicode_string(v), e)

    def test_map_ipa_string(self):
        mapper = KirshenbaumMapper()
        values = [
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_ipa_string(IPAString(unicode_string=v)), e)

    def test_map_unicode_string_ignore(self):
        mapper = KirshenbaumMapper()
        values = [
            (None, None),
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
            (u"L", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032AL", u"p["),
            (u"L\u025FM", u"J"),
            (u"L\u0294M", u"?"),
            (u"fLoo\u025F\u0294M", u"fooJ?"),
            (u"fo\u02C8oL\u025F\u0294M", u"fo'oJ?"),
            (u"fooL MbarN", u"foo#bar<trl>"),
            (u"\u0261L\u0067", u"gg"),
            (u"mLa\u0272Mana", u"man^ana"),
            (u"L\u02A3", u"dz"),
            (u"\u02A7M", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_unicode_string(v, ignore=True), e)

    def test_map_ipa_string_ignore(self):
        mapper = KirshenbaumMapper()
        values = [
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
            (u"L", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032AL", u"p["),
            (u"L\u025FM", u"J"),
            (u"L\u0294M", u"?"),
            (u"fLoo\u025F\u0294M", u"fooJ?"),
            (u"fo\u02C8oL\u025F\u0294M", u"fo'oJ?"),
            (u"fooL MbarN", u"foo#bar<trl>"),
            (u"\u0261L\u0067", u"gg"),
            (u"mLa\u0272Mana", u"man^ana"),
            (u"L\u02A3", u"dz"),
            (u"\u02A7M", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_ipa_string(IPAString(unicode_string=v, ignore=True), ignore=True), e)

    def test_map_unicode_string_single(self):
        mapper = KirshenbaumMapper()
        values = [
            (None, None),
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(mapper.map_unicode_string(v, single_char_parsing=True), e)




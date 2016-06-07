#!/usr/bin/env python
# coding=utf-8

import unittest

from ipapy import UNICODE_TO_IPA as U2I
from ipapy.ipachar import IPAChar
from ipapy.ipastring import IPAString

class TestIPAString(unittest.TestCase):

    def test_init_ipa_chars_bad(self):
        values = [
            1,
            u"",
            "",
            u"foo",
            "foo",
            {"k": "v"},
            [None],
            [1],
            [u""],
            [""],
            [u"foo"],
            ["foo"],
            [{"k": "v"}],
            [U2I[u"f"], None],
            ["f", U2I[u"o"], U2I[u"o"]],
        ]
        for v in values:
            with self.assertRaises(TypeError):
                IPAString(ipa_chars=v)

    def test_init_ipa_chars(self):
        values = [
            None,
            [],
            [U2I[u"f"]],
            [U2I[u"f"], U2I[u"o"], U2I[u"o"]],
        ]
        for v in values:
            IPAString(ipa_chars=v)

    def test_init_unicode_string(self):
        values = [
            None,
            u"",
            u"f",
            u"foo",
            u"\u0066\u02BCoo",
            u"f\u006e\u0361\u006doo",
        ]
        for v in values:
            IPAString(unicode_string=v)

    def test_init_unicode_string_bad(self):
        values = [
            b"",
            b"f",
            b"foo",
            b"\u0066\u02BCoo",
            b"f\u006e\u0361\u006doo",
            u"L",
            u"fL",
            u"fLooM",
            u"/\u0066\u02BCoo/",
            u"[f\u006e\u0361\u006doo]",
        ]
        for v in values:
            with self.assertRaises(ValueError):
                IPAString(unicode_string=v)

    def test_init_unicode_string_ignore(self):
        values = [
            u"L",
            u"fL",
            u"fLooM",
            u"/\u0066\u02BCoo/",
            u"[f\u006e\u0361\u006doo]",
        ]
        for v in values:
            IPAString(unicode_string=v, ignore=True)

    def test_init_unicode_len(self):
        values = [
            (None, 0),
            (u"", 0),
            (u"f", 1),
            (u"foo", 3),
            (u"\u0066\u02BCoo", 3),
            (u"f\u006e\u0361\u006doo", 4),
        ]
        for v, e in values:
            self.assertEqual(len(IPAString(unicode_string=v)), e)

    def test_init_unicode_single(self):
        values = [
            (None, 0),
            (u"", 0),
            (u"f", 1),
            (u"foo", 3),
            (u"\u0066\u02BCoo", 4),
            (u"f\u006e\u0361\u006doo", 6),
        ]
        for v, e in values:
            self.assertEqual(len(IPAString(unicode_string=v, single_char_parsing=True)), e)

    def test_ipa_chars_get(self):
        values = [
            (None, 0),
            (u"", 0),
            (u"f", 1),
            (u"foo", 3),
            (u"\u0066\u02BCoo", 3),
            (u"f\u006e\u0361\u006doo", 4),
        ]
        for v, e in values:
            self.assertEqual(len(IPAString(unicode_string=v).ipa_chars), e)

    def test_ipa_chars_set(self):
        IPAString().ipa_chars = [U2I[u"f"], U2I[u"o"], U2I[u"o"]]
        with self.assertRaises(TypeError):
            IPAString().ipa_chars = u"foo"
        with self.assertRaises(TypeError):
            IPAString().ipa_chars = [U2I[u"f"], None]
        with self.assertRaises(TypeError):
            IPAString().ipa_chars = [U2I[u"f"], u"o", u"o"]

    def test_add(self):
        values = [
            (None, None, 0),
            (None, u"a", 1),
            (u"a", None, 1),
            (u"a", u"b", 2),
            (u"f\u006e\u0361\u006doo", u"", 4),
            (u"f\u006e\u0361\u006doo", u"foo", 7),
        ]
        for v1, v2, e in values:
            self.assertEqual(len(IPAString(unicode_string=v1) + IPAString(unicode_string=v2)), e)

    def test_is_equivalent(self):
        values = [
            (None, None, True),
            (None, u"", True),
            (u"", None, True),
            (u"", u"", True),
            (u"f", u"f", True),
            (u"f\u006e\u0361\u006d", u"f\u006e\u0361\u006d", True),
            (u"f\u006e\u0361\u006d", u"f\u006e\u035C\u006d", True),
            (u"f\u006e\u0361\u006d", u"f\u006e\u006d", True),
            (u"\u0074\u0361\u026C", u"\u019B", True),
        ]
        for v1, v2, e in values:
            self.assertEqual(IPAString(unicode_string=v1).is_equivalent(IPAString(unicode_string=v2)), e)

    def test_is_equivalent_single(self):
        values = [
            (None, None, True),
            (None, u"", True),
            (u"", None, True),
            (u"", u"", True),
            (u"f", u"f", True),
            (u"f\u006e\u0361\u006d", u"f\u006e\u0361\u006d", True),
            (u"f\u006e\u0361\u006d", u"f\u006e\u035C\u006d", True),
            (u"f\u006e\u0361\u006d", u"f\u006e\u006d", True),
            (u"\u0074\u0361\u026C", u"\u019B", True),
        ]
        for v1, v2, e in values:
            self.assertEqual(IPAString(unicode_string=v1, single_char_parsing=True).is_equivalent(IPAString(unicode_string=v2)), e)

    def test_canonical_representation(self):
        values = [
            (None, 0),
            (u"", 0),
            (u"f", 1),
            (u"foo", 3),
            (u"\u0066\u02BCoo", 3),
            (u"f\u006e\u0361\u006doo", 4),
        ]
        for v, e in values:
            self.assertEqual(len(IPAString(unicode_string=v, single_char_parsing=True).canonical_representation), e)

    def test_filter_chars(self):
        s = u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"
        s_ipa = IPAString(unicode_string=s)
        values = [
            (None, s),
            ([], s),
            ({}, s),
            (u"", s),
            (u"foo", s),
            (u"bar", s),
            (0, s),
            (1, s),
            (u"cns", u"knknθld͡ʒ"),
            (u"consonants", u"knknθld͡ʒ"),
            (u"vwl", u"əiææɑəi"),
            (u"vowels", u"əiææɑəi"),
            (u"cns_vwl", u"əkinækænθɑləd͡ʒi"),
            (u"letters", u"əkinækænθɑləd͡ʒi"),
            (u"cns_vwl_pstr", u"əˈkinækænˈθɑləd͡ʒi"),
            (u"cvp", u"əˈkinækænˈθɑləd͡ʒi"),
            (u"cns_vwl_pstr_long", u"əˈkiːnækænˈθɑləd͡ʒi"),
            (u"cvpl", u"əˈkiːnækænˈθɑləd͡ʒi"),
            (u"cns_vwl_str", u"əˈkinæˌkænˈθɑləd͡ʒi"),
            (u"cvs", u"əˈkinæˌkænˈθɑləd͡ʒi"),
            (u"cns_vwl_str_len", u"əˈkiːnæˌkænˈθɑləd͡ʒi"),
            (u"cvsl", u"əˈkiːnæˌkænˈθɑləd͡ʒi"),
            (u"cns_vwl_str_len_wb", u"əˈkiːn æˌkænˈθɑləd͡ʒi"),
            (u"cvslw", u"əˈkiːn æˌkænˈθɑləd͡ʒi"),
            (u"cns_vwl_str_len_wb_sb", u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"),
            (u"cvslws", u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"),
        ]
        for v, e in values:
            self.assertTrue(s_ipa.filter_chars(v).is_equivalent(IPAString(unicode_string=e)))




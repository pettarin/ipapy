#!/usr/bin/env python
# coding=utf-8

import unittest

from ipapy import invalid_ipa_characters
from ipapy import ipa_substrings
from ipapy import is_valid_ipa
from ipapy import remove_invalid_ipa_characters
from ipapy import split_using_dictionary

class TestInit(unittest.TestCase):

    def do_test(self, values, func):
        for v, e in values:
            self.assertEqual(func(v), e)

    def test_ipa_substrings(self):
        values = [
            (None, None),
            (u"", []),
            (u"f", [u"f"]),
            (u"foo", [u"f", u"o", u"o"]),
            (u"\u0066\u02BCoo", [u"\u0066\u02BC", u"o", u"o"]),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", [u"f", u"\u031A", u"o", u"o"]),
            (u"f\u006e\u0361\u006doo", [u"f", u"\u006e\u0361\u006d", u"o", u"o"]), # single (\u006e + \u0361 + \u006d)
            (u"L", [u"L"]),
            (u"LfM", [u"L", u"f", u"M"]),
            (u"fLoMo", [u"f", u"L", u"o", u"M", u"o"]),
            (u"L\u0066\u02BCMoo", [u"L", u"\u0066\u02BC", u"M", u"o", u"o"]),
            (u"LfM\u02BCoo", [u"L", u"f", u"M", u"\u02BC", u"o", u"o"]),
            (u"fL\u031AMoo", [u"f", u"L", u"\u031A", u"M", u"o", u"o"]),
            (u"f\u006eL\u0361\u006doo", [u"f", u"\u006e", u"L", u"\u0361", u"\u006d", u"o", u"o"]),
        ]
        self.do_test(values, ipa_substrings)

    def test_ipa_substrings_single(self):
        values = [
            (None, None),
            (u"", []),
            (u"f", [u"f"]),
            (u"foo", [u"f", u"o", u"o"]),
            (u"\u0066\u02BCoo", [u"\u0066", u"\u02BC", u"o", u"o"]),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", [u"f", u"\u031A", u"o", u"o"]),
            (u"f\u006e\u0361\u006doo", [u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"]), # single (\u006e + \u0361 + \u006d)
            (u"L", ["L"]),
            (u"LfM", [u"L", u"f", u"M"]),
            (u"fLoMo", [u"f", u"L", u"o", u"M", u"o"]),
            (u"L\u0066\u02BCMoo", [u"L", u"\u0066", u"\u02BC", u"M", u"o", u"o"]),
            (u"LfM\u02BCoo", [u"L", u"f", u"M", u"\u02BC", u"o", u"o"]),
            (u"fL\u031AMoo", [u"f", u"L", u"\u031A", u"M", u"o", u"o"]),
            (u"f\u006eL\u0361\u006doo", [u"f", u"\u006e", u"L", u"\u0361", u"\u006d", u"o", u"o"]),
        ]
        for v, e in values:
            self.assertEqual(ipa_substrings(v, single_char_parsing=True), e)

    def test_invalid_ipa_characters(self):
        values = [
            (None, None),
            (u"", set([])),
            (u"foo", set([])),
            (u"L", set([u"L"])),
            (u"LfM", set([u"L", u"M"])),
            (u"fLoMo", set([u"L", u"M"])),
            (u"L\u0066\u02BCMoo", set([u"L", u"M"])),
            (u"LfM\u02BCoo", set([u"L", u"M"])),
            (u"fL\u031AMoo", set([u"L", u"M"])),
            (u"f\u006eL\u0361\u006doo", set([u"L"])),
        ]
        self.do_test(values, invalid_ipa_characters)

    def test_invalid_ipa_characters_indices(self):
        values = [
            (None, None),
            (u"", []),
            (u"foo", []),
            (u"L", [(0, u"L")]),
            (u"LfM", [(0, u"L"), (2, u"M")]),
            (u"fLoMo", [(1, u"L"), (3, u"M")]),
            (u"L\u0066\u02BCMoo", [(0, u"L"), (3, u"M")]),
            (u"LfM\u02BCoo", [(0, u"L"), (2, u"M")]),
            (u"fL\u031AMoo", [(1, u"L"), (3, u"M")]),
            (u"f\u006eL\u0361\u006doo", [(2, u"L")]),
        ]
        for v, e in values:
            self.assertEqual(invalid_ipa_characters(v, indices=True), e)

    def test_is_valid_ipa(self):
        values = [
            (None, None),
            (u"", True),
            (u"f", True),
            (u"foo", True),
            (u"\u0066\u02BCoo", True),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", True),
            (u"f\u006e\u0361\u006doo", True), # single (\u006e + \u0361 + \u006d)
            (u"L", False),
            (u"LfM", False),
            (u"fLoMo", False),
            (u"L\u0066\u02BCMoo", False),
            (u"LfM\u02BCoo", False),
            (u"fL\u031AMoo", False),
            (u"f\u006eL\u0361\u006doo", False),
        ]
        self.do_test(values, is_valid_ipa)

    def test_remove_invalid_ipa_characters(self):
        values = [
            (None, None),
            (u"", []),
            (u"f", [u"f"]),
            (u"foo", [u"f", u"o", u"o"]),
            (u"\u0066\u02BCoo", [u"\u0066\u02BC", u"o", u"o"]),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", [u"f", u"\u031A", u"o", u"o"]),
            (u"f\u006e\u0361\u006doo", [u"f", u"\u006e\u0361\u006d", u"o", u"o"]), # single (\u006e + \u0361 + \u006d)
            (u"L", []),
            (u"LfM", [u"f"]),
            (u"fLoMo", [u"f", u"o", u"o"]),
            (u"L\u0066\u02BCMoo", [u"\u0066\u02BC", u"o", u"o"]),
            (u"LfM\u02BCoo", [u"f", u"\u02BC", u"o", u"o"]),
            (u"fL\u031AMoo", [u"f", u"\u031A", u"o", u"o"]),
            (u"f\u006eL\u0361\u006doo", [u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"]),
        ]
        self.do_test(values, remove_invalid_ipa_characters)

    def test_remove_invalid_ipa_characters_single(self):
        values = [
            (None, None),
            (u"", []),
            (u"f", [u"f"]),
            (u"foo", [u"f", u"o", u"o"]),
            (u"\u0066\u02BCoo", [u"\u0066", u"\u02BC", u"o", u"o"]),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", [u"f", u"\u031A", u"o", u"o"]),
            (u"f\u006e\u0361\u006doo", [u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"]), # single (\u006e + \u0361 + \u006d)
            (u"L", []),
            (u"LfM", [u"f"]),
            (u"fLoMo", [u"f", u"o", u"o"]),
            (u"L\u0066\u02BCMoo", [u"\u0066", u"\u02BC", u"o", u"o"]),
            (u"LfM\u02BCoo", [u"f", u"\u02BC", u"o", u"o"]),
            (u"fL\u031AMoo", [u"f", u"\u031A", u"o", u"o"]),
            (u"f\u006eL\u0361\u006doo", [u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"]),
        ]
        for v, e in values:
            self.assertEqual(remove_invalid_ipa_characters(v, single_char_parsing=True), e)

    def test_remove_invalid_ipa_characters_invalid(self):
        values = [
            (None, None),
            (u"", ([], [])),
            (u"f", ([u"f"], [])),
            (u"foo", ([u"f", u"o", u"o"], [])),
            (u"\u0066\u02BCoo", ([u"\u0066\u02BC", u"o", u"o"], [])),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", ([u"f", u"\u031A", u"o", u"o"], [])),
            (u"f\u006e\u0361\u006doo", ([u"f", u"\u006e\u0361\u006d", u"o", u"o"], [])), # single (\u006e + \u0361 + \u006d)
            (u"L", ([], [u"L"])),
            (u"LfM", ([u"f"], [u"L", u"M"])),
            (u"fLoMo", ([u"f", u"o", u"o"], [u"L", u"M"])),
            (u"L\u0066\u02BCMoo", ([u"\u0066\u02BC", u"o", u"o"], [u"L", u"M"])),
            (u"LfM\u02BCoo", ([u"f", u"\u02BC", u"o", u"o"], [u"L", u"M"])),
            (u"fL\u031AMoo", ([u"f", u"\u031A", u"o", u"o"], [u"L", u"M"])),
            (u"f\u006eL\u0361\u006doo", ([u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"], [u"L"])),
        ]
        for v, e in values:
            self.assertEqual(remove_invalid_ipa_characters(v, return_invalid=True), e)

    def test_remove_invalid_ipa_characters_invalid_single(self):
        values = [
            (None, None),
            (u"", ([], [])),
            (u"f", ([u"f"], [])),
            (u"foo", ([u"f", u"o", u"o"], [])),
            (u"\u0066\u02BCoo", ([u"\u0066", u"\u02BC", u"o", u"o"], [])),     # single (\u0066 + \u02BC)
            (u"f\u031Aoo", ([u"f", u"\u031A", u"o", u"o"], [])),
            (u"f\u006e\u0361\u006doo", ([u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"], [])), # single (\u006e + \u0361 + \u006d)
            (u"L", ([], [u"L"])),
            (u"LfM", ([u"f"], [u"L", u"M"])),
            (u"fLoMo", ([u"f", u"o", u"o"], [u"L", u"M"])),
            (u"L\u0066\u02BCMoo", ([u"\u0066", u"\u02BC", u"o", u"o"], [u"L", u"M"])),
            (u"LfM\u02BCoo", ([u"f", u"\u02BC", u"o", u"o"], [u"L", u"M"])),
            (u"fL\u031AMoo", ([u"f", u"\u031A", u"o", u"o"], [u"L", u"M"])),
            (u"f\u006eL\u0361\u006doo", ([u"f", u"\u006e", u"\u0361", u"\u006d", u"o", u"o"], [u"L"])),
        ]
        for v, e in values:
            self.assertEqual(remove_invalid_ipa_characters(v, return_invalid=True, single_char_parsing=True), e)

    def test_split_using_dictionary(self):
        d = dict()
        d[u"a"] = 1
        d[u"ba"] = 2
        d[u"b"] = 3
        d[u"c"] = 4
        d[u"ca"] = 5
        values = [
            (None, None),
            (u"", []),
            (u"aza", [u"a", u"z", u"a"]),
            (u"aaba", [u"a", u"a", u"ba"]),
            (u"acaba", [u"a", u"ca", u"ba"]),
        ]
        for v, e in values:
            self.assertEqual(split_using_dictionary(v, d, 2, single_char_parsing=False), e)

    def test_split_using_dictionary_single(self):
        d = dict()
        d[u"a"] = 1
        d[u"ba"] = 2
        d[u"b"] = 3
        d[u"c"] = 4
        d[u"ca"] = 5
        values = [
            (None, None),
            (u"", []),
            (u"aza", [u"a", u"z", u"a"]),
            (u"aaba", [u"a", u"a", u"b", u"a"]),
            (u"acaba", [u"a", u"c", u"a", u"b", u"a"]),
        ]
        for v, e in values:
            self.assertEqual(split_using_dictionary(v, d, 2, single_char_parsing=True), e)

    def test_split_using_dictionary_key_one(self):
        d = dict()
        d[u"a"] = 1
        d[u"b"] = 2
        d[u"c"] = 4
        values = [
            (None, None),
            (u"", []),
            (u"aza", [u"a", u"z", u"a"]),
            (u"aaba", [u"a", u"a", u"b", u"a"]),
            (u"acaba", [u"a", u"c", u"a", u"b", u"a"]),
        ]
        for v, e in values:
            self.assertEqual(split_using_dictionary(v, d, 1, single_char_parsing=False), e)

    def test_split_using_dictionary_key_one_single(self):
        d = dict()
        d[u"a"] = 1
        d[u"b"] = 2
        d[u"c"] = 4
        values = [
            (None, None),
            (u"", []),
            (u"aza", [u"a", u"z", u"a"]),
            (u"aaba", [u"a", u"a", u"b", u"a"]),
            (u"acaba", [u"a", u"c", u"a", u"b", u"a"]),
        ]
        for v, e in values:
            self.assertEqual(split_using_dictionary(v, d, 1, single_char_parsing=True), e)




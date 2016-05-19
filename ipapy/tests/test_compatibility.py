#!/usr/bin/env python
# coding=utf-8

import sys
import unittest

from ipapy.compatibility import is_unicode_string
from ipapy.compatibility import to_unicode_string
from ipapy.compatibility import to_str
from ipapy.compatibility import int_to_unichr
from ipapy.compatibility import hex_to_unichr
from ipapy.compatibility import unicode_to_hex

PY2 = (sys.version_info[0] == 2)

class TestCompatibility(unittest.TestCase):

    def do_test(self, values, func):
        for v, e in values:
            self.assertEqual(func(v), e)

    def test_is_unicode_string(self):
        values = [
            (None, None),
            (u"", True),
            (b"", False),
            (u"foo", True),
            (b"foo", False),
        ]
        self.do_test(values, is_unicode_string)
        if PY2:
            self.assertFalse(is_unicode_string("foo"))
            self.assertTrue(is_unicode_string(u"foo"))
            self.assertFalse(is_unicode_string(b"foo"))
        else:
            self.assertTrue(is_unicode_string("foo"))
            self.assertTrue(is_unicode_string(u"foo"))
            self.assertFalse(is_unicode_string(b"foo"))

    def test_to_unicode_string(self):
        values = [
            (None, None),
            ("", u""),
            (u"", u""),
            (b"", u""),
            ("foo", u"foo"),
            (u"foo", u"foo"),
            (b"foo", u"foo"),
        ]
        self.do_test(values, to_unicode_string)

    def test_to_str(self):
        values = [
            (None, None),
            ("", ""),
            (u"", ""),
            ("foo", "foo"),
            (u"foo", "foo"),
        ]
        self.do_test(values, to_str)

    def test_int_to_unichr(self):
        values = [
            (97, u"a"),
            (771, u"\u0303"),
            (43981, u"\uABCD"),
            (1, u"\u0001"),
            (16, u"\u0010"),
            (256, u"\u0100"),
            (4096, u"\u1000"),
        ]
        self.do_test(values, int_to_unichr)

    def test_hex_to_unichr(self):
        values = [
            (None, None),
            (u"", None),
            ("", None),
            ("U+0061", u"a"),
            ("0061", u"a"),
            (u"0303", u"\u0303"),
            (u"ABCD", u"\uABCD"),
            (u"abcd", u"\uABCD"),
            ("1", u"\u0001"),
            ("10", u"\u0010"),
            ("100", u"\u0100"),
            ("0001", u"\u0001"),
            ("0010", u"\u0010"),
            ("0100", u"\u0100"),
            ("1000", u"\u1000"),
            ("U+0001", u"\u0001"),
            ("U+0010", u"\u0010"),
            ("U+0100", u"\u0100"),
            ("U+1000", u"\u1000"),
        ]
        self.do_test(values, hex_to_unichr)

    def test_unicode_to_hex(self):
        values = [
            (None, None),
            (u"", ""),
            ("", ""),
            (u"a", "U+0061"),
            ("a", "U+0061"),
            (u"ab", "U+0061 U+0062"),
            ("ab", "U+0061 U+0062"),
            (u"\u0303", "U+0303"),
            (u"\uABCD", "U+ABCD"),
            (u"\u0001", "U+0001"),
            (u"\u0010", "U+0010"),
            (u"\u0100", "U+0100"),
            (u"\u1000", "U+1000"),
        ]
        self.do_test(values, unicode_to_hex)











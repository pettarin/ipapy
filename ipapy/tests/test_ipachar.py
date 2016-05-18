#!/usr/bin/env python
# coding=utf-8

import os
import unittest

from ipapy.ipachar import IPAChar
from ipapy.ipachar import IPALetter
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipachar import IPADiacritic
from ipapy.ipachar import IPASuprasegmental
from ipapy.ipachar import IPATone
from ipapy.ipachar import flatten
from ipapy.ipachar import is_list_of_ipachars
from ipapy.ipachar import canonical_representation
from ipapy.ipachar import variant_to_list
from ipapy.ipachar import variant_to_frozenset

class TestIPAChar(unittest.TestCase):

    def create_generic(self, arg=None):
        cha = IPAChar(name=u"generic IPAChar", properties=u"foo_c")
        let = IPALetter(name="generic IPALetter", properties=u"foo_l")
        cns = IPAConsonant(name="generic IPAConsonant", properties=u"voiceless bilabial plosive")
        vwl = IPAVowel(name="generic IPAVowel", properties=u"close front unrounded")
        dia = IPADiacritic(name="generic IPADiacritic", properties=u"foo_d")
        sup = IPASuprasegmental(name="generic IPA", properties=u"foo_s")
        ton = IPATone(name="generic IPA", properties=u"foo_t")
        if arg == "cha":
            return cha
        elif arg == "let":
            return let
        elif arg == "cns":
            return cns
        elif arg == "vwl":
            return vwl
        elif arg == "dia":
            return dia
        elif arg == "sup":
            return sup
        elif arg == "ton":
            return ton
        return (cha, let, cns, vwl, dia, sup, ton)

    def test_constructor_no_property(self):
        with self.assertRaises(ValueError):
            c = IPAChar(name=u"generic IPAChar", properties=u"")

    def test_constructor(self):
        c = IPAChar(name=u"generic IPAChar", properties=u"consonant")

    def test_constructor_unknown_property(self):
        # OK to give an unknown property
        c = IPAChar(name=u"generic IPAChar", properties=u"foobarbaz")

    def test_get_properties(self):
        c = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        prop = c.properties
        self.assertTrue(len(prop) > 0)

    def test_set_properties_bad_type(self):
        c = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        for v in [
            None,
            1,
            {"k": "v"}
        ]:
            with self.assertRaises(TypeError):
                c.properties = v

    def test_set_properties_bad_empty(self):
        c = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        with self.assertRaises(ValueError):
            c.properties = u""

    def test_set_properties(self):
        c = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        c.properties = u"diacritic long" 

    def test_equal(self):
        c1 = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        c2 = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        self.assertFalse(c1 == c2)

    def test_is_equivalent(self):
        c1 = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        c2 = IPAChar(name=u"generic IPAChar", properties=u"consonant")
        self.assertTrue(c1.is_equivalent(c1))
        self.assertTrue(c2.is_equivalent(c2))
        self.assertTrue(c1.is_equivalent(c2))
        self.assertTrue(c2.is_equivalent(c1))

    def test_is_letter(self):
        expected = (False, True, True, True, False, False, False)
        for (obj, expected) in zip(self.create_generic(), expected):
            self.assertEqual(obj.is_letter, expected)

    def test_is_consonant(self):
        expected = (False, False, True, False, False, False, False)
        for (obj, expected) in zip(self.create_generic(), expected):
            self.assertEqual(obj.is_consonant, expected)

    def test_is_vowel(self):
        expected = (False, False, False, True, False, False, False)
        for (obj, expected) in zip(self.create_generic(), expected):
            self.assertEqual(obj.is_vowel, expected)

    def test_is_diacritic(self):
        expected = (False, False, False, False, True, False, False)
        for (obj, expected) in zip(self.create_generic(), expected):
            self.assertEqual(obj.is_diacritic, expected)

    def test_is_suprasegmental(self):
        expected = (False, False, False, False, False, True, False)
        for (obj, expected) in zip(self.create_generic(), expected):
            self.assertEqual(obj.is_suprasegmental, expected)

    def test_is_tone(self):
        expected = (False, False, False, False, False, False, True)
        for (obj, expected) in zip(self.create_generic(), expected):
            self.assertEqual(obj.is_tone, expected)

    def test_ipaconsonant_init_bad(self):
        for v in [
            None,
            u"consonant",
            u"voiceless",
            u"bilabial",
            u"plosive",
            u"voiceless bilabial",
            u"voiceless plosive",
            u"bilabial plosive"
        ]:
            with self.assertRaises(ValueError):
                c = IPAConsonant(name="mycns", properties=v) 

    def test_ipaconsonant_init_bad_2(self):
        for v, p, m in [
            (None, None, None),
            (u"voiceless", None, None),
            (None, u"bilabial", None),
            (None, None, u"plosive"),
            (u"voiceless", u"bilabial", None),
            (u"voiceless", None, u"plosive"),
            (None, u"bilabial", u"plosive"),
        ]:
            with self.assertRaises(ValueError):
                c = IPAConsonant(name="mycns", voicing=v, place=p, manner=m) 

    def test_ipaconsonant_properties(self):
        cns = self.create_generic("cns")
        self.assertEqual(cns.properties, frozenset(["voiceless", "bilabial", "plosive", "consonant"]))

    def test_ipaconsonant_properties_set(self):
        cns = self.create_generic("cns")
        for v in [
            u"voiced bilabial plosive",
            u"voiced bilabial plosive consonant",
            [u"voiced", u"bilabial", u"plosive"],
            [u"voiced", u"bilabial", u"plosive", u"consonant"],
            set([u"voiced", u"bilabial", u"plosive"]),
            set([u"voiced", u"bilabial", u"plosive", u"consonant"]),
            frozenset([u"voiced", u"bilabial", u"plosive"]),
            frozenset([u"voiced", u"bilabial", u"plosive", u"consonant"]),
        ]:
            cns.properties = v
            self.assertEqual(cns.properties, frozenset(["voiced", "bilabial", "plosive", "consonant"]))

    def test_ipaconsonant_properties_set_bad(self):
        cns = self.create_generic("cns")
        for v in [
            None,
            1,
            {"k": "v"},
            u"voiced",
            u"consonant",
            u"voiceless",
            u"bilabial",
            u"plosive",
            u"voiceless bilabial",
            u"voiceless plosive",
            u"bilabial plosive"
        ]:
            with self.assertRaises((ValueError, TypeError)):
                cns.properties = v

    def test_ipaconsonant_voicing(self):
        cns = self.create_generic("cns")
        self.assertEqual(cns.voicing, "voiceless")
        cns.voicing = "voiced"
        cns.voicing = "vcd"
        with self.assertRaises(ValueError):
            cns.voicing = "foo"

    def test_ipaconsonant_place(self):
        cns = self.create_generic("cns")
        self.assertEqual(cns.place, "bilabial")
        cns.place = "alveolar"
        cns.place = "alv"
        with self.assertRaises(ValueError):
            cns.place = "foo"

    def test_ipaconsonant_manner(self):
        cns = self.create_generic("cns")
        self.assertEqual(cns.manner, "plosive")
        cns.manner = "nasal"
        cns.manner = "nas"
        with self.assertRaises(ValueError):
            cns.manner = "foo"







    def test_is_list_of_ipachars(self):
        cha, let, cns, vwl, dia, sup, ton = self.create_generic()
        values = [
            (None, False),
            ([], True),
            ([1, 2, 3], False),
            ([cha, let, 3], False),
            ([cha], True),
            ([cha, let], True),
            (["consonant"], False),
        ]
        for v, e in values:
            self.assertEqual(is_list_of_ipachars(v), e)

    def test_variant_to_list(self):
        values = [
            ([], []),
            (set([]), []),
            (frozenset([]), []),
            ([u"a", u"b", "c"], [u"a", u"b", u"c"]),
            (u"a b c", [u"a", u"b", u"c"]),
            (set([u"a", u"b", u"c"]), list(set([u"a", u"b", u"c"]))),
            (frozenset([u"a", u"b", u"c"]), list(frozenset([u"a", u"b", u"c"]))),
        ]
        for v, e in values:
            self.assertEqual(variant_to_list(v), e)

    def test_variant_to_list_bad(self):
        values = [
            None,
            {"k": "v"}
        ]
        for v in values:
            with self.assertRaises(TypeError):
                variant_to_list(v)

    def test_variant_to_frozenset(self):
        values = [
            ([], frozenset([])),
            (set([]), frozenset([])),
            (frozenset([]), frozenset([])),
            ([u"a", u"b", "c"], frozenset([u"a", u"b", u"c"])),
            (u"a b c", frozenset([u"a", u"b", u"c"])),
            (set([u"a", u"b", u"c"]), frozenset([u"a", u"b", u"c"])),
            (frozenset([u"a", u"b", u"c"]), frozenset([u"a", u"b", u"c"])),
        ]
        for v, e in values:
            self.assertEqual(variant_to_frozenset(v), e)

    def test_variant_to_frozenset_bad(self):
        values = [
            None,
            {"k": "v"}
        ]
        for v in values:
            with self.assertRaises(TypeError):
                variant_to_frozenset(v)

    def test_canonical_representation(self):
        values = [
            ([], frozenset([])),
            ([u"c", u"a", "b"], frozenset([u"a", u"b", u"c"])),
        ]
        for v, e in values:
            self.assertEqual(canonical_representation(v), e)

    def test_canonical_representation_bad(self):
        values = [
            set([]),
            frozenset([]),
            u"c a b",
        ]
        for v in values:
            with self.assertRaises(TypeError):
                canonical_representation(v)


    def test_flatten(self):
        values = [
            ([["a"]], ["a"]),
            ([["a", "b"]], ["a", "b"]),
            ([["a"], ["b"]], ["a", "b"]),
            ([["a"], ["b", "c"]], ["a", "b", "c"]),
        ]
        for v, e in values:
            self.assertEqual(flatten(v), e)

    def test_flatten_bad_not_list(self):
        values = [
            None,
            1,
            u"b",
            "b",
            set(["b"]),
            frozenset(["b"]),
            {"k": "v"}
        ]
        for v in values:
            with self.assertRaises(TypeError):
                flatten(v)

    def test_flatten_bad_not_list_of_lists(self):
        values = [
            [None],
            [1],
            [u"b"],
            ["b"],
            set(["b"]),
            frozenset(["b"]),
            {"k": "v"},
            [["a"], None],
            [["a"], 1],
            [["a"], "b"],
            [["a"], set(["b"])],
            [["a"], frozenset(["b"])],
            [["a"], {"k": "v"}]
        ]
        for v in values:
            with self.assertRaises(TypeError):
                flatten(v)




#!/usr/bin/env python
# coding=utf-8

import unittest

from ipapy.ipachar import D_D_MORE_ROUNDED
from ipapy.ipachar import D_D_VELARIZED
from ipapy.ipachar import IPAChar
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPADescriptor
from ipapy.ipachar import IPADescriptorGroup
from ipapy.ipachar import IPADiacritic
from ipapy.ipachar import IPALetter
from ipapy.ipachar import IPASuprasegmental
from ipapy.ipachar import IPATone
from ipapy.ipachar import IPAVowel
from ipapy.ipachar import is_list_of_ipachars
from ipapy.ipachar import variant_to_canonical_string
from ipapy.ipachar import variant_to_list

class TestIPADescriptor(unittest.TestCase):

    def test_init(self):
        d = IPADescriptor([u"foo", u"bar"])

    def test_init_bad(self):
        values = [
            None,
            [],
            "foo",
            u"foo",
            {"k": "v"},
        ]
        for v in values:
            with self.assertRaises((TypeError, ValueError)):
                d = IPADescriptor(v)
    
    def test_canonical_label_get(self):
        d = IPADescriptor([u"foo", u"bar"])
        self.assertEqual(d.canonical_label, u"foo")

    def test_canonical_label_set(self):
        d = IPADescriptor([u"foo", u"bar"])
        with self.assertRaises(ValueError):
            d.canonical_label = u"bar"

    def test_labels_get(self):
        d = IPADescriptor([u"foo", u"bar"])
        self.assertEqual(d.labels, [u"foo", u"bar"])

    def test_labels_set(self):
        d = IPADescriptor([u"foo", u"bar"])
        with self.assertRaises(ValueError):
            d.labels = set([u"bar"])

    def test_in(self):
        d = IPADescriptor([u"foo", u"bar"])
        self.assertTrue(u"foo" in d)
        self.assertTrue(u"bar" in d)
        self.assertTrue("foo" in d)
        self.assertTrue("bar" in d)

class TestIPADescriptorGroup(unittest.TestCase):

    def create_group(self):
        d1 = IPADescriptor([u"foo", u"bar"])
        d2 = IPADescriptor([u"baz"])
        d3 = IPADescriptor([u"foobarbaz"])
        return IPADescriptorGroup([d1, d2, d3])

    def test_init(self):
        g = self.create_group()

    def test_init_bad(self):
        values = [
            None,
            [],
            "foo",
            u"foo",
            {"k": "v"},
            [None],
            [[]],
            ["foo"],
            [u"foo"],
            [{"k": "v"}],
        ]
        for v in values:
            with self.assertRaises((TypeError, ValueError)):
                d = IPADescriptorGroup(v)

    def test_descriptors_get(self):
        g = self.create_group()
        self.assertTrue(isinstance(g.descriptors, list))
        self.assertEqual(len(g.descriptors), 3)

    def test_descriptors_set(self):
        g = self.create_group()
        with self.assertRaises(ValueError):
            g.descriptors = None
    
    def test_in(self):
        g = self.create_group()
        self.assertTrue(u"foo" in g)
        self.assertTrue(u"bar" in g)
        self.assertTrue(u"baz" in g)
        self.assertTrue(u"foobarbaz" in g)
        self.assertTrue("foo" in g)
        self.assertTrue("bar" in g)
        self.assertTrue("baz" in g)
        self.assertTrue("foobarbaz" in g)

    def test_canonical_value(self):
        g = self.create_group()
        self.assertEqual(g.canonical_value(u"foo"), u"foo")
        self.assertEqual(g.canonical_value(u"foo"), "foo")
        self.assertEqual(g.canonical_value("foo"), u"foo")
        self.assertEqual(g.canonical_value(u"bar"), u"foo")
        self.assertEqual(g.canonical_value(u"bar"), "foo")
        self.assertEqual(g.canonical_value("bar"), u"foo")
        self.assertEqual(g.canonical_value(u"baz"), u"baz")
        self.assertEqual(g.canonical_value(u"baz"), "baz")
        self.assertEqual(g.canonical_value("baz"), u"baz")
        self.assertEqual(g.canonical_value(u"bazbazbaz"), None)
        self.assertEqual(g.canonical_value("bazbazbaz"), None)

    def test_add(self):
        g1 = self.create_group()
        g2 = IPADescriptorGroup([IPADescriptor([u"foobar"])])
        g = g1 + g2
        self.assertNotEqual(g, g1)
        self.assertNotEqual(g, g2)
        self.assertTrue(u"foo" in g)
        self.assertTrue(u"bar" in g)
        self.assertTrue(u"baz" in g)
        self.assertTrue(u"foobar" in g)
        self.assertEqual(len(g), len(g1) + len(g2))



class TestIPAChar(unittest.TestCase):

    def create_generic(self, arg=None):
        cha = IPAChar(name=u"generic IPAChar", descriptors=u"foo_c")
        let = IPALetter(name="generic IPALetter", descriptors=u"foo_l")
        cns = IPAConsonant(name="generic IPAConsonant", descriptors=u"voiceless bilabial plosive")
        vwl = IPAVowel(name="generic IPAVowel", descriptors=u"close front unrounded")
        dia = IPADiacritic(name="generic IPADiacritic", descriptors=u"foo_d")
        sup = IPASuprasegmental(name="generic IPA", descriptors=u"foo_s")
        ton = IPATone(name="generic IPA", descriptors=u"foo_t")
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
            c = IPAChar(name=u"generic IPAChar", descriptors=u"")

    def test_constructor(self):
        c = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")

    def test_constructor_unknown_property(self):
        # OK to give an unknown property
        c = IPAChar(name=u"generic IPAChar", descriptors=u"foobarbaz")

    def test_get_descriptors(self):
        c = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        prop = c.descriptors
        self.assertTrue(len(prop) > 0)

    def test_set_descriptors_bad_type(self):
        c = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        for v in [
            None,
            1,
            {"k": "v"}
        ]:
            with self.assertRaises(TypeError):
                c.descriptors = v

    def test_set_descriptors_bad_empty(self):
        c = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        with self.assertRaises(ValueError):
            c.descriptors = u""

    def test_set_descriptors(self):
        c = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        c.descriptors = u"diacritic long" 

    def test_equal(self):
        c1 = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        c2 = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        self.assertFalse(c1 == c2)

    def test_is_equivalent(self):
        c1 = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
        c2 = IPAChar(name=u"generic IPAChar", descriptors=u"consonant")
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
                c = IPAConsonant(name="mycns", descriptors=v) 

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

    def test_ipaconsonant_descriptors(self):
        cns = self.create_generic("cns")
        self.assertEqual(cns.descriptors, ["consonant", "voiceless", "bilabial", "plosive"])

    def test_ipaconsonant_descriptors_set(self):
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
            cns.descriptors = v
            self.assertEqual(cns.descriptors, ["consonant", "voiced", "bilabial", "plosive"])

    def test_ipaconsonant_descriptors_set_bad(self):
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
                cns.descriptors = v

    def test_ipaconsonant_modifiers(self):
        cns = self.create_generic("cns")
        self.assertEqual(cns.modifiers, [])
        cns = IPAConsonant(name="mycns", voicing="voiceless", place="bilabial", manner="plosive", modifiers=["velarized"])
        self.assertEqual(cns.modifiers, ["velarized"])
        self.assertTrue(cns.has_descriptor(D_D_VELARIZED))

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

    def test_ipavowel_init_bad(self):
        for v in [
            None,
            u"vowel",
            u"close",
            u"front",
            u"unrounded",
            u"close front",
            u"close unrounded",
            u"front unrounded"
        ]:
            with self.assertRaises(ValueError):
                c = IPAVowel(name="myvwl", descriptors=v) 

    def test_ipavowel_init_bad_2(self):
        for h, b, r in [
            (None, None, None),
            (u"close", None, None),
            (None, u"front", None),
            (None, None, u"unrounded"),
            (u"close", u"front", None),
            (u"close", None, u"unrounded"),
            (None, u"front", u"unrounded"),
        ]:
            with self.assertRaises(ValueError):
                c = IPAVowel(name="myvwl", height=h, backness=b, roundness=r) 

    def test_ipavowel_descriptors(self):
        vwl = self.create_generic("vwl")
        self.assertEqual(vwl.descriptors, ["vowel", "close", "front", "unrounded"])

    def test_ipavowel_descriptors_set(self):
        vwl = self.create_generic("vwl")
        for v in [
            u"open front unrounded",
            u"open front unrounded vowel",
            [u"open", u"front", u"unrounded"],
            [u"open", u"front", u"unrounded", u"vowel"],
            set([u"open", u"front", u"unrounded"]),
            set([u"open", u"front", u"unrounded", u"vowel"]),
            frozenset([u"open", u"front", u"unrounded"]),
            frozenset([u"open", u"front", u"unrounded", u"vowel"]),
        ]:
            vwl.descriptors = v
            self.assertEqual(vwl.descriptors, ["vowel", "open", "front", "unrounded"])

    def test_ipavowel_descriptors_set_bad(self):
        vwl = self.create_generic("vwl")
        for v in [
            None,
            1,
            {"k": "v"},
            u"voiced",
            u"vowel",
            u"open",
            u"front",
            u"unrounded",
            u"open front",
            u"open unrounded",
            u"front unrounded"
        ]:
            with self.assertRaises((ValueError, TypeError)):
                vwl.descriptors = v

    def test_ipaconsonant_modifiers(self):
        vwl = self.create_generic("vwl")
        self.assertEqual(vwl.modifiers, [])
        vwl = IPAVowel(name="myvwl", height="open", backness="front", roundness="unrounded", modifiers=["more-rounded"]) 
        self.assertEqual(vwl.modifiers, ["more-rounded"])
        self.assertTrue(vwl.has_descriptor(D_D_MORE_ROUNDED))

    def test_ipavowel_height(self):
        vwl = self.create_generic("vwl")
        self.assertEqual(vwl.height, "close")
        vwl.height = "open"
        vwl.height = "low"
        with self.assertRaises(ValueError):
            vwl.height = "foo"

    def test_ipavowel_backness(self):
        vwl = self.create_generic("vwl")
        self.assertEqual(vwl.backness, "front")
        vwl.backness = "back"
        vwl.backness = "bck"
        with self.assertRaises(ValueError):
            vwl.backness = "foo"

    def test_ipavowel_roundness(self):
        vwl = self.create_generic("vwl")
        self.assertEqual(vwl.roundness, "unrounded")
        vwl.roundness = "rounded"
        vwl.roundness = "rnd"
        with self.assertRaises(ValueError):
            vwl.roundness = "foo"

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

    def test_variant_to_canonical_string(self):
        values = [
            ([], u""),
            (set([]), u""),
            (frozenset([]), u""),
            ([u"a", u"b", "c"], u""),
            (u"a b c", u""),
            (set([u"a", u"b", u"c"]), u""),
            (frozenset([u"a", u"b", u"c"]), u""),
            (u"consonant", u"consonant"),
            (u"bilabial consonant", u"bilabial consonant"),
            (u"consonant bilabial", u"bilabial consonant"),
            (u"voiceless bilabial plosive consonant", u"bilabial consonant plosive voiceless"),
            (u"voiceless bilabial plosive consonant velarized", u"bilabial consonant plosive velarized voiceless"),
            (u"voiceless bilabial plosive consonant nasalized", u"bilabial consonant nasalized plosive voiceless"),
            (u"vls blb stp cns", u"bilabial consonant plosive voiceless"),
            (u"suprasegmental long", u"long suprasegmental"),
            (u"suprasegmental primary-stress", u"primary-stress suprasegmental"),
        ]
        for v, e in values:
            self.assertEqual(variant_to_canonical_string(v), e)

    def test_variant_to_canonical_string_bad(self):
        values = [
            None,
            {"k": "v"}
        ]
        for v in values:
            with self.assertRaises(TypeError):
                variant_to_canonical_string(v)



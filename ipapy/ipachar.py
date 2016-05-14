#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

# types
T_CONSONANT = ["consonant", "cns"]
T_VOWEL = ["vowel", "vwl"]
T_DIACRITIC = ["diacritic", "dia"]
T_SUPRASEGMENTAL = ["suprasegmental", "sup"]
T_TONE = ["tone", "ton"]

# consonants and diacritics
D_ADVANCED = ["advanced"]
D_ADVANCED_TONGUE_ROOT = ["advanced-tongue-root"]
D_AFFRICATE = ["affricate"]
D_ALVEOLAR = ["alveolar", "alv"]
D_ALVEOLOPALATAL = ["alveolo-palatal"]
D_APICAL = ["apical"]
D_APPROXIMANT = ["approximant", "apr"]
D_ASPIRATED = ["aspirated", "asp"]
D_BILABIAL = ["bilabial", "blb"]
D_BREATHY_VOICED = ["breathy-voiced"]
D_CENTRALIZED = ["centralized"]
D_CLICK = ["click", "clk"]
D_CREAKY_VOICED = ["creaky-voiced"]
D_DENTAL = ["dental", "dnt"]
D_DENTAL_ALVEOLAR = ["dental-alveolar"]
D_EJECTIVE = ["ejective", "ejc"]
D_EPIGLOTTAL = ["epiglottal"]
D_FLAP = ["flap", "flp"]
D_FRICATIVE = ["fricative", "frc"]
D_GLOTTAL = ["glottal", "glt"]
D_IMPLOSIVE = ["implosive", "imp"]
D_LABIALIZED = ["labialized", "lzd"]
D_LABIAL_PALATAL = ["labial-palatal"]
D_LABIAL_VELAR = ["labial-velar"]
D_LABIODENTAL = ["labiodental", "labio-dental", "lbd"]
D_LAMINAL = ["laminal"]
D_LATERAL = ["lateral", "lat"]
D_LATERAL_RELEASE = ["lateral-release"]
D_LESS_ROUNDED = ["less-rounded"]
D_LINGUOLABIAL = ["linguolabial"]
D_LOWERED = ["lowered"]
D_MID_CENTRALIZED = ["mid-centralized"]
D_MORE_ROUNDED = ["more-rounded"]
D_NASAL = ["nasal", "nas"]
D_NASALIZED = ["nasalized"]
D_NASAL_RELEASE = ["nasal-release"]
D_NON_SYLLABIC = ["non-syllabic"]
D_NO_AUDIBLE_RELEASE = ["no-audible-release"]
D_PALATAL = ["palatal", "pal"]
D_PALATALIZED = ["palatalized", "pzd"]
D_PALATO_ALVEOLAR = ["palato-alveolar"]
D_PHARYNGEAL = ["pharyngeal", "phr"]
D_PHARYNGEALIZED = ["pharyngealized", "fzd"]
D_PLOSIVE = ["plosive", "stp"]
D_POSTALVEOLAR = ["postalveolar", "palato-alveolar", "pla"]
D_RAISED = ["raised"]
D_RETRACTED = ["retracted"]
D_RETRACTED_TONGUE_ROOT = ["retracted-tongue-root"]
D_RETROFLEX = ["retroflex", "rfx"]
D_RHOTACIZED = ["rhotacized", "rzd"]
D_STOP = ["stop"]
D_SYLLABIC = ["syllabic", "syl"]
D_TAP = ["tap"]
D_TIE_BAR_ABOVE = ["tie-bar-above"]
D_TIE_BAR_BELOW = ["tie-bar-below"]
D_TRILL = ["trill", "trl"]
D_UNEXPLODED = ["unexploded"]
D_UVULAR = ["uvular", "uvl"]
D_VELAR = ["velar", "vel"]
D_VELARIZED = ["velarized", "vzd"]
D_VELARIZED_OR_PHARYNGEALIZED = ["velarized-or-pharyngealized"]
D_VOICED = ["voiced", "vcd"]
D_VOICELESS = ["voiceless", "vls"]

# consonants
G_VOICING = [
    D_VOICED,
    D_VOICELESS
]

# vowels
V_CLOSE = ["close", "high", "hgh"]
V_LOWERED_CLOSE = ["lowered-close", "semi-high", "smh"]
V_CLOSE_MID = ["close-mid", "upper-mid", "umd"]
V_MID = ["mid"]
V_OPEN_MID = ["open-mid", "lower-mid", "lmd"]
V_RAISED_OPEN = ["raised-open", "semi-low", "slw"]
V_OPEN = ["open", "low"]
G_HEIGHT = [
    V_CLOSE,
    V_LOWERED_CLOSE,
    V_CLOSE_MID,
    V_MID,
    V_OPEN_MID,
    V_RAISED_OPEN,
    V_OPEN,
]

V_FRONT = ["front", "fnt"]
V_CENTER = ["central", "center", "cnt"]
V_BACK = ["back", "bck"]
G_BACKNESS = [
    V_FRONT,
    V_CENTER,
    V_BACK,
]
G_BACKNESS_MODIFIERS = [
    D_ADVANCED,
    D_RETRACTED,
    D_CENTRALIZED,
    D_MID_CENTRALIZED,
]

V_ROUNDED = ["rounded", "rnd"]
V_UNROUNDED = ["unrounded", "unr"]
G_ROUNDNESS = [
    V_ROUNDED,
    V_UNROUNDED,
]
G_ROUNDNESS_MODIFIERS = [
    D_MORE_ROUNDED,
    D_LESS_ROUNDED
]

# suprasegmental
S_PRIMARY_STRESS = ["primary-stress"]
S_SECONDARY_STRESS = ["secondary-stress"]
S_LONG = ["long", "lng"]
S_HALF_LONG = ["half-long"]
S_EXTRA_SHORT = ["extra-short"]
S_MINOR_GROUP = ["minor-group"]
S_MAJOR_GROUP = ["major-group"]
S_SYLLABLE_BREAK = ["syllable-break"]
S_LINKING = ["linking"]
S_WORD_BREAK = ["word-break"]
G_STRESS = [
    S_PRIMARY_STRESS,
    S_SECONDARY_STRESS
]
G_LENGTH = [
    S_LONG,
    S_HALF_LONG,
    S_EXTRA_SHORT
]

G_ALL_PROPERTIES = [
    T_CONSONANT,
    T_VOWEL,
    T_DIACRITIC,
    T_SUPRASEGMENTAL,
    T_TONE,
    D_ADVANCED,
    D_ADVANCED_TONGUE_ROOT,
    D_AFFRICATE,
    D_ALVEOLAR,
    D_ALVEOLOPALATAL,
    D_APICAL,
    D_APPROXIMANT,
    D_ASPIRATED,
    D_BILABIAL,
    D_BREATHY_VOICED,
    D_CENTRALIZED,
    D_CLICK,
    D_CREAKY_VOICED,
    D_DENTAL,
    D_DENTAL_ALVEOLAR,
    D_EJECTIVE,
    D_EPIGLOTTAL,
    D_FLAP,
    D_FRICATIVE,
    D_GLOTTAL,
    D_IMPLOSIVE,
    D_LABIALIZED,
    D_LABIAL_PALATAL,
    D_LABIAL_VELAR,
    D_LABIODENTAL,
    D_LAMINAL,
    D_LATERAL,
    D_LATERAL_RELEASE,
    D_LESS_ROUNDED,
    D_LINGUOLABIAL,
    D_LOWERED,
    D_MID_CENTRALIZED,
    D_MORE_ROUNDED,
    D_NASAL,
    D_NASALIZED,
    D_NASAL_RELEASE,
    D_NON_SYLLABIC,
    D_NO_AUDIBLE_RELEASE,
    D_PALATAL,
    D_PALATALIZED,
    D_PALATO_ALVEOLAR,
    D_PHARYNGEAL,
    D_PHARYNGEALIZED,
    D_PLOSIVE,
    D_POSTALVEOLAR,
    D_RAISED,
    D_RETRACTED,
    D_RETRACTED_TONGUE_ROOT,
    D_RETROFLEX,
    D_RHOTACIZED,
    D_STOP,
    D_SYLLABIC,
    D_TAP,
    D_TIE_BAR_ABOVE,
    D_TIE_BAR_BELOW,
    D_TRILL,
    D_UNEXPLODED,
    D_UVULAR,
    D_VELAR,
    D_VELARIZED,
    D_VELARIZED_OR_PHARYNGEALIZED,
    D_VOICED,
    D_VOICELESS,
    V_CLOSE,
    V_LOWERED_CLOSE,
    V_CLOSE_MID,
    V_MID,
    V_OPEN_MID,
    V_RAISED_OPEN,
    V_OPEN,
    V_FRONT,
    V_CENTER,
    V_BACK,
    V_ROUNDED,
    V_UNROUNDED,
    S_PRIMARY_STRESS,
    S_SECONDARY_STRESS,
    S_LONG,
    S_HALF_LONG,
    S_EXTRA_SHORT,
    S_MINOR_GROUP,
    S_MAJOR_GROUP,
    S_SYLLABLE_BREAK,
    S_LINKING,
    S_WORD_BREAK,
]

def canonical_representation(properties):
    """
    Return the canonical representation of a list of properties,
    that is, a frozenset built from properties.

    :param list properties: a list of properties
    :rtype: frozenset
    """
    return frozenset(sorted(properties))

class IPAChar(object):
    TAG = "IPAChar"
    
    def __init__(self, name, properties, unicode_char=None):
        self.name = name
        if isinstance(properties, set):
            self.properties = frozenset(properties)
        elif isinstance(properties, list):
            self.properties = frozenset(properties)
        else:
            self.properties = frozenset(properties.split())
        self.unicode_char = unicode_char

    def __eq__(self, other):
        return self.properties == other.properties

    def __str__(self):
        return self.unicode_char
    
    def __unicode__(self):
        return self.unicode_char

    def __repr__(self):
        return "%s (%s)" % (self.name, str(self.properties))

    @property
    def is_vowel(self):
        return False

    @property
    def is_consonant(self):
        return False

    @property
    def is_diacritic(self):
        return False

    @property
    def is_suprasegmental(self):
        return False

    @property
    def is_tone(self):
        return False

    def has_property(self, descriptors):
        for d in descriptors:
            if d in self.properties:
                return True
        return False

    @property
    def canonical_representation(self):
        acc = []
        for a in G_ALL_PROPERTIES:
            for p in self.properties:
                if p in a:
                    acc.append(a[0])
        return canonical_representation(acc)

    def alternative_property(self, alternatives, modifiers=None):
        if modifiers is None:
            for a in alternatives:
                if self.has_property(a):
                    return a[0]
            return None
        else:
            value, modifier = None, None
            for a in alternatives:
                if self.has_property(a):
                    value = a[0]
                    break
            for m in modifiers:
                if self.has_property(m):
                    modifier = m[0]
                    break
            return (value, modifier)



class IPADiacritic(IPAChar):
    TAG = "IPADiacritic"
    
    @property
    def is_diacritic(self):
        return True



class IPASuprasegmental(IPAChar):
    TAG = "IPASuprasegmental"
    
    @property
    def is_suprasegmental(self):
        return True

    @property
    def stress(self):
        return self.alternative_property(G_STRESS)

    @property
    def length(self):
        return self.alternative_property(G_LENGTH)

    @property
    def is_syllable_break(self):
        return self.has_property(S_SYLLABLE_BREAK)

    @property
    def is_word_break(self):
        return self.has_property(S_WORD_BREAK)

    def is_char_of_type(self, query):
        for c in query:
            if (c == "s") and (self.stress is not None):
                return True
            elif (c == "l") and (self.length is not None):
                return True
            elif (c == "w") and (self.is_word_break):
                return True
        return False



class IPATone(IPAChar):
    TAG = "IPATone"
    
    @property
    def is_tone(self):
        return True



class IPAPhone(IPAChar):
    TAG = "IPAPhone"



class IPAConsonant(IPAPhone):
    TAG = "IPAConsonant"
   
    @property
    def is_consonant(self):
        return True

    @property
    def is_voiced(self):
        return self.has_property(C_VOICED)

    @property
    def is_voiceless(self):
        return self.has_property(C_VOICELESS)



class IPAVowel(IPAPhone):
    TAG = "IPAVowel"
       
    @property
    def is_vowel(self):
        return True

    @property
    def height(self):
        return self.alternative_property(G_HEIGHT)
    
    @property
    def is_close(self):
        return self.has_property(V_CLOSE)

    @property
    def is_lowered_close(self):
        return self.has_property(V_LOWERED_CLOSE)

    @property
    def is_close_mid(self):
        return self.has_property(V_CLOSE_MID)

    @property
    def is_mid(self):
        return self.has_property(V_MID)

    @property
    def is_open_mid(self):
        return self.has_property(V_OPEN_MID)

    @property
    def is_raised_open(self):
        return self.has_property(V_RAISED_OPEN)

    @property
    def is_open(self):
        return self.has_property(V_OPEN)

    @property
    def backness(self):
        return self.alternative_property(G_BACKNESS)

    @property
    def backness_modifier(self):
        return self.alternative_property(G_BACKNESS, G_BACKNESS_MODIFIERS)

    @property
    def is_front(self):
        return self.has_property(V_FRONT)

    @property
    def is_center(self):
        return self.has_property(V_CENTER)

    @property
    def is_back(self):
        return self.has_property(V_BACK)

    @property
    def is_advanced(self):
        return self.has_property(V_ADVANCED)

    @property
    def is_retracted(self):
        return self.has_property(V_RETRACTED)

    @property
    def is_centralized(self):
        return self.has_property(V_CENTRALIZED)

    @property
    def is_mid_centralized(self):
        return self.has_property(V_MID_CENTRALIZED)

    @property
    def roundness(self):
        return self.alternative_property(G_ROUNDNESS)
    
    @property
    def roundness_modifier(self):
        return self.alternative_property(G_ROUNDNESS, G_ROUNDNESS_MODIFIERS)
    
    @property
    def is_rounded(self):
        return self.has_property(V_ROUNDED)

    @property
    def is_unrounded(self):
        return self.has_property(V_UNROUNDED)

    @property
    def is_more_rounded(self):
        return self.has_property(V_MORE_ROUNDED)

    @property
    def is_less_rounded(self):
        return self.has_property(V_LESS_ROUNDED)




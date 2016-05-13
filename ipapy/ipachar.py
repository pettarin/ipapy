#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function
import io
import os

from ipapy.compatibility import hex2unichr

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

# IPA data file constants
IPA_DATA_FILE_CODEPOINT_SEPARATOR = " "
IPA_DATA_FILE_COMMENT = "#"
IPA_DATA_FILE_COMPOUND_OPERATOR = "+"
IPA_DATA_FILE_FIELD_SEPARATOR = ","
IPA_DATA_FILE_NOT_AVAILABLE = "N/A"
IPA_DATA_FILE_PATH = "data/ipa.all"

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
D_LABIODENTAL = ["labiodental", "labio-dental", "blb"]
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
D_PLOSIVE = ["plosive", "imp"]
D_POSTALVEOLAR = ["postalveolar", "palato-alveolar", "pla"]
D_RAISED = ["raised"]
D_RETRACTED = ["retracted"]
D_RETRACTED_TONGUE_ROOT = ["retracted-tongue-root"]
D_RETROFLEX = ["retroflex", "rfx"]
D_RHOTACIZED = ["rhotacized", "rzd"]
D_STOP = ["stop", "stp"]
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
V_CENTER = ["center", "cnt"]
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
    def canonical_properties(self):
        acc = []
        for p in self.properties:
            pass
        return acc

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



def load_ipa_data():
    ipa_signs = []
    unicode_to_ipa = {}
    ipa_to_unicode = {}
    file_path = os.path.join(os.path.dirname(__file__), IPA_DATA_FILE_PATH)
    with io.open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if (len(line) > 0) and (not line.startswith(IPA_DATA_FILE_COMMENT)):
                # unpack line
                try:
                    i_type, i_desc, i_unicode = line.split(IPA_DATA_FILE_FIELD_SEPARATOR)
                except:
                    raise ValueError("The IPA data file contains a bad line: '%s'" % line)
                # create name
                name = "%s %s" % (i_desc, i_type)
                # create obj
                if i_type == "consonant":
                    obj = IPAConsonant(name=name, properties=i_desc)
                elif i_type == "vowel":
                    obj = IPAVowel(name=name, properties=i_desc)
                elif i_type == "diacritic":
                    obj = IPADiacritic(name=name, properties=i_desc)
                elif i_type == "suprasegmental":
                    obj = IPASuprasegmental(name=name, properties=i_desc)
                elif i_type == "tone":
                    obj = IPATone(name=name, properties=i_desc)
                else:
                    raise ValueError("The IPA data file contains a bad line: '%s'" % line)
                ipa_signs.append(obj)
                # map Unicode codepoint to object, if the former is available
                primary_set = False
                for codepoint in i_unicode.split(IPA_DATA_FILE_CODEPOINT_SEPARATOR):
                    # deal with compound symbols, like '||' = major-group suprasegmental
                    key = None
                    if IPA_DATA_FILE_COMPOUND_OPERATOR in codepoint:
                        ch1, ch2 = codepoint.split(IPA_DATA_FILE_COMPOUND_OPERATOR)
                        key = hex2unichr(ch1) + hex2unichr(ch2)
                    elif not IPA_DATA_FILE_NOT_AVAILABLE in codepoint:
                        key = hex2unichr(codepoint)
                    # if we have a key, map it
                    if key is not None:
                        if key in unicode_to_ipa:
                            raise ValueError("The IPA data file contains a bad line, redefining codepoint'%s': '%s'" % (codepoint, line))
                        unicode_to_ipa[key] = obj
                        if not primary_set:
                            primary_set = True
                            ipa_to_unicode[obj.properties] = key
                            obj.unicode_char = key
    return ipa_signs, unicode_to_ipa, ipa_to_unicode
IPA_SIGNS, UNICODE_TO_IPA, IPA_TO_UNICODE = load_ipa_data()




#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.compatibility import is_unicode_string

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

def flatten(lists):
    """
    Flatten a list-of-lists, that is,
    return a list containing the union of the elements
    of all lists in the given list-of-lists.

    :param list lists: a list-of-lists
    :rtype: list
    """
    if not isinstance(lists, list):
        raise TypeError("The given object is not a list")
    for l in lists:
        if not isinstance(l, list):
            raise TypeError("The given object contains an element which is not a list")
    acc = []
    for l in lists:
        acc.extend(l)
    return acc

# types
T_CONSONANT = ["consonant", "cns"]
T_VOWEL = ["vowel", "vwl"]
T_DIACRITIC = ["diacritic", "dia"]
T_SUPRASEGMENTAL = ["suprasegmental", "sup"]
T_TONE = ["tone", "ton"]
G_TYPES = [
    T_CONSONANT,
    T_VOWEL,
    T_DIACRITIC,
    T_SUPRASEGMENTAL,
    T_TONE
]
FG_TYPES = flatten(G_TYPES)

# consonants
D_VOICED = ["voiced", "vcd"]
D_VOICELESS = ["voiceless", "tenuis", "vls"]
G_VOICING = [
    D_VOICED,
    D_VOICELESS
]
FG_VOICING = flatten(G_VOICING)

D_ALVEOLAR = ["alveolar", "alv"]
D_ALVEOLO_NASAL = ["alveolo-nasal", "alveolar-nasal"]
D_ALVEOLO_PALATAL = ["alveolo-palatal", "alveolar-palatal"]
D_BILABIAL = ["bilabial", "blb"]
D_DENTAL = ["dental", "dnt"]
D_DENTO_NASAL = ["dento-nasal", "dental-nasal"]
D_GLOTTAL = ["glottal", "glt"]
D_LABIO_ALVEOLAR = ["labio-alveolar", "labial-alveolar", "labioalveolar"]
D_LABIO_DENTAL = ["labio-dental", "labial-dental", "labiodental", "lbd"]
D_LABIO_PALATAL = ["labio-palatal", "labial-palatal", "labiopalatal"]
D_LABIO_VELAR = ["labio-velar", "labial-velar", "labiovelar"]
D_LINGUOLABIAL = ["linguolabial"]
D_PALATAL = ["palatal", "pal"]
D_PALATO_ALVEOLAR = ["palato-alveolar", "palatal-alveolar", "palatoalveolar", "postalveolar", "pla"]
D_PALATO_ALVEOLO_VELAR = ["palato-alveolo-velar", "palatoalveolar-velar"]
D_PALATO_NASAL = ["palato-nasal", "palatal-nasal", "palatonasal"]
D_PHARYNGEAL = ["pharyngeal", "epiglottal", "phr"]
D_RETROFLEX = ["retroflex", "rfx"]
D_RETROFLEX_NASAL = ["retroflex-nasal", "retroflexnasal"]
D_UVULAR = ["uvular", "uvl"]
D_UVULO_PHARYNGEAL = ["uvulo-pharyngeal", "uvular-pharyngeal", "uvulopharyngeal"]
D_VELAR = ["velar", "vel"]
G_PLACE = [
    D_ALVEOLAR,
    D_ALVEOLO_NASAL,
    D_ALVEOLO_PALATAL,
    D_BILABIAL,
    D_DENTAL,
    D_DENTO_NASAL,
    D_GLOTTAL,
    D_LABIO_ALVEOLAR,
    D_LABIO_DENTAL,
    D_LABIO_PALATAL,
    D_LABIO_VELAR,
    D_LINGUOLABIAL,
    D_PALATAL,
    D_PALATO_ALVEOLAR,
    D_PALATO_ALVEOLO_VELAR,
    D_PALATO_NASAL,
    D_PHARYNGEAL,
    D_RETROFLEX,
    D_RETROFLEX_NASAL,
    D_UVULAR,
    D_UVULO_PHARYNGEAL,
    D_VELAR,
]
FG_PLACE = flatten(G_PLACE)

D_APPROXIMANT = ["approximant", "apr"]
D_CLICK = ["click", "clk"]
D_EJECTIVE = ["ejective", "ejc"]
D_EJECTIVE_AFFRICATE = ["ejective-affricate"]
D_EJECTIVE_FRICATIVE = ["ejective-fricative"]
D_FLAP = ["flap", "tap", "flp"]
D_IMPLOSIVE = ["implosive", "imp"]
D_LATERAL_AFFRICATE = ["lateral-affricate"]
D_LATERAL_APPROXIMANT = ["lateral-approximant"]
D_LATERAL_CLICK = ["lateral-click"]
D_LATERAL_EJECTIVE_AFFRICATE = ["lateral-ejective-affricate"]
D_LATERAL_EJECTIVE_FRICATIVE = ["lateral-ejective-fricative"]
D_LATERAL_FLAP = ["lateral-flap"]
D_LATERAL_FRICATIVE = ["lateral-fricative"]
D_NASAL = ["nasal", "nas"]
D_NON_SIBILANT_AFFRICATE = ["non-sibilant-affricate"]
D_NON_SIBILANT_FRICATIVE = ["non-sibilant-fricative"]
D_PLOSIVE = ["plosive", "stop", "stp"]
D_SIBILANT_AFFRICATE = ["sibilant-affricate"]
D_SIBILANT_FRICATIVE = ["sibilant-fricative"]
D_TRILL = ["trill", "trl"]
G_MANNER = [
    D_APPROXIMANT,
    D_CLICK,
    D_EJECTIVE,
    D_EJECTIVE_AFFRICATE,
    D_EJECTIVE_FRICATIVE,
    D_FLAP,
    D_IMPLOSIVE,
    D_LATERAL_AFFRICATE,
    D_LATERAL_APPROXIMANT,
    D_LATERAL_CLICK,
    D_LATERAL_EJECTIVE_AFFRICATE,
    D_LATERAL_EJECTIVE_FRICATIVE,
    D_LATERAL_FLAP,
    D_LATERAL_FRICATIVE,
    D_NASAL,
    D_NON_SIBILANT_AFFRICATE,
    D_NON_SIBILANT_FRICATIVE,
    D_PLOSIVE,
    D_SIBILANT_AFFRICATE,
    D_SIBILANT_FRICATIVE,
    D_TRILL,
]
FG_MANNER = flatten(G_MANNER)

G_CONSONANTS = [
    FG_VOICING,
    FG_PLACE,
    FG_MANNER
]
FG_CONSONANTS = flatten(G_CONSONANTS)

# diacritics
D_ADVANCED = ["advanced"]
D_ADVANCED_TONGUE_ROOT = ["advanced-tongue-root"]
D_APICAL = ["apical"]
D_ASPIRATED = ["aspirated", "asp"]
D_BREATHY_VOICED = ["breathy-voiced"]
D_CENTRALIZED = ["centralized"]
D_CREAKY_VOICED = ["creaky-voiced"]
D_LABIALIZED = ["labialized", "lzd"]
D_LAMINAL = ["laminal"]
D_LATERAL_RELEASE = ["lateral-release"]
D_LESS_ROUNDED = ["less-rounded"]
D_LOWERED = ["lowered"]
D_MID_CENTRALIZED = ["mid-centralized"]
D_MORE_ROUNDED = ["more-rounded"]
D_NASALIZED = ["nasalized"]
D_NASAL_RELEASE = ["nasal-release"]
D_NON_SYLLABIC = ["non-syllabic"]
D_NO_AUDIBLE_RELEASE = ["no-audible-release"]
D_PALATALIZED = ["palatalized", "pzd"]
D_PHARYNGEALIZED = ["pharyngealized", "fzd"]
D_RAISED = ["raised"]
D_RETRACTED = ["retracted"]
D_RETRACTED_TONGUE_ROOT = ["retracted-tongue-root"]
D_RHOTACIZED = ["rhotacized", "rzd"]
D_SYLLABIC = ["syllabic", "syl"]
D_TIE_BAR_ABOVE = ["tie-bar-above"]
D_TIE_BAR_BELOW = ["tie-bar-below"]
D_UNEXPLODED = ["unexploded"]
D_VELARIZED = ["velarized", "vzd"]
D_VELARIZED_OR_PHARYNGEALIZED = ["velarized-or-pharyngealized"]
G_DIACRITICS = [
    D_ADVANCED,
    D_ADVANCED_TONGUE_ROOT,
    D_APICAL,
    D_ASPIRATED,
    D_BREATHY_VOICED,
    D_CENTRALIZED,
    D_CREAKY_VOICED,
    D_LABIALIZED,
    D_LAMINAL,
    D_LATERAL_RELEASE,
    D_LESS_ROUNDED,
    D_LOWERED,
    D_MID_CENTRALIZED,
    D_MORE_ROUNDED,
    D_NASALIZED,
    D_NASAL_RELEASE,
    D_NON_SYLLABIC,
    D_NO_AUDIBLE_RELEASE,
    D_PALATALIZED,
    D_PHARYNGEALIZED,
    D_RAISED,
    D_RETRACTED,
    D_RETRACTED_TONGUE_ROOT,
    D_RHOTACIZED,
    D_SYLLABIC,
    D_TIE_BAR_ABOVE,
    D_TIE_BAR_BELOW,
    D_UNEXPLODED,
    D_VELARIZED,
    D_VELARIZED_OR_PHARYNGEALIZED,
]
FG_DIACRITICS = flatten(G_DIACRITICS)

# vowels
V_CLOSE = ["close", "high", "hgh"]
V_NEAR_CLOSE = ["near-close", "lowered-close", "semi-high", "smh"]
V_CLOSE_MID = ["close-mid", "upper-mid", "umd"]
V_MID = ["mid"]
V_OPEN_MID = ["open-mid", "lower-mid", "lmd"]
V_NEAR_OPEN = ["near-open", "raised-open", "semi-low", "slw"]
V_OPEN = ["open", "low"]
G_HEIGHT = [
    V_CLOSE,
    V_NEAR_CLOSE,
    V_CLOSE_MID,
    V_MID,
    V_OPEN_MID,
    V_NEAR_OPEN,
    V_OPEN,
]
FG_HEIGHT = flatten(G_HEIGHT)

V_FRONT = ["front", "fnt"]
V_NEAR_FRONT = ["near-front"]
V_CENTER = ["central", "center", "cnt"]
V_NEAR_BACK = ["near-back"]
V_BACK = ["back", "bck"]
G_BACKNESS = [
    V_FRONT,
    V_NEAR_FRONT,
    V_CENTER,
    V_NEAR_BACK,
    V_BACK,
]
G_BACKNESS_MODIFIERS = [
    D_ADVANCED,
    D_RETRACTED,
    D_CENTRALIZED,
    D_MID_CENTRALIZED,
]
FG_BACKNESS = flatten(G_BACKNESS)

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
FG_ROUNDNESS = flatten(G_ROUNDNESS)

G_VOWELS = [
    FG_HEIGHT,
    FG_BACKNESS,
    FG_ROUNDNESS,
]
FG_VOWELS = flatten(G_VOWELS)

# suprasegmentals
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
G_SUPRASEGMENTALS = [
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
FG_SUPRASEGMENTALS = flatten(G_SUPRASEGMENTALS)

# tones 
T_EXTRA_HIGH_LEVEL = ["extra-high-level"]
T_HIGH_LEVEL = ["high-level"]
T_MID_LEVEL = ["mid-level"]
T_LOW_LEVEL = ["low-level"]
T_EXTRA_LOW_LEVEL = ["extra-low-level"]
T_RISING_CONTOUR = ["rising-contour"]
T_FALLING_CONTOUR = ["falling-contour"]
T_HIGH_RISING_CONTOUR = ["high-rising-contour"]
T_LOW_RISING_CONTOUR = ["low-rising-contour"]
T_RISING_FALLING_CONTOUR = ["rising-falling-contour"]
T_MID_LOW_FALLING_CONTOUR = ["mid-low-falling-contour"]
T_HIGH_MID_FALLING_CONTOUR = ["high-mid-falling-contour"]
T_FALLING_RISING_CONTOUR = ["falling-rising-contour"]
T_DOWNSTEP = ["downstep"]
T_UPSTEP = ["upstep"]
T_GLOBAL_RISE = ["global-rise"]
T_GLOBAL_FALL = ["global-fall"]
G_TONE_LEVEL = [
    T_EXTRA_HIGH_LEVEL,
    T_HIGH_LEVEL,
    T_MID_LEVEL,
    T_LOW_LEVEL,
    T_EXTRA_LOW_LEVEL,
]
G_TONE_CONTOUR = [
    T_RISING_CONTOUR,
    T_FALLING_CONTOUR,
    T_HIGH_RISING_CONTOUR,
    T_LOW_RISING_CONTOUR,
    T_RISING_FALLING_CONTOUR,
    T_MID_LOW_FALLING_CONTOUR,
    T_HIGH_MID_FALLING_CONTOUR,
    T_FALLING_RISING_CONTOUR, 
]
G_TONE_GLOBAL = [
    T_DOWNSTEP,
    T_UPSTEP,
    T_GLOBAL_RISE,
    T_GLOBAL_FALL,
]
G_TONES = [
    T_EXTRA_HIGH_LEVEL,
    T_HIGH_LEVEL,
    T_MID_LEVEL,
    T_LOW_LEVEL,
    T_EXTRA_LOW_LEVEL,
    T_RISING_CONTOUR,
    T_FALLING_CONTOUR,
    T_HIGH_RISING_CONTOUR,
    T_LOW_RISING_CONTOUR,
    T_RISING_FALLING_CONTOUR,
    T_MID_LOW_FALLING_CONTOUR,
    T_HIGH_MID_FALLING_CONTOUR,
    T_FALLING_RISING_CONTOUR, 
    T_DOWNSTEP,
    T_UPSTEP,
    T_GLOBAL_RISE,
    T_GLOBAL_FALL,
]
FG_TONES = flatten(G_TONES)

# all properties
G_ALL_PROPERTIES = (
    G_TYPES +
    G_DIACRITICS +
    G_SUPRASEGMENTALS +
    G_TONES +
    (G_VOICING + G_PLACE + G_MANNER) +
    (G_HEIGHT + G_BACKNESS + G_ROUNDNESS)
)
FG_ALL_PROPERTIES = flatten(G_ALL_PROPERTIES)

def canonical_representation(properties):
    """
    Return the canonical representation of a list of properties,
    that is, a frozenset built from properties,
    where the value for each group of properties is the canonical one
    (e.g., "open" for the height of a vowel),
    even if the object has been created with a non-canonical value
    (e.g., "low" for the height of a vowel).

    :param list properties: a list of properties
    :rtype: frozenset
    :raise TypeError: if the ``properties`` is not a list
    """
    if not isinstance(properties, list):
        raise TypeError("The properties parameter must be a list")
    return frozenset(sorted(properties))

def variant_to_list(obj):
    """
    Return a list containing the properties in the given object.

    The ``obj`` can be a frozenset, a set, a list (of single properties) or a Unicode string.
    
    If ``obj`` is a Unicode string, it will be split using spaces.

    :param variant obj: the object to be parsed
    :rtype: list 
    :raise TypeError: if the ``obj`` has a type not listed above
    """
    if isinstance(obj, list):
        return obj
    elif isinstance(obj, frozenset) or isinstance(obj, set):
        return list(obj)
    elif is_unicode_string(obj):
        return [s for s in obj.split() if len(s) > 0]
    raise TypeError("The given value must be a frozenset, a set, a list or a Unicode string.")

def variant_to_frozenset(obj):
    """
    Return a frozenset containing the properties in the given object.

    The ``obj`` can be a frozenset, a set, a list (of single properties) or a Unicode string.
    
    If ``obj`` is a Unicode string, it will be split using spaces.

    :param variant obj: the object to be parsed
    :rtype: frozenset
    :raise TypeError: if the ``obj`` has a type not listed above
    """
    return frozenset(variant_to_list(obj))



class IPAChar(object):
    """
    An IPA character, that is, an IPA letter or diacritic/suprasegmental/tone mark.

    Note that an IPAChar might correspond to 0, 1, or more Unicode characters.

    :param str name: an arbitrary mnemonic name for the character
    :param frozenset properties: the properties of the character
    :param str unicode_repr: the Unicode representation for the character
    """
    
    TAG = "IPAChar"

    def __init__(self, name, properties, unicode_repr=None):
        self.name = name
        self.properties = properties
        self.unicode_repr = unicode_repr

    def __str__(self):
        return "" if self.unicode_repr is None else self.unicode_repr
    
    def __unicode__(self):
        return u"" if self.unicode_repr is None else self.unicode_repr

    def __repr__(self):
        return u"%s (%s)" % (self.name, str(self.canonical_representation))

    @property
    def properties(self):
        return self.__properties
    @properties.setter
    def properties(self, value):
        prop = variant_to_frozenset(value)
        if len(prop) < 1:
            raise ValueError("The IPAChar must have at least one property")
        self.__properties = prop

    def is_equivalent(self, other):
        """
        Return ``True`` if the IPA character is equivalent to the ``other`` object.

        The ``other`` object can be:

        1. a Unicode string, containing the representation of the IPA character,
        2. a Unicode string, containing a space-separated list of properties,
        3. a list of Unicode strings, containing properties, and
        4. another IPAChar.

        :rtype: bool
        """
        if (self.unicode_repr is not None) and (is_unicode_string(other)) and (self.unicode_repr == other):
            return True
        if isinstance(other, IPAChar):
            return self.canonical_representation == other.canonical_representation
        try:
            return self.canonical_representation == IPAChar(name=None, properties=other).canonical_representation
        except:
            return False

    @property
    def is_letter(self):
        """
        Return ``True`` if the character is a letter.

        :rtype: bool
        """
        return False

    @property
    def is_consonant(self):
        """
        Return ``True`` if the character is a consonant.

        :rtype: bool
        """
        return False

    @property
    def is_vowel(self):
        """
        Return ``True`` if the character is a vowel.

        :rtype: bool
        """
        return False


    @property
    def is_diacritic(self):
        """
        Return ``True`` if the character is a diacritic mark.

        :rtype: bool
        """
        return False

    @property
    def is_suprasegmental(self):
        """
        Return ``True`` if the character is a suprasegmental mark.

        :rtype: bool
        """
        return False

    @property
    def is_tone(self):
        """
        Return ``True`` if the character is a tone mark.

        :rtype: bool
        """
        return False

    def has_property(self, values):
        """
        Return ``True`` if the character has a property listed
        in the given list of values.

        :param list values: a list of values (synonyms) to check against
        :rtype: bool
        """
        for v in values:
            if v in self.properties:
                return True
        return False

    @property
    def canonical_representation(self):
        """
        The canonical representation of the character.

        Each property of the character is represented
        with its canonical value.

        The canonical representation is a frozenset
        so that it can be hashed.

        :rtype: frozenset
        """
        acc = []
        for g in G_ALL_PROPERTIES:
            for p in self.properties:
                if p in g:
                    acc.append(g[0])
        return canonical_representation(acc)

    def alternative_property(self, alternatives, modifiers=None):
        """
        Check if the character has a property whose value
        is contained in one of the lists forming the given
        ``alternatives`` list-of-lists.

        If it has it, return the canonical value for the property.
        Otherwise, return ``None``.

        If ``modifiers`` are specified, it also checks if the character
        has a modifier property.
        For example, you might want to set
        ``alternatives=G_ROUNDNESS`` and
        ``modifiers=G_ROUNDNESS_MODIFIERS``
        to know the roundness of a vowel and its modifier, if any
        (e.g., ``(rounded, less-roundend)``).

        :param list alternatives: list-of-lists, each being the synonyms for a given value
        :param boolean modifiers: if ``True``, also checks against the given modifiers,
                                  and return a pair ``(value, modifier)`` instead of just ``value``
        :rtype: str
        """
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



def is_list_of_ipachars(obj):
    """
    Return ``True`` if the given object is a list of IPAChar objects.

    :param object obj: the object to test
    :rtype: bool
    """
    if isinstance(obj, list):
        for e in obj:
            if not isinstance(e, IPAChar):
                return False
        return True
    return False



class IPALetter(IPAChar):
    """
    An IPA letter, either a consonant or a vowel.
    """
    
    TAG = "IPALetter"

    @property
    def is_letter(self):
        return True 

    @property
    def modifiers(self):
        """
        The modifiers (e.g., "velarized" or "more-rounded") of the letter.

        :rtype: list
        """
        return self.__modifiers
    @modifiers.setter
    def modifiers(self, value):
        """
        Set the modifiers of the letter.

        :param variant value: a parsable property (list or strings or string with space-separated values)
        """
        self.__modifiers = variant_to_list(value)



class IPAConsonant(IPALetter):
    """
    An IPA consonant.

    The object can be initialized using the ``properties`` as in the generic IPAChar,
    or via the consonant-specific properties:

    1. voicing (e.g. "voiceless"),
    2. place (e.g., "bilabial"),
    3. manner (e.g., "plosive").

    In both cases, a value for each of the three properties must be present,
    otherwise a ValueError will be raised.

    Modifiers (e.g. "velarized") are optional.

    :param str name: an arbitrary mnemonic name for the consonant 
    :param frozenset properties: the properties of the consonant
    :param str unicode_repr: the (optional) Unicode representation for the consonant
    :param str voicing: the voicing of the consonant
    :param str place: the articulation place of the consonant
    :param str manner: the articulation manner of the consonant
    :param variant modifiers: optional modifiers of the consonant
    """
    
    TAG = "IPAConsonant"

    def __init__(self, name, properties=None, unicode_repr=None, voicing=None, place=None, manner=None, modifiers=None):
        self.name = name
        self.unicode_repr = unicode_repr
        self.height = None
        self.backness = None
        self.roundness = None
        self.modifiers = []
        if (voicing is not None) and (place is not None) and (manner is not None):
            properties = [T_CONSONANT[0], voicing, place, manner]
            if modifiers is not None:
                properties.extend(variant_to_list(modifiers))
        elif (voicing, place, manner) != (None, None, None):
            raise ValueError("You must specify either a properties list/string, or a triple (voicing, place, manner)")
        elif properties is None:
            raise ValueError("You must specify either a properties list/string, or a triple (voicing, place, manner)")
        self.properties = properties

    @property
    def is_consonant(self):
        return True

    @property
    def properties(self):
        prop = [T_CONSONANT[0], self.voicing, self.place, self.manner]
        prop.extend(self.modifiers)
        return frozenset(prop)
    @properties.setter
    def properties(self, value):
        voicing = None
        place = None
        manner = None
        modifiers = []
        for p in variant_to_list(value):
            if p in FG_VOICING:
                voicing = p
            elif p in FG_PLACE:
                place = p
            elif p in FG_MANNER:
                manner = p
            elif p not in T_CONSONANT:
                modifiers.append(p)
        if (voicing is not None) and (place is not None) and (manner is not None):
            self.voicing = voicing
            self.place = place
            self.manner = manner
            self.modifiers = modifiers
        else:
            raise ValueError("The properties list must contain a value for each of the following properties: voicing, place, and manner.")

    @property
    def voicing(self):
        """
        The voicing of the consonant.

        :rtype: str
        """
        return self.__voicing
    @voicing.setter
    def voicing(self, value):
        """
        Set the voicing of the consonant.

        :param str value: the value to be set
        """
        if (value is not None) and (not value in FG_VOICING):
            raise ValueError("Unrecognized value for voicing: '%s'" % value)
        self.__voicing = value

    @property
    def place(self):
        """
        The place of articulation of the consonant.

        :rtype: str
        """
        return self.__place
    @place.setter
    def place(self, value):
        """
        Set the place of articulation of the consonant.

        :param str value: the value to be set
        """
        if (value is not None) and (not value in FG_PLACE):
            raise ValueError("Unrecognized value for place: '%s'" % value)
        self.__place = value

    @property
    def manner(self):
        """
        The manner of articulation of the consonant.

        :rtype: str
        """
        return self.__manner
    @manner.setter
    def manner(self, value):
        """
        Set the manner of articulation of the consonant.

        :param str value: the value to be set
        """
        if (value is not None) and (not value in FG_MANNER):
            raise ValueError("Unrecognized value for manner: '%s'" % value)
        self.__manner = value



class IPAVowel(IPALetter):
    """
    An IPA vowel.

    The object can be initialized using the ``properties`` as in the generic IPAChar,
    or via the consonant-specific properties:

    1. height (e.g. "open"),
    2. backness (e.g., "front"),
    3. roundness (e.g., "unrounded").

    In both cases, a value for each of the three properties must be present,
    otherwise a ValueError will be raised.

    Modifiers (e.g. "more-rounded") are optional.

    :param str name: an arbitrary mnemonic name for the vowel
    :param frozenset properties: the properties of the vowel
    :param str unicode_repr: the (optional) Unicode representation for the vowel
    :param str height: the voicing of the vowel
    :param str backness: the articulation place of the vowel
    :param str roundness: the articulation manner of the vowel
    :param variant modifiers: optional modifiers of the vowel
    """
    
    TAG = "IPAVowel"

    def __init__(self, name, properties=None, unicode_repr=None, height=None, backness=None, roundness=None, modifiers=None):
        self.name = name
        self.unicode_repr = unicode_repr
        self.height = None
        self.backness = None
        self.roundness = None
        self.modifiers = []
        if (height is not None) and (backness is not None) and (roundness is not None):
            properties = [T_VOWEL[0], height, backness, roundness]
            if modifiers is not None:
                properties.extend(variant_to_list(modifiers))
        elif (height, backness, roundness) != (None, None, None):
            raise ValueError("You must specify either a properties list/string, or a triple (height, backness, roundness)")
        elif properties is None:
            raise ValueError("You must specify either a properties list/string, or a triple (height, backness, roundness)")
        self.properties = properties

    @property
    def is_vowel(self):
        return True

    @property
    def properties(self):
        prop = [T_VOWEL[0], self.height, self.backness, self.roundness]
        prop.extend(self.modifiers)
        return frozenset(prop)
    @properties.setter
    def properties(self, value):
        height = None
        backness = None
        roundness = None
        modifiers = []
        for p in variant_to_list(value):
            if p in FG_HEIGHT:
                height = p
            elif p in FG_BACKNESS:
                backness = p
            elif p in FG_ROUNDNESS:
                roundness = p
            elif p not in T_VOWEL:
                modifiers.append(p)
        if (height is not None) and (backness is not None) and (roundness is not None):
            self.height = height
            self.backness = backness
            self.roundness = roundness
            self.modifiers = modifiers
        else:
            raise ValueError("The properties list must contain a value for each of the following properties: height, backness, and roundness.")

    @property
    def height(self):
        """
        The height of the vowel.

        :rtype: str
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Set the height of the vowel.

        :param str value: the value to be set
        """
        if (value is not None) and (not value in FG_HEIGHT):
            raise ValueError("Unrecognized value for height: '%s'" % value)
        self.__height = value

    @property
    def backness(self):
        """
        The backness of the vowel.

        :rtype: str
        """
        return self.__backness
    @backness.setter
    def backness(self, value):
        """
        Set the backness of the vowel.

        :param str value: the value to be set
        """
        if (value is not None) and (not value in FG_BACKNESS):
            raise ValueError("Unrecognized value for backness: '%s'" % value)
        self.__backness = value

    @property
    def roundness(self):
        """
        The roundness of the vowel.

        :rtype: str
        """
        return self.__roundness
    @roundness.setter
    def roundness(self, value):
        """
        Set the roundness of the vowel.

        :param str value: the value to be set
        """
        if (value is not None) and (not value in FG_ROUNDNESS):
            raise ValueError("Unrecognized value for roundness: '%s'" % value)
        self.__roundness = value



class IPADiacritic(IPAChar):
    """
    An IPA diacritic mark.
    """
    
    TAG = "IPADiacritic"
    
    @property
    def is_diacritic(self):
        return True



class IPASuprasegmental(IPAChar):
    """
    An IPA suprasegmental mark.
    """
    
    TAG = "IPASuprasegmental"
    
    @property
    def is_suprasegmental(self):
        return True

    @property
    def stress(self):
        """
        Return the stress value of the suprasegmental,
        or ``None`` if not a stress mark.

        :rtype: str
        """
        return self.alternative_property(G_STRESS)

    @property
    def length(self):
        """
        Return the length value of the suprasegmental,
        or ``None`` if not a length mark.

        :rtype: str
        """
        return self.alternative_property(G_LENGTH)

    @property
    def is_stress(self):
        """
        Return ``True`` if the suprasegmental is a stress mark.

        :rtype: bool
        """
        return self.stress is not None

    @property
    def is_length(self):
        """
        Return ``True`` if the suprasegmental is a length mark.

        :rtype: bool
        """
        return self.length is not None

    @property
    def is_word_break(self):
        """
        Return ``True`` if the suprasegmental is a word break mark.

        :rtype: bool
        """
        return self.has_property(S_WORD_BREAK)

    @property
    def is_syllable_break(self):
        """
        Return ``True`` if the suprasegmental is a syllable break mark.

        :rtype: bool
        """
        return self.has_property(S_SYLLABLE_BREAK)

    @property
    def is_minor_or_major_break(self):
        """
        Return ``True`` if the suprasegmental is a minor (foot) or major (intonation) break.
        
        :rtype: bool
        """
        return self.has_property(S_MINOR_GROUP) or self.has_property(S_MAJOR_GROUP)



class IPATone(IPAChar):
    """
    An IPA tone mark.
    """

    TAG = "IPATone"

    @property
    def is_tone(self):
        return True

    @property
    def tone_level(self):
        """
        Return the tone level value of the tone mark,
        or ``None`` if not a tone level mark.

        :rtype: str
        """
        return self.alternative_property(G_TONE_LEVEL)

    @property
    def tone_contour(self):
        """
        Return the tone contour value of the tone mark,
        or ``None`` if not a tone contour mark.

        :rtype: str
        """
        return self.alternative_property(G_TONE_CONTOUR)

    @property
    def is_level_or_contour(self):
        """
        Return ``True`` if the tone mark is a tone level or a tone contour mark.
        
        :rtype: bool
        """
        return (self.tone_level is not None) or (self.tone_contour is not None)

    @property
    def is_global(self):
        """
        Return ``True`` if the tone mark is a global tone mark.
        
        :rtype: bool
        """
        return self.alternative_property(G_TONE_GLOBAL) is not None




#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.compatibility import is_unicode_string
from ipapy.ipadescriptor import IPADescriptor
from ipapy.ipadescriptor import IPADescriptorGroup

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

def variant_to_list(obj):
    """
    Return a list containing the descriptors in the given object.

    The ``obj`` can be a frozenset, a set, a list of descriptor strings, or a Unicode string.
    
    If ``obj`` is a Unicode string, it will be split using spaces as delimiters.

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
    Return a frozenset containing the descriptors in the given object.

    The ``obj`` can be a frozenset, a set, a list of descriptor strings, or a Unicode string.
    
    If ``obj`` is a Unicode string, it will be split using spaces as delimiters.

    :param variant obj: the object to be parsed
    :rtype: frozenset
    :raise TypeError: if the ``obj`` has a type not listed above
    """
    return frozenset(variant_to_list(obj))

# types
D_CONSONANT = IPADescriptor([u"consonant", u"cns"])
D_VOWEL = IPADescriptor([u"vowel", u"vwl"])
D_DIACRITIC = IPADescriptor([u"diacritic", u"dia"])
D_SUPRASEGMENTAL = IPADescriptor([u"suprasegmental", u"sup"])
D_TONE = IPADescriptor([u"tone", u"ton"])
DG_TYPES = IPADescriptorGroup([
    D_CONSONANT,
    D_VOWEL,
    D_DIACRITIC,
    D_SUPRASEGMENTAL,
    D_TONE,
])


# consonants
D_C_VOICED = IPADescriptor([u"voiced", u"vcd"])
D_C_VOICELESS = IPADescriptor([u"voiceless", u"tenuis", u"vls"])
DG_C_VOICING = IPADescriptorGroup([
    D_C_VOICED,
    D_C_VOICELESS,
])
D_C_ALVEOLAR = IPADescriptor([u"alveolar", u"alv"])
D_C_ALVEOLO_NASAL = IPADescriptor([u"alveolo-nasal", u"alveolar-nasal"])
D_C_ALVEOLO_PALATAL = IPADescriptor([u"alveolo-palatal", u"alveolar-palatal"])
D_C_BILABIAL = IPADescriptor([u"bilabial", u"blb"])
D_C_DENTAL = IPADescriptor([u"dental", u"dnt"])
D_C_DENTO_NASAL = IPADescriptor([u"dento-nasal", u"dental-nasal"])
D_C_GLOTTAL = IPADescriptor([u"glottal", u"glt"])
D_C_LABIO_ALVEOLAR = IPADescriptor([u"labio-alveolar", u"labial-alveolar", u"labioalveolar"])
D_C_LABIO_DENTAL = IPADescriptor([u"labio-dental", u"labial-dental", u"labiodental", u"lbd"])
D_C_LABIO_PALATAL = IPADescriptor([u"labio-palatal", u"labial-palatal", u"labiopalatal"])
D_C_LABIO_VELAR = IPADescriptor([u"labio-velar", u"labial-velar", u"labiovelar"])
D_C_LINGUOLABIAL = IPADescriptor([u"linguolabial"])
D_C_PALATAL = IPADescriptor([u"palatal", u"pal"])
D_C_PALATO_ALVEOLAR = IPADescriptor([u"palato-alveolar", u"palatal-alveolar", u"palatoalveolar", u"postalveolar", u"pla"])
D_C_PALATO_ALVEOLO_VELAR = IPADescriptor([u"palato-alveolo-velar", u"palatoalveolar-velar"])
D_C_PALATO_NASAL = IPADescriptor([u"palato-nasal", u"palatal-nasal", u"palatonasal"])
D_C_PHARYNGEAL = IPADescriptor([u"pharyngeal", u"epiglottal", u"phr"])
D_C_RETROFLEX = IPADescriptor([u"retroflex", u"rfx"])
D_C_RETROFLEX_NASAL = IPADescriptor([u"retroflex-nasal", u"retroflexnasal"])
D_C_UVULAR = IPADescriptor([u"uvular", u"uvl"])
D_C_UVULO_PHARYNGEAL = IPADescriptor([u"uvulo-pharyngeal", u"uvular-pharyngeal", u"uvulopharyngeal"])
D_C_VELAR = IPADescriptor([u"velar", u"vel"])
DG_C_PLACE = IPADescriptorGroup([
    D_C_ALVEOLAR,
    D_C_ALVEOLO_NASAL,
    D_C_ALVEOLO_PALATAL,
    D_C_BILABIAL,
    D_C_DENTAL,
    D_C_DENTO_NASAL,
    D_C_GLOTTAL,
    D_C_LABIO_ALVEOLAR,
    D_C_LABIO_DENTAL,
    D_C_LABIO_PALATAL,
    D_C_LABIO_VELAR,
    D_C_LINGUOLABIAL,
    D_C_PALATAL,
    D_C_PALATO_ALVEOLAR,
    D_C_PALATO_ALVEOLO_VELAR,
    D_C_PALATO_NASAL,
    D_C_PHARYNGEAL,
    D_C_RETROFLEX,
    D_C_RETROFLEX_NASAL,
    D_C_UVULAR,
    D_C_UVULO_PHARYNGEAL,
    D_C_VELAR,
])
D_C_APPROXIMANT = IPADescriptor([u"approximant", u"apr"])
D_C_CLICK = IPADescriptor([u"click", u"clk"])
D_C_EJECTIVE = IPADescriptor([u"ejective", u"ejc"])
D_C_EJECTIVE_AFFRICATE = IPADescriptor([u"ejective-affricate"])
D_C_EJECTIVE_FRICATIVE = IPADescriptor([u"ejective-fricative"])
D_C_FLAP = IPADescriptor([u"flap", u"tap", u"flp"])
D_C_IMPLOSIVE = IPADescriptor([u"implosive", u"imp"])
D_C_LATERAL_AFFRICATE = IPADescriptor([u"lateral-affricate"])
D_C_LATERAL_APPROXIMANT = IPADescriptor([u"lateral-approximant"])
D_C_LATERAL_CLICK = IPADescriptor([u"lateral-click"])
D_C_LATERAL_EJECTIVE_AFFRICATE = IPADescriptor([u"lateral-ejective-affricate"])
D_C_LATERAL_EJECTIVE_FRICATIVE = IPADescriptor([u"lateral-ejective-fricative"])
D_C_LATERAL_FLAP = IPADescriptor([u"lateral-flap"])
D_C_LATERAL_FRICATIVE = IPADescriptor([u"lateral-fricative"])
D_C_NASAL = IPADescriptor([u"nasal", u"nas"])
D_C_NON_SIBILANT_AFFRICATE = IPADescriptor([u"non-sibilant-affricate"])
D_C_NON_SIBILANT_FRICATIVE = IPADescriptor([u"non-sibilant-fricative"])
D_C_PLOSIVE = IPADescriptor([u"plosive", u"stop", u"stp"])
D_C_SIBILANT_AFFRICATE = IPADescriptor([u"sibilant-affricate"])
D_C_SIBILANT_FRICATIVE = IPADescriptor([u"sibilant-fricative"])
D_C_TRILL = IPADescriptor([u"trill", u"trl"])
DG_C_MANNER = IPADescriptorGroup([
    D_C_APPROXIMANT,
    D_C_CLICK,
    D_C_EJECTIVE,
    D_C_EJECTIVE_AFFRICATE,
    D_C_EJECTIVE_FRICATIVE,
    D_C_FLAP,
    D_C_IMPLOSIVE,
    D_C_LATERAL_AFFRICATE,
    D_C_LATERAL_APPROXIMANT,
    D_C_LATERAL_CLICK,
    D_C_LATERAL_EJECTIVE_AFFRICATE,
    D_C_LATERAL_EJECTIVE_FRICATIVE,
    D_C_LATERAL_FLAP,
    D_C_LATERAL_FRICATIVE,
    D_C_NASAL,
    D_C_NON_SIBILANT_AFFRICATE,
    D_C_NON_SIBILANT_FRICATIVE,
    D_C_PLOSIVE,
    D_C_SIBILANT_AFFRICATE,
    D_C_SIBILANT_FRICATIVE,
    D_C_TRILL,
])
DG_CONSONANTS = DG_C_VOICING + DG_C_PLACE + DG_C_MANNER


# vowels
D_V_CLOSE = IPADescriptor([u"close", u"high", u"hgh"])
D_V_NEAR_CLOSE = IPADescriptor([u"near-close", u"lowered-close", u"semi-high", u"smh"])
D_V_CLOSE_MID = IPADescriptor([u"close-mid", u"upper-mid", u"umd"])
D_V_MID = IPADescriptor([u"mid"])
D_V_OPEN_MID = IPADescriptor([u"open-mid", u"lower-mid", u"lmd"])
D_V_NEAR_OPEN = IPADescriptor([u"near-open", u"raised-open", u"semi-low", u"slw"])
D_V_OPEN = IPADescriptor([u"open", u"low"])
DG_V_HEIGHT = IPADescriptorGroup([
    D_V_CLOSE,
    D_V_NEAR_CLOSE,
    D_V_CLOSE_MID,
    D_V_MID,
    D_V_OPEN_MID,
    D_V_NEAR_OPEN,
    D_V_OPEN,
])
D_V_FRONT = IPADescriptor([u"front", u"fnt"])
D_V_NEAR_FRONT = IPADescriptor([u"near-front"])
D_V_CENTER = IPADescriptor([u"central", u"center", u"cnt"])
D_V_NEAR_BACK = IPADescriptor([u"near-back"])
D_V_BACK = IPADescriptor([u"back", u"bck"])
DG_V_BACKNESS = IPADescriptorGroup([
    D_V_FRONT,
    D_V_NEAR_FRONT,
    D_V_CENTER,
    D_V_NEAR_BACK,
    D_V_BACK,
])
D_V_ROUNDED = IPADescriptor([u"rounded", u"rnd"])
D_V_UNROUNDED = IPADescriptor([u"unrounded", u"unr"])
DG_V_ROUNDNESS = IPADescriptorGroup([
    D_V_ROUNDED,
    D_V_UNROUNDED,
])
DG_VOWELS = DG_V_HEIGHT + DG_V_BACKNESS + DG_V_ROUNDNESS


# diacritics
D_D_ADVANCED = IPADescriptor([u"advanced"])
D_D_ADVANCED_TONGUE_ROOT = IPADescriptor([u"advanced-tongue-root"])
D_D_APICAL = IPADescriptor([u"apical"])
D_D_ASPIRATED = IPADescriptor([u"aspirated", u"asp"])
D_D_BREATHY_VOICED = IPADescriptor([u"breathy-voiced"])
D_D_CENTRALIZED = IPADescriptor([u"centralized"])
D_D_CREAKY_VOICED = IPADescriptor([u"creaky-voiced"])
D_D_LABIALIZED = IPADescriptor([u"labialized", u"lzd"])
D_D_LAMINAL = IPADescriptor([u"laminal"])
D_D_LATERAL_RELEASE = IPADescriptor([u"lateral-release"])
D_D_LESS_ROUNDED = IPADescriptor([u"less-rounded"])
D_D_LOWERED = IPADescriptor([u"lowered"])
D_D_MID_CENTRALIZED = IPADescriptor([u"mid-centralized"])
D_D_MORE_ROUNDED = IPADescriptor([u"more-rounded"])
D_D_NASALIZED = IPADescriptor([u"nasalized"])
D_D_NASAL_RELEASE = IPADescriptor([u"nasal-release"])
D_D_NON_SYLLABIC = IPADescriptor([u"non-syllabic"])
D_D_NO_AUDIBLE_RELEASE = IPADescriptor([u"no-audible-release"])
D_D_PALATALIZED = IPADescriptor([u"palatalized", u"pzd"])
D_D_PHARYNGEALIZED = IPADescriptor([u"pharyngealized", u"fzd"])
D_D_RAISED = IPADescriptor([u"raised"])
D_D_RETRACTED = IPADescriptor([u"retracted"])
D_D_RETRACTED_TONGUE_ROOT = IPADescriptor([u"retracted-tongue-root"])
D_D_RHOTACIZED = IPADescriptor([u"rhotacized", u"rzd"])
D_D_SYLLABIC = IPADescriptor([u"syllabic", u"syl"])
D_D_TIE_BAR_ABOVE = IPADescriptor([u"tie-bar-above"])
D_D_TIE_BAR_BELOW = IPADescriptor([u"tie-bar-below"])
D_D_UNEXPLODED = IPADescriptor([u"unexploded"])
D_D_VELARIZED = IPADescriptor([u"velarized", u"vzd"])
D_D_VELARIZED_OR_PHARYNGEALIZED = IPADescriptor([u"velarized-or-pharyngealized"])
DG_DIACRITICS = IPADescriptorGroup([
    D_D_ADVANCED,
    D_D_ADVANCED_TONGUE_ROOT,
    D_D_APICAL,
    D_D_ASPIRATED,
    D_D_BREATHY_VOICED,
    D_D_CENTRALIZED,
    D_D_CREAKY_VOICED,
    D_D_LABIALIZED,
    D_D_LAMINAL,
    D_D_LATERAL_RELEASE,
    D_D_LESS_ROUNDED,
    D_D_LOWERED,
    D_D_MID_CENTRALIZED,
    D_D_MORE_ROUNDED,
    D_D_NASALIZED,
    D_D_NASAL_RELEASE,
    D_D_NON_SYLLABIC,
    D_D_NO_AUDIBLE_RELEASE,
    D_D_PALATALIZED,
    D_D_PHARYNGEALIZED,
    D_D_RAISED,
    D_D_RETRACTED,
    D_D_RETRACTED_TONGUE_ROOT,
    D_D_RHOTACIZED,
    D_D_SYLLABIC,
    D_D_TIE_BAR_ABOVE,
    D_D_TIE_BAR_BELOW,
    D_D_UNEXPLODED,
    D_D_VELARIZED,
    D_D_VELARIZED_OR_PHARYNGEALIZED,
])


# suprasegmentals
D_S_PRIMARY_STRESS = IPADescriptor([u"primary-stress"])
D_S_SECONDARY_STRESS = IPADescriptor([u"secondary-stress"])
D_S_LONG = IPADescriptor([u"long", u"lng"])
D_S_HALF_LONG = IPADescriptor([u"half-long"])
D_S_EXTRA_SHORT = IPADescriptor([u"extra-short"])
D_S_MINOR_GROUP = IPADescriptor([u"minor-group"])
D_S_MAJOR_GROUP = IPADescriptor([u"major-group"])
D_S_SYLLABLE_BREAK = IPADescriptor([u"syllable-break"])
D_S_LINKING = IPADescriptor([u"linking"])
D_S_WORD_BREAK = IPADescriptor([u"word-break"])
DG_S_STRESS = IPADescriptorGroup([
    D_S_PRIMARY_STRESS,
    D_S_SECONDARY_STRESS,
])
DG_S_LENGTH = IPADescriptorGroup([
    D_S_LONG,
    D_S_HALF_LONG,
    D_S_EXTRA_SHORT,
])
DG_S_BREAK = IPADescriptorGroup([
    D_S_MINOR_GROUP,
    D_S_MAJOR_GROUP,
    D_S_SYLLABLE_BREAK,
    D_S_LINKING,
    D_S_WORD_BREAK,
])
DG_SUPRASEGMENTALS = DG_S_STRESS + DG_S_LENGTH + DG_S_BREAK


# tones 
D_T_EXTRA_HIGH_LEVEL = IPADescriptor([u"extra-high-level"])
D_T_HIGH_LEVEL = IPADescriptor([u"high-level"])
D_T_MID_LEVEL = IPADescriptor([u"mid-level"])
D_T_LOW_LEVEL = IPADescriptor([u"low-level"])
D_T_EXTRA_LOW_LEVEL = IPADescriptor([u"extra-low-level"])
D_T_RISING_CONTOUR = IPADescriptor([u"rising-contour"])
D_T_FALLING_CONTOUR = IPADescriptor([u"falling-contour"])
D_T_HIGH_RISING_CONTOUR = IPADescriptor([u"high-rising-contour"])
D_T_LOW_RISING_CONTOUR = IPADescriptor([u"low-rising-contour"])
D_T_RISING_FALLING_CONTOUR = IPADescriptor([u"rising-falling-contour"])
D_T_MID_LOW_FALLING_CONTOUR = IPADescriptor([u"mid-low-falling-contour"])
D_T_HIGH_MID_FALLING_CONTOUR = IPADescriptor([u"high-mid-falling-contour"])
D_T_FALLING_RISING_CONTOUR = IPADescriptor([u"falling-rising-contour"])
D_T_DOWNSTEP = IPADescriptor([u"downstep"])
D_T_UPSTEP = IPADescriptor([u"upstep"])
D_T_GLOBAL_RISE = IPADescriptor([u"global-rise"])
D_T_GLOBAL_FALL = IPADescriptor([u"global-fall"])
DG_T_LEVEL = IPADescriptorGroup([
    D_T_EXTRA_HIGH_LEVEL,
    D_T_HIGH_LEVEL,
    D_T_MID_LEVEL,
    D_T_LOW_LEVEL,
    D_T_EXTRA_LOW_LEVEL,
])
DG_T_CONTOUR = IPADescriptorGroup([
    D_T_RISING_CONTOUR,
    D_T_FALLING_CONTOUR,
    D_T_HIGH_RISING_CONTOUR,
    D_T_LOW_RISING_CONTOUR,
    D_T_RISING_FALLING_CONTOUR,
    D_T_MID_LOW_FALLING_CONTOUR,
    D_T_HIGH_MID_FALLING_CONTOUR,
    D_T_FALLING_RISING_CONTOUR, 
])
DG_T_GLOBAL = IPADescriptorGroup([
    D_T_DOWNSTEP,
    D_T_UPSTEP,
    D_T_GLOBAL_RISE,
    D_T_GLOBAL_FALL,
])
DG_TONES = DG_T_LEVEL + DG_T_CONTOUR + DG_T_GLOBAL


# all descriptors
DG_ALL_DESCRIPTORS = DG_TYPES + DG_CONSONANTS + DG_VOWELS + DG_DIACRITICS + DG_SUPRASEGMENTALS + DG_TONES



class IPAChar(object):
    """
    An IPA character, that is, an IPA letter or diacritic/suprasegmental/tone mark.

    Note that an IPAChar might correspond to 0, 1, or more Unicode characters.

    :param str name: an arbitrary mnemonic name for the character
    :param frozenset descriptors: the descriptors of the character
    :param str unicode_repr: the Unicode representation for the character
    """
    
    TAG = "IPAChar"

    def __init__(self, name, descriptors, unicode_repr=None):
        self.name = name
        self.descriptors = descriptors
        self.unicode_repr = unicode_repr

    def __str__(self):
        return u"" if self.unicode_repr is None else self.unicode_repr
    
    def __unicode__(self):
        return u"" if self.unicode_repr is None else self.unicode_repr

    def __repr__(self):
        return u"%s (%s)" % (self.name, str(self.canonical_representation))

    @property
    def descriptors(self):
        return self.__descriptors
    @descriptors.setter
    def descriptors(self, value):
        desc = variant_to_frozenset(value)
        if len(desc) < 1:
            raise ValueError("The IPAChar must have at least one property")
        self.__descriptors = desc

    def is_equivalent(self, other):
        """
        Return ``True`` if the IPA character is equivalent to the ``other`` object.

        The ``other`` object can be:

        1. a Unicode string, containing the representation of the IPA character,
        2. a Unicode string, containing a space-separated list of descriptors,
        3. a list of Unicode strings, containing descriptors, and
        4. another IPAChar.

        :rtype: bool
        """
        if (self.unicode_repr is not None) and (is_unicode_string(other)) and (self.unicode_repr == other):
            return True
        if isinstance(other, IPAChar):
            return self.canonical_representation == other.canonical_representation
        try:
            return self.canonical_representation == IPAChar(name=None, descriptors=other).canonical_representation
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
        for p in self.descriptors:
            canonical = DG_ALL_DESCRIPTORS.canonical_value(p)
            if canonical is not None:
                acc.append(canonical)
        return frozenset(acc)

    def dg_value(self, descriptor_group):
        """
        Return the canonical value of a descriptor of the character,
        provided it is present in the given descriptor group.

        If not present, return ``None``.

        :param IPADescriptorGroup descriptor_group: the descriptor group to be checked against
        :rtype: str
        """
        for p in self.descriptors:
            if p in descriptor_group:
                return descriptor_group.canonical_value(p)
        return None

    def has_descriptor(self, descriptor):
        """
        Return ``True`` if the character has the given descriptor.

        :param IPADescriptor descriptor: the descriptor to be checked against
        :rtype: bool
        """
        for p in self.descriptors:
            if p in descriptor:
                return True
        return False


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

    The object can be initialized using the ``descriptors`` as in the generic IPAChar,
    or via the consonant-specific descriptors:

    1. voicing (e.g. "voiceless"),
    2. place (e.g., "bilabial"),
    3. manner (e.g., "plosive").

    In both cases, a value for each of the three descriptors must be present,
    otherwise a ValueError will be raised.

    Modifiers (e.g. "velarized") are optional.

    :param str name: an arbitrary mnemonic name for the consonant 
    :param frozenset descriptors: the descriptors of the consonant
    :param str unicode_repr: the (optional) Unicode representation for the consonant
    :param str voicing: the voicing of the consonant
    :param str place: the articulation place of the consonant
    :param str manner: the articulation manner of the consonant
    :param variant modifiers: optional modifiers of the consonant
    """
    
    TAG = "IPAConsonant"

    def __init__(self, name, descriptors=None, unicode_repr=None, voicing=None, place=None, manner=None, modifiers=None):
        self.name = name
        self.unicode_repr = unicode_repr
        self.height = None
        self.backness = None
        self.roundness = None
        self.modifiers = []
        if (voicing is not None) and (place is not None) and (manner is not None):
            descriptors = [D_CONSONANT.canonical_label, voicing, place, manner]
            if modifiers is not None:
                descriptors.extend(variant_to_list(modifiers))
        elif (voicing, place, manner) != (None, None, None):
            raise ValueError("You must specify either a descriptors list/string, or a triple (voicing, place, manner)")
        elif descriptors is None:
            raise ValueError("You must specify either a descriptors list/string, or a triple (voicing, place, manner)")
        self.descriptors = descriptors

    @property
    def is_consonant(self):
        return True

    @property
    def descriptors(self):
        desc = [D_CONSONANT.canonical_label, self.voicing, self.place, self.manner]
        desc.extend(self.modifiers)
        return frozenset(desc)
    @descriptors.setter
    def descriptors(self, value):
        voicing = None
        place = None
        manner = None
        modifiers = []
        for p in variant_to_list(value):
            if p in DG_C_VOICING:
                voicing = p
            elif p in DG_C_PLACE:
                place = p
            elif p in DG_C_MANNER:
                manner = p
            elif p not in D_CONSONANT:
                modifiers.append(p)
        if (voicing is not None) and (place is not None) and (manner is not None):
            self.voicing = voicing
            self.place = place
            self.manner = manner
            self.modifiers = modifiers
        else:
            raise ValueError("The descriptors list must contain a value for each of the following descriptors: voicing, place, and manner.")

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
        if (value is not None) and (not value in DG_C_VOICING):
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
        if (value is not None) and (not value in DG_C_PLACE):
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
        if (value is not None) and (not value in DG_C_MANNER):
            raise ValueError("Unrecognized value for manner: '%s'" % value)
        self.__manner = value



class IPAVowel(IPALetter):
    """
    An IPA vowel.

    The object can be initialized using the ``descriptors`` as in the generic IPAChar,
    or via the consonant-specific descriptors:

    1. height (e.g. "open"),
    2. backness (e.g., "front"),
    3. roundness (e.g., "unrounded").

    In both cases, a value for each of the three descriptors must be present,
    otherwise a ValueError will be raised.

    Modifiers (e.g. "more-rounded") are optional.

    :param str name: an arbitrary mnemonic name for the vowel
    :param frozenset descriptors: the descriptors of the vowel
    :param str unicode_repr: the (optional) Unicode representation for the vowel
    :param str height: the voicing of the vowel
    :param str backness: the articulation place of the vowel
    :param str roundness: the articulation manner of the vowel
    :param variant modifiers: optional modifiers of the vowel
    """
    
    TAG = "IPAVowel"

    def __init__(self, name, descriptors=None, unicode_repr=None, height=None, backness=None, roundness=None, modifiers=None):
        self.name = name
        self.unicode_repr = unicode_repr
        self.height = None
        self.backness = None
        self.roundness = None
        self.modifiers = []
        if (height is not None) and (backness is not None) and (roundness is not None):
            descriptors = [D_VOWEL.canonical_label, height, backness, roundness]
            if modifiers is not None:
                descriptors.extend(variant_to_list(modifiers))
        elif (height, backness, roundness) != (None, None, None):
            raise ValueError("You must specify either a descriptors list/string, or a triple (height, backness, roundness)")
        elif descriptors is None:
            raise ValueError("You must specify either a descriptors list/string, or a triple (height, backness, roundness)")
        self.descriptors = descriptors

    @property
    def is_vowel(self):
        return True

    @property
    def descriptors(self):
        desc = [D_VOWEL.canonical_label, self.height, self.backness, self.roundness]
        desc.extend(self.modifiers)
        return frozenset(desc)
    @descriptors.setter
    def descriptors(self, value):
        height = None
        backness = None
        roundness = None
        modifiers = []
        for p in variant_to_list(value):
            if p in DG_V_HEIGHT:
                height = p
            elif p in DG_V_BACKNESS:
                backness = p
            elif p in DG_V_ROUNDNESS:
                roundness = p
            elif p not in D_VOWEL:
                modifiers.append(p)
        if (height is not None) and (backness is not None) and (roundness is not None):
            self.height = height
            self.backness = backness
            self.roundness = roundness
            self.modifiers = modifiers
        else:
            raise ValueError("The descriptors list must contain a value for each of the following descriptors: height, backness, and roundness.")

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
        if (value is not None) and (not value in DG_V_HEIGHT):
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
        if (value is not None) and (not value in DG_V_BACKNESS):
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
        if (value is not None) and (not value in DG_V_ROUNDNESS):
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
        return self.dg_value(DG_S_STRESS)

    @property
    def length(self):
        """
        Return the length value of the suprasegmental,
        or ``None`` if not a length mark.

        :rtype: str
        """
        return self.dg_value(DG_S_LENGTH)

    @property
    def break_mark(self):
        """
        Return the break value of the suprasegmental,
        or ``None`` if not a break mark.

        :rtype: str
        """
        return self.dg_value(DG_S_BREAK)

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
    def is_break(self):
        """
        Return ``True`` if the suprasegmental is a break mark.

        :rtype: bool
        """
        return self.break_mark is not None

    @property
    def is_word_break(self):
        """
        Return ``True`` if the suprasegmental is a word break mark.

        :rtype: bool
        """
        return self.has_descriptor(D_S_WORD_BREAK)

    @property
    def is_syllable_break(self):
        """
        Return ``True`` if the suprasegmental is a syllable break mark.

        :rtype: bool
        """
        return self.has_descriptor(D_S_SYLLABLE_BREAK)

    @property
    def is_minor_or_major_break(self):
        """
        Return ``True`` if the suprasegmental is a minor (foot) or major (intonation) break.
        
        :rtype: bool
        """
        return self.has_descriptor(D_S_MINOR_GROUP) or self.has_descriptor(D_S_MAJOR_GROUP)



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
        return self.dg_value(DG_T_LEVEL)

    @property
    def tone_contour(self):
        """
        Return the tone contour value of the tone mark,
        or ``None`` if not a tone contour mark.

        :rtype: str
        """
        return self.dg_value(DG_T_CONTOUR)

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
        return self.dg_value(DG_T_GLOBAL) is not None




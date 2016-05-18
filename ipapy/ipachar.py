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

class IPADescriptor(object):
    """
    An IPA descriptor is a label associated with an IPA character.

    The first label in the list is assumed to be the canonical label.

    :param list labels: list of labels (str)
    """
    
    TAG = u"IPADescriptor"
    
    def __init__(self, labels):
        if not isinstance(labels, list):
            raise TypeError("Parameter labels must be a list of strings")
        if len(labels) < 1:
            raise ValueError("Parameter labels must contain at least one string")
        self.name = labels[0] 
        self.labels = set(labels)

    def __str__(self):
        return " ".join(self.labels)

    def __unicode__(self):
        return u" ".join(self.labels)

    def __contains__(self, other):
        return other in self.labels



class IPADescriptorGroup(object):
    """
    An IPA descriptor group is a list of descriptors,
    for example different values for the same property,
    like "rounded" and "unrounded" for the vowel roundness.

    :param list descriptors: list of IPADescriptor objects
    """
    
    TAG = u"IPADescriptorGroup"
    
    def __init__(self, descriptors):
        if not isinstance(descriptors, list):
            raise TypeError("Parameter descriptors must be a list of IPADescriptor objects")
        for d in descriptors:
            if not isinstance(d, IPADescriptor):
                raise TypeError("Parameter descriptors must be a list of IPADescriptor objects")
        self.descriptors = descriptors

    def __str__(self):
        return "\n".join([d.__str__() for d in self.descriptors])

    def __unicode__(self):
        return u"\n".join([d.__unicode__() for d in self.labels])

    def __contains__(self, value):
        if isinstance(value, IPADescriptor):
            return value in self.descriptors
        return self.canonical_value(value) is not None

    def __add__(self, other):
        if not isinstance(other, IPADescriptorGroup):
            raise TypeError("Cannot concatenate an object that is not an IPADescriptorGroup")
        return IPADescriptorGroup(descriptors=self.descriptors + other.descriptors)

    def canonical_value(self, query):
        """
        Return the canonical value corresponding to the given query value.

        Return ``None`` if the query value is not present in any descriptor of the group.

        :param str query: the descriptor value to be checked against
        """
        for d in self.descriptors:
            if query in d:
                return d.name
        return None



# types
D_CONSONANT = IPADescriptor(["consonant", "cns"])
D_VOWEL = IPADescriptor(["vowel", "vwl"])
D_DIACRITIC = IPADescriptor(["diacritic", "dia"])
D_SUPRASEGMENTAL = IPADescriptor(["suprasegmental", "sup"])
D_TONE = IPADescriptor(["tone", "ton"])
DG_TYPES = IPADescriptorGroup([
    D_CONSONANT,
    D_VOWEL,
    D_DIACRITIC,
    D_SUPRASEGMENTAL,
    D_TONE,
])


# consonants
D_C_VOICED = IPADescriptor(["voiced", "vcd"])
D_C_VOICELESS = IPADescriptor(["voiceless", "tenuis", "vls"])
DG_C_VOICING = IPADescriptorGroup([
    D_C_VOICED,
    D_C_VOICELESS,
])
D_C_ALVEOLAR = IPADescriptor(["alveolar", "alv"])
D_C_ALVEOLO_NASAL = IPADescriptor(["alveolo-nasal", "alveolar-nasal"])
D_C_ALVEOLO_PALATAL = IPADescriptor(["alveolo-palatal", "alveolar-palatal"])
D_C_BILABIAL = IPADescriptor(["bilabial", "blb"])
D_C_DENTAL = IPADescriptor(["dental", "dnt"])
D_C_DENTO_NASAL = IPADescriptor(["dento-nasal", "dental-nasal"])
D_C_GLOTTAL = IPADescriptor(["glottal", "glt"])
D_C_LABIO_ALVEOLAR = IPADescriptor(["labio-alveolar", "labial-alveolar", "labioalveolar"])
D_C_LABIO_DENTAL = IPADescriptor(["labio-dental", "labial-dental", "labiodental", "lbd"])
D_C_LABIO_PALATAL = IPADescriptor(["labio-palatal", "labial-palatal", "labiopalatal"])
D_C_LABIO_VELAR = IPADescriptor(["labio-velar", "labial-velar", "labiovelar"])
D_C_LINGUOLABIAL = IPADescriptor(["linguolabial"])
D_C_PALATAL = IPADescriptor(["palatal", "pal"])
D_C_PALATO_ALVEOLAR = IPADescriptor(["palato-alveolar", "palatal-alveolar", "palatoalveolar", "postalveolar", "pla"])
D_C_PALATO_ALVEOLO_VELAR = IPADescriptor(["palato-alveolo-velar", "palatoalveolar-velar"])
D_C_PALATO_NASAL = IPADescriptor(["palato-nasal", "palatal-nasal", "palatonasal"])
D_C_PHARYNGEAL = IPADescriptor(["pharyngeal", "epiglottal", "phr"])
D_C_RETROFLEX = IPADescriptor(["retroflex", "rfx"])
D_C_RETROFLEX_NASAL = IPADescriptor(["retroflex-nasal", "retroflexnasal"])
D_C_UVULAR = IPADescriptor(["uvular", "uvl"])
D_C_UVULO_PHARYNGEAL = IPADescriptor(["uvulo-pharyngeal", "uvular-pharyngeal", "uvulopharyngeal"])
D_C_VELAR = IPADescriptor(["velar", "vel"])
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
D_C_APPROXIMANT = IPADescriptor(["approximant", "apr"])
D_C_CLICK = IPADescriptor(["click", "clk"])
D_C_EJECTIVE = IPADescriptor(["ejective", "ejc"])
D_C_EJECTIVE_AFFRICATE = IPADescriptor(["ejective-affricate"])
D_C_EJECTIVE_FRICATIVE = IPADescriptor(["ejective-fricative"])
D_C_FLAP = IPADescriptor(["flap", "tap", "flp"])
D_C_IMPLOSIVE = IPADescriptor(["implosive", "imp"])
D_C_LATERAL_AFFRICATE = IPADescriptor(["lateral-affricate"])
D_C_LATERAL_APPROXIMANT = IPADescriptor(["lateral-approximant"])
D_C_LATERAL_CLICK = IPADescriptor(["lateral-click"])
D_C_LATERAL_EJECTIVE_AFFRICATE = IPADescriptor(["lateral-ejective-affricate"])
D_C_LATERAL_EJECTIVE_FRICATIVE = IPADescriptor(["lateral-ejective-fricative"])
D_C_LATERAL_FLAP = IPADescriptor(["lateral-flap"])
D_C_LATERAL_FRICATIVE = IPADescriptor(["lateral-fricative"])
D_C_NASAL = IPADescriptor(["nasal", "nas"])
D_C_NON_SIBILANT_AFFRICATE = IPADescriptor(["non-sibilant-affricate"])
D_C_NON_SIBILANT_FRICATIVE = IPADescriptor(["non-sibilant-fricative"])
D_C_PLOSIVE = IPADescriptor(["plosive", "stop", "stp"])
D_C_SIBILANT_AFFRICATE = IPADescriptor(["sibilant-affricate"])
D_C_SIBILANT_FRICATIVE = IPADescriptor(["sibilant-fricative"])
D_C_TRILL = IPADescriptor(["trill", "trl"])
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
D_V_CLOSE = IPADescriptor(["close", "high", "hgh"])
D_V_NEAR_CLOSE = IPADescriptor(["near-close", "lowered-close", "semi-high", "smh"])
D_V_CLOSE_MID = IPADescriptor(["close-mid", "upper-mid", "umd"])
D_V_MID = IPADescriptor(["mid"])
D_V_OPEN_MID = IPADescriptor(["open-mid", "lower-mid", "lmd"])
D_V_NEAR_OPEN = IPADescriptor(["near-open", "raised-open", "semi-low", "slw"])
D_V_OPEN = IPADescriptor(["open", "low"])
DG_V_HEIGHT = IPADescriptorGroup([
    D_V_CLOSE,
    D_V_NEAR_CLOSE,
    D_V_CLOSE_MID,
    D_V_MID,
    D_V_OPEN_MID,
    D_V_NEAR_OPEN,
    D_V_OPEN,
])
D_V_FRONT = IPADescriptor(["front", "fnt"])
D_V_NEAR_FRONT = IPADescriptor(["near-front"])
D_V_CENTER = IPADescriptor(["central", "center", "cnt"])
D_V_NEAR_BACK = IPADescriptor(["near-back"])
D_V_BACK = IPADescriptor(["back", "bck"])
DG_V_BACKNESS = IPADescriptorGroup([
    D_V_FRONT,
    D_V_NEAR_FRONT,
    D_V_CENTER,
    D_V_NEAR_BACK,
    D_V_BACK,
])
D_V_ROUNDED = IPADescriptor(["rounded", "rnd"])
D_V_UNROUNDED = IPADescriptor(["unrounded", "unr"])
DG_V_ROUNDNESS = IPADescriptorGroup([
    D_V_ROUNDED,
    D_V_UNROUNDED,
])
DG_VOWELS = DG_V_HEIGHT + DG_V_BACKNESS + DG_V_ROUNDNESS


# diacritics
D_D_ADVANCED = IPADescriptor(["advanced"])
D_D_ADVANCED_TONGUE_ROOT = IPADescriptor(["advanced-tongue-root"])
D_D_APICAL = IPADescriptor(["apical"])
D_D_ASPIRATED = IPADescriptor(["aspirated", "asp"])
D_D_BREATHY_VOICED = IPADescriptor(["breathy-voiced"])
D_D_CENTRALIZED = IPADescriptor(["centralized"])
D_D_CREAKY_VOICED = IPADescriptor(["creaky-voiced"])
D_D_LABIALIZED = IPADescriptor(["labialized", "lzd"])
D_D_LAMINAL = IPADescriptor(["laminal"])
D_D_LATERAL_RELEASE = IPADescriptor(["lateral-release"])
D_D_LESS_ROUNDED = IPADescriptor(["less-rounded"])
D_D_LOWERED = IPADescriptor(["lowered"])
D_D_MID_CENTRALIZED = IPADescriptor(["mid-centralized"])
D_D_MORE_ROUNDED = IPADescriptor(["more-rounded"])
D_D_NASALIZED = IPADescriptor(["nasalized"])
D_D_NASAL_RELEASE = IPADescriptor(["nasal-release"])
D_D_NON_SYLLABIC = IPADescriptor(["non-syllabic"])
D_D_NO_AUDIBLE_RELEASE = IPADescriptor(["no-audible-release"])
D_D_PALATALIZED = IPADescriptor(["palatalized", "pzd"])
D_D_PHARYNGEALIZED = IPADescriptor(["pharyngealized", "fzd"])
D_D_RAISED = IPADescriptor(["raised"])
D_D_RETRACTED = IPADescriptor(["retracted"])
D_D_RETRACTED_TONGUE_ROOT = IPADescriptor(["retracted-tongue-root"])
D_D_RHOTACIZED = IPADescriptor(["rhotacized", "rzd"])
D_D_SYLLABIC = IPADescriptor(["syllabic", "syl"])
D_D_TIE_BAR_ABOVE = IPADescriptor(["tie-bar-above"])
D_D_TIE_BAR_BELOW = IPADescriptor(["tie-bar-below"])
D_D_UNEXPLODED = IPADescriptor(["unexploded"])
D_D_VELARIZED = IPADescriptor(["velarized", "vzd"])
D_D_VELARIZED_OR_PHARYNGEALIZED = IPADescriptor(["velarized-or-pharyngealized"])
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
D_S_PRIMARY_STRESS = IPADescriptor(["primary-stress"])
D_S_SECONDARY_STRESS = IPADescriptor(["secondary-stress"])
D_S_LONG = IPADescriptor(["long", "lng"])
D_S_HALF_LONG = IPADescriptor(["half-long"])
D_S_EXTRA_SHORT = IPADescriptor(["extra-short"])
D_S_MINOR_GROUP = IPADescriptor(["minor-group"])
D_S_MAJOR_GROUP = IPADescriptor(["major-group"])
D_S_SYLLABLE_BREAK = IPADescriptor(["syllable-break"])
D_S_LINKING = IPADescriptor(["linking"])
D_S_WORD_BREAK = IPADescriptor(["word-break"])
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
D_T_EXTRA_HIGH_LEVEL = IPADescriptor(["extra-high-level"])
D_T_HIGH_LEVEL = IPADescriptor(["high-level"])
D_T_MID_LEVEL = IPADescriptor(["mid-level"])
D_T_LOW_LEVEL = IPADescriptor(["low-level"])
D_T_EXTRA_LOW_LEVEL = IPADescriptor(["extra-low-level"])
D_T_RISING_CONTOUR = IPADescriptor(["rising-contour"])
D_T_FALLING_CONTOUR = IPADescriptor(["falling-contour"])
D_T_HIGH_RISING_CONTOUR = IPADescriptor(["high-rising-contour"])
D_T_LOW_RISING_CONTOUR = IPADescriptor(["low-rising-contour"])
D_T_RISING_FALLING_CONTOUR = IPADescriptor(["rising-falling-contour"])
D_T_MID_LOW_FALLING_CONTOUR = IPADescriptor(["mid-low-falling-contour"])
D_T_HIGH_MID_FALLING_CONTOUR = IPADescriptor(["high-mid-falling-contour"])
D_T_FALLING_RISING_CONTOUR = IPADescriptor(["falling-rising-contour"])
D_T_DOWNSTEP = IPADescriptor(["downstep"])
D_T_UPSTEP = IPADescriptor(["upstep"])
D_T_GLOBAL_RISE = IPADescriptor(["global-rise"])
D_T_GLOBAL_FALL = IPADescriptor(["global-fall"])
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



def variant_to_list(obj):
    """
    Return a list containing the descriptors in the given object.

    The ``obj`` can be a frozenset, a set, a list (of single descriptors) or a Unicode string.
    
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
    Return a frozenset containing the descriptors in the given object.

    The ``obj`` can be a frozenset, a set, a list (of single descriptors) or a Unicode string.
    
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
    :param frozenset descriptors: the descriptors of the character
    :param str unicode_repr: the Unicode representation for the character
    """
    
    TAG = "IPAChar"

    def __init__(self, name, descriptors, unicode_repr=None):
        self.name = name
        self.descriptors = descriptors
        self.unicode_repr = unicode_repr

    def __str__(self):
        return "" if self.unicode_repr is None else self.unicode_repr
    
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
            descriptors = [D_CONSONANT.name, voicing, place, manner]
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
        desc = [D_CONSONANT.name, self.voicing, self.place, self.manner]
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
            descriptors = [D_VOWEL.name, height, backness, roundness]
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
        desc = [D_VOWEL.name, self.height, self.backness, self.roundness]
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




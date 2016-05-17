# ipapy

**ipapy** is a Python module to work with IPA strings.

* Version: 0.0.1
* Date: 2016-05-17
* Developer: [Alberto Pettarin](http://www.albertopettarin.it/)
* License: the MIT License (MIT)
* Contact: [click here](http://www.albertopettarin.it/contact.html)

## Installation

```bash
$ pip install ipapy
```

(NOTE: ipapy is not on PyPI yet. It will be uploaded as soon as finished.)

or

```bash
$ git clone https://github.com/pettarin/ipapy.git
$ cd ipapy
```

## Usage

```python
# Unicode string for "achene acanthology"
s_uni = u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"

# check if s contains only IPA characters
from ipapy import is_valid_ipa
is_valid_ipa(s_uni)     # True
is_valid_ipa(u"LoL")    # False (uppercase letter L is not IPA valid)

# create an IPA string from the Unicode string
from ipapy.ipastring import IPAString
s_ipa = IPAString(unicode_string=s_uni)

# print the IPA string
print(unicode(s_ipa))                   # "əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"  (Python 2)
print(s_ipa)                            # "əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"  (Python 3)

# new IPA strings containing only...
print(s_ipa.consonants)                 # "knknθld͡ʒ"                (consonants)
print(s_ipa.vowels)                     # "əiææɑəi"                 (vowels)
print(s_ipa.letters)                    # "əkinækænθɑləd͡ʒi"         (vowels and consonants)
print(s_ipa.cns_vwl)                    # "əkinækænθɑləd͡ʒi"         (vowels and consonants)
print(s_ipa.cns_vwl_str)                # "əˈkinæˌkænˈθɑləd͡ʒi"      (idem + stress marks)
print(s_ipa.cns_vwl_str_len)            # "əˈkiːnæˌkænˈθɑləd͡ʒi"     (idem + length marks)
print(s_ipa.cns_vwl_str_len_wb)         # "əˈkiːn æˌkænˈθɑləd͡ʒi"    (idem + word breaks)
print(s_ipa.cns_vwl_str_len_wb_sb)      # "əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"  (idem + syllable breaks)

# print all IPA chars in s_ipa with their names
for c_ipa in s_ipa:
    print("%s\t%s" % (str(c_ipa), c_ipa.name))

# ə   mid central unrounded vowel
# ˈ   primary-stress suprasegmental
# k   voiceless velar plosive consonant
# i   close front unrounded vowel
# ː   long suprasegmental
# n   voiced alveolar nasal consonant
#     word-break suprasegmental
# æ   near-open front unrounded vowel
# ˌ   secondary-stress suprasegmental
# k   voiceless velar plosive consonant
# æ   near-open front unrounded vowel
# n   voiced alveolar nasal consonant
# ˈ   primary-stress suprasegmental
# θ   voiceless dental non-sibilant-fricative consonant
# ɑ   open back unrounded vowel
# .   syllable-break suprasegmental
# l   voiced alveolar lateral-approximant consonant
# ə   mid central unrounded vowel
# .   syllable-break suprasegmental
# d͡ʒ  voiced palato-alveolar sibilant-affricate consonant
# i   close front unrounded vowel

# print the name and properties of all the consonants in the string
for c_ipa in [c for c in s_ipa if c.is_consonant]:
    print(u"%s => %s" % (c_ipa, c_ipa.name))

# print the name and properties of all the vowels in the string
for c_ipa in [c for c in s_ipa if c.is_vowel]:
    print(u"%s => %s" % (c_ipa, c_ipa.name))

# load IPA char from its Unicode representation
from ipapy import UNICODE_TO_IPA
c1 = UNICODE_TO_IPA["a"]                    # open front unrounded vowel
c2 = UNICODE_TO_IPA["e"]                    # close-mid front unrounded vowel
c3 = UNICODE_TO_IPA[u"\u03B2"]              # voiced bilabial non-sibilant-fricative consonant)

# compound symbols and legacy ligatures
ts1 = UNICODE_TO_IPA[u"t͜ʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
ts2 = UNICODE_TO_IPA[u"tʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
ts3 = UNICODE_TO_IPA[u"ʧ"]                  # voiceless palato-alveolar sibilant-affricate consonant
ts4 = UNICODE_TO_IPA[u"\u0074\u035C\u0283"] # voiceless palato-alveolar sibilant-affricate consonant
ts5 = UNICODE_TO_IPA[u"\u0074\u0283"]       # voiceless palato-alveolar sibilant-affricate consonant
ts6 = UNICODE_TO_IPA[u"\u02A7"]             # voiceless palato-alveolar sibilant-affricate consonant

# create IPA String from list of IPA chars
new_s_ipa = IPAString([c3, c2, ts1, c1])    # "βet͡ʃa"
len(new_s_ipa)                              # 4

# build custom IPA chars
from ipapy.ipachar import IPAVowel
my_a1 = IPAVowel(name="my_a_1", properties="open front unrounded", unicode_repr="a")
my_a2 = IPAVowel(name="my_a_2", properties=["open", "front", "unrounded"], unicode_repr="a")
my_a3 = IPAVowel(name="my_a_3", height="open", backness="front", roundness="unrounded", unicode_repr="a")
my_a4 = IPAVowel(name="my_a_4", properties=["low", "fnt", "unr"], unicode_repr="a")
my_ee = IPAVowel(name="my_e_1", properties="close-mid front unrounded", unicode_repr="e")

my_aa = IPAVowel(name="a with special representation", properties=["low", "fnt", "unr"], unicode_repr="{a foo}")
print(my_aa)        # "{a foo}"

from ipapy.ipachar import IPAConsonant
my_b1 = IPAConsonant(name="bilabial fricative", properties="voiced bilabial non-sibilant-fricative", unicode_repr=u"\u03B2")
my_b2 = IPAConsonant(name="bf", voicing="voiced", place="bilabial", manner="non-sibilant-fricative", unicode_repr=u"\u03B2")
my_tS = IPAConsonant(name="tS", voicing="voiceless", place="palato-alveolar", manner="sibilant-affricate", unicode_repr=u"t͜ʃ")

# compare IPA chars
my_a1 == my_a2      # True
my_a1 == my_a3      # True
my_a1 == my_a4      # True
my_a1 == my_ee      # False
my_a1 == my_b1      # False
my_b1 == my_b2      # True
my_b1 == my_tS      # False
my_ts == ts1        # True
my_ts == ts2        # True
my_ts == ts3        # True
my_ts == ts4        # True
my_ts == ts5        # True
my_ts == ts6        # True

# compare IPA char and Unicode string
my_b1 == u"\u03B2"  # True
my_b1 == u"β"       # True
my_b1 == u"b"       # False
my_tS == u"tS"      # False
my_tS == u"tʃ"      # False (missing U+035C COMBINING DOUBLE BREVE BELOW)
my_tS == u"t͜ʃ"      # True (has U+035C COMBINING DOUBLE BREVE BELOW)

# compare against a string listing properties
my_a1 == "open front unrounded"                                 # False (missing 'vowel')
my_a1 == "open front unrounded vowel"                           # True
my_a1 == "low fnt unr vwl"                                      # True (known abbreviations are good as well)
my_ee == "open front unrounded vowel"                           # False
my_b1 == "voiced bilabial non-sibilant-fricative"               # False (missing 'consonant')
my_b1 == "voiced bilabial non-sibilant-fricative consonant"     # True
my_b1 == "consonant non-sibilant-fricative bilabial voiced"     # True (the order does not matter)
my_b1 == "consonant non-sibilant-fricative bilabial voiceless"  # False

# compare against a list of properties
my_a1 == ["open", "front", "unrounded"]                         # False
my_a1 == ["vowel", "open", "front", "unrounded"]                # True
my_a1 == ["open", "unrounded", "vowel", "front"]                # True
my_a1 == ["low", "fnt", "unr", "vwl"]                           # True

# convert IPA string to ASCII-IPA (Kirshenbaum)
from ipapy.asciiipa import ipa_string_to_ascii_string
a_s1 = ipa_string_to_ascii_string(s_ipa)                        # u"@'ki:n#&,k&n'TA#l@#dZi"

# convert Unicode string to ASCII-IPA (Kirshenbaum)
from ipapy.asciiipa import unicode_string_to_ascii_string
a_s2 = unicode_string_to_ascii_string(s_uni)                    # u"@'ki:n#&,k&n'TA#l@#dZi"

a_s1 == a_s2    # True
```

## License

**ipapy** is released under the MIT License.




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

(NOTE: **ipapy** is **not** on PyPI yet. It will be uploaded as soon as finished.)

or

```bash
$ git clone https://github.com/pettarin/ipapy.git
$ cd ipapy
```

## Usage

### As A Python Module

```python
# import functions and classes
from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy.asciiipa import ipa_string_to_ascii_string
from ipapy.asciiipa import unicode_string_to_ascii_string
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipastring import IPAString

# Unicode string for "achene acanthology"
s_uni = u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"

# check if s contains only IPA characters
is_valid_ipa(s_uni)     # True
is_valid_ipa(u"LoL")    # False (uppercase letter L is not IPA valid)

# create an IPA string from the Unicode string
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
for c in s_ipa.consonants:
    print(u"%s => %s" % (c, c.name))

# print the name and properties of all the vowels in the string
for v in s_ipa.vowels:
    print(u"%s => %s" % (v, v.name))

# load IPA char from its Unicode representation
c1 = UNICODE_TO_IPA["a"]                    # open front unrounded vowel
c2 = UNICODE_TO_IPA["e"]                    # close-mid front unrounded vowel
c3 = UNICODE_TO_IPA[u"\u03B2"]              # voiced bilabial non-sibilant-fricative consonant)
tS1 = UNICODE_TO_IPA[u"t͜ʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
tS2 = UNICODE_TO_IPA[u"tʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
tS3 = UNICODE_TO_IPA[u"ʧ"]                  # voiceless palato-alveolar sibilant-affricate consonant
tS4 = UNICODE_TO_IPA[u"\u0074\u035C\u0283"] # voiceless palato-alveolar sibilant-affricate consonant
tS5 = UNICODE_TO_IPA[u"\u0074\u0283"]       # voiceless palato-alveolar sibilant-affricate consonant
tS6 = UNICODE_TO_IPA[u"\u02A7"]             # voiceless palato-alveolar sibilant-affricate consonant

# note that all the variables point to the same object
tS1 == tS2  # True
tS1 == tS3  # True
tS1 == tS4  # True
tS1 == tS5  # True
tS1 == tS6  # True

# create IPA String from list of IPA chars
new_s_ipa = IPAString([c3, c2, tS1, c1])    # "βet͡ʃa"
len(new_s_ipa)                              # 4

# build custom IPA chars
my_a1 = IPAVowel(name="my_a_1", properties="open front unrounded", unicode_repr="a")
my_a2 = IPAVowel(name="my_a_2", properties=["open", "front", "unrounded"], unicode_repr="a")
my_a3 = IPAVowel(name="my_a_3", height="open", backness="front", roundness="unrounded", unicode_repr="a")
my_a4 = IPAVowel(name="my_a_4", properties=["low", "fnt", "unr"], unicode_repr="a")
my_ee = IPAVowel(name="my_e_1", properties="close-mid front unrounded", unicode_repr="e")

my_aa = IPAVowel(name="a special", properties=["low", "fnt", "unr"], unicode_repr="a{*}")
print(my_aa)    # "a{*}"

my_b1 = IPAConsonant(name="bilabial fricative", properties="voiced bilabial non-sibilant-fricative", unicode_repr=u"\u03B2")
my_b2 = IPAConsonant(name="bf", voicing="voiced", place="bilabial", manner="non-sibilant-fricative", unicode_repr=u"\u03B2")
my_tS = IPAConsonant(name="tS", voicing="voiceless", place="palato-alveolar", manner="sibilant-affricate", unicode_repr=u"t͜ʃ")

# equality vs equivalence
my_tS == tS1                # False (my_tS is a different object than tS1)
my_tS.is_equivalent(tS1)    # True  (my_tS is equivalent to tS1)
tS1.is_equivalent(my_tS)    # True  (and vice versa)

# compare IPA chars
my_a1.is_equivalent(my_a2)  # True
my_a1.is_equivalent(my_a3)  # True
my_a1.is_equivalent(my_a4)  # True
my_a1.is_equivalent(my_ee)  # False
my_a1.is_equivalent(my_b1)  # False
my_b1.is_equivalent(my_b2)  # True
my_b1.is_equivalent(my_tS)  # False

# compare IPA char and Unicode string
my_b1.is_equivalent(u"\u03B2")  # True
my_b1.is_equivalent(u"β")       # True
my_b1.is_equivalent(u"b")       # False
my_tS.is_equivalent(u"tS")      # False
my_tS.is_equivalent(u"tʃ")      # False (missing U+035C COMBINING DOUBLE BREVE BELOW)
my_tS.is_equivalent(u"t͜ʃ")      # True (has U+035C COMBINING DOUBLE BREVE BELOW)

# compare IPA char against a string listing properties
my_a1.is_equivalent("open front unrounded")                                 # False (missing 'vowel')
my_a1.is_equivalent("open front unrounded vowel")                           # True
my_a1.is_equivalent("low fnt unr vwl")                                      # True (known abbreviations are good as well)
my_ee.is_equivalent("open front unrounded vowel")                           # False
my_b1.is_equivalent("voiced bilabial non-sibilant-fricative")               # False (missing 'consonant')
my_b1.is_equivalent("voiced bilabial non-sibilant-fricative consonant")     # True
my_b1.is_equivalent("consonant non-sibilant-fricative bilabial voiced")     # True (the order does not matter)
my_b1.is_equivalent("consonant non-sibilant-fricative bilabial voiceless")  # False

# compare IPA char against a list of properties
my_a1.is_equivalent(["open", "front", "unrounded"])                         # False
my_a1.is_equivalent(["vowel", "open", "front", "unrounded"])                # True
my_a1.is_equivalent(["open", "unrounded", "vowel", "front"])                # True
my_a1.is_equivalent(["low", "fnt", "unr", "vwl"])                           # True

# compare IPA strings
s_ipa_d = IPAString(unicode_string=u"diff")
s_ipa_1 = IPAString(unicode_string=u"at͜ʃe")
s_ipa_2 = IPAString(unicode_string=u"aʧe")
s_ipa_3 = IPAString(unicode_string=u"at͜ʃe", single_char_parsing=True)
s_ipa_d == s_ipa_1              # False
s_ipa_1 == s_ipa_2              # False (different objects)
s_ipa_1 == s_ipa_3              # False (different objects)
s_ipa_2 == s_ipa_3              # False (different objects)
s_ipa_d.is_equivalent(s_ipa_1)  # False
s_ipa_1.is_equivalent(s_ipa_2)  # True
s_ipa_2.is_equivalent(s_ipa_1)  # True
s_ipa_1.is_equivalent(s_ipa_3)  # True
s_ipa_2.is_equivalent(s_ipa_3)  # True

# compare IPA string against a list of IPA chars
s_ipa_1.is_equivalent([my_a1, my_tS, my_ee])

# compare IPA string against a Unicode string
s_ipa_d.is_equivalent("diff")                   # True
s_ipa_d.is_equivalent("less")                   # False
s_ipa_1.is_equivalent("at͜ʃe")                   # True
s_ipa_1.is_equivalent("aʧe")                    # True
s_ipa_1.is_equivalent("aʧe")                    # True
s_ipa_1.is_equivalent("at͜ʃeLOL", ignore=True)   # True (ignore chars non IPA valid)
s_ipa_1.is_equivalent("atse")                   # False

# conversions
s_ascii_ipa = ipa_string_to_ascii_string(s_ipa)     # IPA string to ASCII-IPA (Kirshenbaum)
s_ascii_uni = unicode_string_to_ascii_string(s_uni) # Unicode string to ASCII-IPA (Kirshenbaum)
s_ascii_ipa == s_ascii_uni                          # True, both are u"@'ki:n#&,k&n'TA#l@#dZi"
```

### As A Command Line Tool

**ipapy** comes with a command line tool to perform operations
on a given UTF-8 encoded Unicode string,
representing an IPA string.

Currently, the supported operations are:

* ``canonize``: canonize the Unicode representation of the IPA string
* ``chars``: list all IPA characters appearing in the IPA string
* ``check``: check if the given Unicode string is IPA valid
* ``clean``: remove characters that are not IPA valid
* ``u2a``: print the corresponding ASCII IPA (Kirshenbaum) string

Run:

```bash
$ python -m ipapy --help
```

to get the usage message:

```
usage: __main__.py [-h] [-i] [-p] [-s] [-u] command string

ipapy perform a command on the given IPA/Unicode string

positional arguments:
  command               [canonize|chars|check|clean|u2a]
  string                String to canonize, check, or convert

optional arguments:
  -h, --help            show this help message and exit
  -i, --ignore          Ignore Unicode characters that are not IPA valid
  -p, --print-invalid   Print Unicode characters that are not IPA valid
  -s, --single-char-parsing
                        Perform single character parsing instead of maximal
                        parsing
  -u, --unicode         Print each Unicode character that is not IPA valid
                        with its Unicode codepoint and name
```

Examples:

```bash
$ python -m ipapy canonize "eʧiu"
et͡ʃiu

$ python -m ipapy chars "eʧiu"
'e'	close-mid front unrounded vowel (U+0065)
't͡ʃ'	voiceless palato-alveolar sibilant-affricate consonant (U+0074 U+0361 U+0283)
'i'	close front unrounded vowel (U+0069)
'u'	close back rounded vowel (U+0075)

$ python -m ipapy chars "et͡ʃiu"
'e'	close-mid front unrounded vowel (U+0065)
't͡ʃ'	voiceless palato-alveolar sibilant-affricate consonant (U+0074 U+0361 U+0283)
'i'	close front unrounded vowel (U+0069)
'u'	close back rounded vowel (U+0075)

$ python -m ipapy chars "et͡ʃiu" -s
'e'	close-mid front unrounded vowel (U+0065)
't'	voiceless alveolar plosive consonant (U+0074)
'͡'	tie-bar-above diacritic (U+0361)
'ʃ'	voiceless palato-alveolar sibilant-fricative consonant (U+0283)
'i'	close front unrounded vowel (U+0069)
'u'	close back rounded vowel (U+0075)

$ python -m ipapy check "eʧiu"
True

$ python -m ipapy check "LoL"
False

$ python -m ipapy check "LoL" -p
False
LL

$ python -m ipapy check "LoL" -p -u
False
LL
'L'	0x4c	LATIN CAPITAL LETTER L

$ python -m ipapy clean "(eʧiu)"
eʧiu

$ python -m ipapy u2a "eʧiu"
etSiu

$ python -m ipapy u2a "eTa"
The given string contains characters not IPA valid. Use the 'ignore' option to ignore them.

$ python -m ipapy u2a "eTa" -i
ea
```

## License

**ipapy** is released under the MIT License.




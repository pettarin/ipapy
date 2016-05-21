# ipapy

**ipapy** is a Python module to work with IPA strings.

* Version: 0.0.2
* Date: 2016-05-21
* Developer: [Alberto Pettarin](http://www.albertopettarin.it/)
* License: the MIT License (MIT)
* Contact: [click here](http://www.albertopettarin.it/contact.html)
* Links: [GitHub](https://github.com/pettarin/ipapy) - [PyPI](https://pypi.python.org/pypi/ipapy)

## Installation

```bash
$ pip install ipapy
```

or

```bash
$ git clone https://github.com/pettarin/ipapy.git
$ cd ipapy
```


## Usage

### As A Python Module

```python
###########
# IMPORTS #
###########
from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy.asciiipa import ipa_string_to_ascii_string
from ipapy.asciiipa import unicode_string_to_ascii_string
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipastring import IPAString


###########
# IPAChar #
###########

# Def.: an IPAChar is an IPA letter or diacritic/suprasegmental/tone mark

# create IPAChar from its Unicode representation
c1 = UNICODE_TO_IPA[u"a"]                   # open front unrounded vowel
c2 = UNICODE_TO_IPA[u"e"]                   # close-mid front unrounded vowel
c3 = UNICODE_TO_IPA[u"\u03B2"]              # voiced bilabial non-sibilant-fricative consonant)
tS1 = UNICODE_TO_IPA[u"t͡ʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
tS2 = UNICODE_TO_IPA[u"t͜ʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
tS3 = UNICODE_TO_IPA[u"tʃ"]                 # voiceless palato-alveolar sibilant-affricate consonant
tS4 = UNICODE_TO_IPA[u"ʧ"]                  # voiceless palato-alveolar sibilant-affricate consonant
tS5 = UNICODE_TO_IPA[u"\u0074\u0361\u0283"] # voiceless palato-alveolar sibilant-affricate consonant
tS6 = UNICODE_TO_IPA[u"\u0074\u035C\u0283"] # voiceless palato-alveolar sibilant-affricate consonant
tS7 = UNICODE_TO_IPA[u"\u0074\u0283"]       # voiceless palato-alveolar sibilant-affricate consonant
tS8 = UNICODE_TO_IPA[u"\u02A7"]             # voiceless palato-alveolar sibilant-affricate consonant
c1 == c2    # False
c1 == c3    # False
c1 == tS1   # False
tS1 == tS2  # True (they both point to the same IPAChar object)
tS1 == tS3  # True (idem)
tS1 == tS4  # True (idem)
tS1 == tS5  # True (idem)
tS1 == tS6  # True (idem)
tS1 == tS7  # True (idem)
tS1 == tS8  # True (idem)

# create custom IPAChars
my_a1 = IPAVowel(name="my_a_1", descriptors=u"open front unrounded", unicode_repr=u"a")
my_a2 = IPAVowel(name="my_a_2", descriptors=[u"open", "front", "unrounded"], unicode_repr=u"a")
my_a3 = IPAVowel(name="my_a_3", height=u"open", backness=u"front", roundness=u"unrounded", unicode_repr=u"a")
my_a4 = IPAVowel(name="my_a_4", descriptors=[u"low", u"fnt", "unr"], unicode_repr=u"a")
my_ee = IPAVowel(name="my_e_1", descriptors=u"close-mid front unrounded", unicode_repr=u"e")
my_b1 = IPAConsonant(name="bilabial fricative", descriptors=u"voiced bilabial non-sibilant-fricative", unicode_repr=u"\u03B2")
my_b2 = IPAConsonant(name="bf", voicing=u"voiced", place=u"bilabial", manner=u"non-sibilant-fricative", unicode_repr=u"\u03B2")
my_tS = IPAConsonant(name="tS", voicing=u"voiceless", place=u"palato-alveolar", manner=u"sibilant-affricate", unicode_repr=u"t͡ʃ")
my_a1 == my_a2                  # False (two different objects)
my_a1 == c1                     # False (two different objects)
my_a1 == UNICODE_TO_IPA["a"]    # False (two different objects)

# associate non-standard Unicode representation
my_aa = IPAVowel(name="a special", descriptors=[u"low", u"fnt", u"unr"], unicode_repr=u"a{*}")
print(my_aa)    # "a{*}"

# equality vs. equivalence
my_tS == tS1                # False (my_tS is a different object than tS1)
my_tS.is_equivalent(tS1)    # True  (my_tS is equivalent to tS1...)
tS1.is_equivalent(my_tS)    # True  (... and vice versa)

# compare IPAChar objects
my_a1.is_equivalent(my_a2)  # True
my_a1.is_equivalent(my_a3)  # True
my_a1.is_equivalent(my_a4)  # True
my_a1.is_equivalent(my_ee)  # False
my_a1.is_equivalent(my_b1)  # False
my_b1.is_equivalent(my_b2)  # True
my_b1.is_equivalent(my_tS)  # False

# compare IPAChar and a Unicode string
my_b1.is_equivalent(u"\u03B2")  # True
my_b1.is_equivalent(u"β")       # True
my_b1.is_equivalent(u"b")       # False
my_tS.is_equivalent(u"tS")      # False
my_tS.is_equivalent(u"tʃ")      # False (missing the combining diacritic)
my_tS.is_equivalent(u"t͜ʃ")      # True (has combining diacritic)

# compare IPAChar and a string listing descriptors
my_a1.is_equivalent(u"open front unrounded")                                # False (missing 'vowel')
my_a1.is_equivalent(u"open front unrounded vowel")                          # True
my_a1.is_equivalent(u"low fnt unr vwl")                                     # True (known abbreviations are good as well)
my_ee.is_equivalent(u"open front unrounded vowel")                          # False
my_b1.is_equivalent(u"voiced bilabial non-sibilant-fricative")              # False (missing 'consonant')
my_b1.is_equivalent(u"voiced bilabial non-sibilant-fricative consonant")    # True
my_b1.is_equivalent(u"consonant non-sibilant-fricative bilabial voiced")    # True (the order does not matter)
my_b1.is_equivalent(u"consonant non-sibilant-fricative bilabial voiceless") # False

# compare IPAChar and list of descriptors
my_a1.is_equivalent([u"open", u"front", u"unrounded"])              # False
my_a1.is_equivalent([u"vowel", u"open", u"front", u"unrounded"])    # True
my_a1.is_equivalent([u"open", u"unrounded", u"vowel", u"front"])    # True
my_a1.is_equivalent([u"low", u"fnt", u"unr", u"vwl"])               # True


#############
# IPAString #
#############

# Def.: an IPAString is a list of IPAChar objects

# check if Unicode string contains only IPA valid characters
s_uni = u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"   # Unicode string of the IPA pronunciation for "achene acanthology"
is_valid_ipa(s_uni)                 # True
is_valid_ipa(u"LoL")                # False (uppercase letter L is not IPA valid)

# create IPAString from list of IPAChar objects
new_s_ipa = IPAString(ipa_chars=[c3, c2, tS1, c1])

# create IPAString from Unicode string
s_ipa = IPAString(unicode_string=s_uni)

# IPAString is similar to regular Python string object
print(s_ipa)                            # "əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"
len(s_ipa)                              # 21
s_ipa[0]                                # (first IPA char)
s_ipa[5:8]                              # (6th, 7th, 8th IPA chars)
s_ipa[19:]                              # (IPA chars from the 20th)
s_ipa[-1]                               # (last IPA char)
len(new_s_ipa)                          # 4
new_s_ipa.append(UNICODE_TO_IPA[u"a"])  # (append IPA char "a")
len(new_s_ipa)                          # 5
new_s_ipa.append(UNICODE_TO_IPA[u"t͡ʃ"]) # (append IPA char "t͡ʃ")
len(new_s_ipa)                          # 6
new_s_ipa.extend(s_ipa)                 # (append s_ipa to new_s_ipa)
len(new_s_ipa)                          # 27
double = s_ipa + new_s_ipa              # (concatenate s_ipa and new_s_ipa)
len(double)                             # 48

# new IPAString objects containing only...
s_ipa.consonants                        # "knknθld͡ʒ"                (consonants)
s_ipa.vowels                            # "əiææɑəi"                 (vowels)
s_ipa.letters                           # "əkinækænθɑləd͡ʒi"         (vowels and consonants)
s_ipa.cns_vwl                           # "əkinækænθɑləd͡ʒi"         (vowels and consonants)
s_ipa.cns_vwl_str                       # "əˈkinæˌkænˈθɑləd͡ʒi"      (  + stress marks)
s_ipa.cns_vwl_str_len                   # "əˈkiːnæˌkænˈθɑləd͡ʒi"     (    + length marks)
s_ipa.cns_vwl_str_len_wb                # "əˈkiːn æˌkænˈθɑləd͡ʒi"    (      + word breaks)
s_ipa.cns_vwl_str_len_wb_sb             # "əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"  (        + syllable breaks)
cns = s_ipa.consonants                  # (store new IPA string)
cns == s_ipa.consonants                 # False (two different objects)
cns.is_equivalent(s_ipa.consonants)     # True
cns.is_equivalent(s_ipa)                # False

# print representation and name of all IPAChar objects in IPAString
for c in s_ipa:
    print(u"%s\t%s" % (c, c.name))
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

# compare IPAString objects
s_ipa_d = IPAString(unicode_string=u"diff")
s_ipa_1 = IPAString(unicode_string=u"at͡ʃe")
s_ipa_2 = IPAString(unicode_string=u"aʧe")
s_ipa_3 = IPAString(unicode_string=u"at͡ʃe", single_char_parsing=True)
s_ipa_d == s_ipa_1              # False
s_ipa_1 == s_ipa_2              # False (different objects)
s_ipa_1 == s_ipa_3              # False (different objects)
s_ipa_2 == s_ipa_3              # False (different objects)
s_ipa_d.is_equivalent(s_ipa_1)  # False
s_ipa_1.is_equivalent(s_ipa_2)  # True
s_ipa_2.is_equivalent(s_ipa_1)  # True
s_ipa_1.is_equivalent(s_ipa_3)  # True
s_ipa_2.is_equivalent(s_ipa_3)  # True

# compare IPAString and list of IPAChar objects
s_ipa_1.is_equivalent([my_a1, my_tS, my_ee])    # True

# compare IPAString and Unicode string
s_ipa_d.is_equivalent(u"diff")                  # True
s_ipa_1.is_equivalent(u"atse")                  # False
s_ipa_1.is_equivalent(u"atSe")                  # False
s_ipa_1.is_equivalent(u"at͡ʃe")                  # True
s_ipa_1.is_equivalent(u"at͜ʃe")                  # True
s_ipa_1.is_equivalent(u"aʧe")                   # True
s_ipa_1.is_equivalent(u"at͡ʃeLOL", ignore=True)  # True (ignore chars non IPA valid)
s_ipa_1.is_equivalent(u"at͡ʃeLoL", ignore=True)  # False (ignore chars non IPA valid, note extra "o")


########################
# CONVERSION FUNCTIONS #
########################
s_ascii_ipa = ipa_string_to_ascii_string(s_ipa)     # IPA string to ASCII IPA (Kirshenbaum)
s_ascii_uni = unicode_string_to_ascii_string(s_uni) # Unicode string to ASCII IPA (Kirshenbaum)
s_ascii_ipa == s_ascii_uni                          # True, both are u"@'ki:n#&,k&n'TA#l@#dZi"
```

### As A Command Line Tool

**ipapy** comes with a command line tool to perform operations
on a given Unicode UTF-8 encoded string,
representing an IPA string.
Therefore, it is recommended to run it on a shell supporting UTF-8.

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

$ python -m ipapy check "LoLOL" -p -u
False
LLOL
'L'	0x4c	LATIN CAPITAL LETTER L
'O'	0x4f	LATIN CAPITAL LETTER O

$ python -m ipapy clean "/eʧiu/"
eʧiu

$ python -m ipapy u2a "eʧiu"
etSiu

$ python -m ipapy u2a "eTa"
The given string contains characters not IPA valid. Use the 'ignore' option to ignore them.

$ python -m ipapy u2a "eTa" -i
ea
```


## Unit Testing

```bash
$ python run_all_unit_tests.py
```


## License

**ipapy** is released under the MIT License.




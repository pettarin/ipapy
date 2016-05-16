# ipapy

**ipapy** is a Python module to work with IPA strings.

* Version: 0.0.1
* Date: 2016-05-16
* Developer: [Alberto Pettarin](http://www.albertopettarin.it/)
* License: the MIT License (MIT)
* Contact: [click here](http://www.albertopettarin.it/contact.html)

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

```python
# Unicode string for "achene acanthology"
s = u"əˈkiːn æˌkænˈθɑ.lə.d͡ʒi"

# check if s contains only IPA characters
from ipapy import is_valid_ipa
is_valid_ipa(s)         # True
is_valid_ipa(u"LoL")    # False (uppercase letter L is not IPA valid)

# create an IPA string from the Unicode string
from ipapy.ipastring import IPAString
s_ipa = IPAString(unicode_string=s)

# print the IPAString
print(unicode(s_ipa))                   # 'əˈkiːn æˌkænˈθɑ.lə.d͡ʒi'  (Python 2)
print(s_ipa)                            # 'əˈkiːn æˌkænˈθɑ.lə.d͡ʒi'  (Python 3)

# new IPAStrings containing only...
print(s_ipa.cns_vwl)                    # 'əkinækænθɑləd͡ʒi'         (vowels and consonants)
print(s_ipa.cns_vwl_str)                # 'əˈkinæˌkænˈθɑləd͡ʒi'      (idem + stress marks)
print(s_ipa.cns_vwl_str_len)            # 'əˈkiːnæˌkænˈθɑləd͡ʒi'     (idem + lenght marks)
print(s_ipa.cns_vwl_str_len_wb)         # 'əˈkiːn æˌkænˈθɑləd͡ʒi'    (idem + word breaks)

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

# convert IPAString to ASCII-IPA (Kirshenbaum)
from ipapy.asciiipa import ipa_string_to_ascii_string
a_s1 = ipa_string_to_ascii_string(s_ipa)                    # u"@'ki:n#&,k&n'TA#l@#dZi"

# convert Unicode string to ASCII-IPA (Kirshenbaum)
from ipapy.asciiipa import unicode_string_to_ascii_string
a_s2 = unicode_string_to_ascii_string(s)                    # u"@'ki:n#&,k&n'TA#l@#dZi"

a_s1 == a_s2    # True

# load IPA char from its Unicode representation
from ipapy import UNICODE_TO_IPA
c1 = UNICODE_TO_IPA["a"]        # open front unrounded vowel (frozenset({'unrounded', 'vowel', 'front', 'open'}))
c2 = UNICODE_TO_IPA["e"]        # close-mid front unrounded vowel (frozenset({'close-mid', 'unrounded', 'vowel', 'front'}))
c3 = UNICODE_TO_IPA[u"\u03B2"]  # voiced bilabial non-sibilant-fricative consonant (frozenset({'non-sibilant-fricative', 'bilabial', 'voiced', 'consonant'}))

# build new IPA chars
from ipapy.ipachar import IPAVowel
my_a1 = IPAVowel(name="my_a", properties="open front unrounded", unicode_repr="a")
my_a2 = IPAVowel(name="my_a", properties=["open", "front", "unrounded"], unicode_repr="a")
my_a3 = IPAVowel(name="my_a", height="open", backness="front", roundness="unrounded", unicode_repr="a")
my_a4 = IPAVowel(name="my_a", properties=["low", "fnt", "unr"], unicode_repr="a")
my_ee = IPAVowel(name="my_e", properties="close-mid front unrounded", unicode_repr="e")

from ipapy.ipachar import IPAConsonant
my_bf = IPAConsonant(name="bilabial fricative", properties="voiced bilabial non-sibilant-fricative", unicode_repr=u"\u03B2")

# compare IPA chars
my_a1 == my_a2  # True
my_a1 == my_a3  # True
my_a1 == my_a4  # True
my_a1 == my_ee  # False
my_a1 == my_bf  # False

# compare against a Unicode character (or string)
my_bf == u"\u03B2"  # True
my_bf == "β"        # True
my_bf == "b"        # False

# compare against a string listing properties (any order, known synonyms/abbreviations allowed)
my_a1 == "open front unrounded"                                 # False (missing 'vowel')
my_a1 == "open front unrounded vowel"                           # True
my_a1 == "low fnt unr vwl"                                      # True
my_ee == "open front unrounded vowel"                           # False
my_bf == "voiced bilabial non-sibilant-fricative"               # False (missing 'consonant')
my_bf == "voiced bilabial non-sibilant-fricative consonant"     # True
my_bf == "consonant non-sibilant-fricative bilabial voiced"     # True
my_bf == "consonant non-sibilant-fricative bilabial voiceless"  # False

# create IPA String from IPA chars
my_ipa_s = IPAString([my_bf, my_ee, my_ee])                     # 'βee'
```

## License

**ipapy** is released under the MIT License.




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
# Unicode string for "Italian style"
# note that the stress mark is not U+0027 but U+02C8
s = u"iˈtaljans ˈtail"

# check if s contains only IPA characters (yes)
from ipapy import is_valid_ipa
if is_valid_ipa(s):
    print("s is a valid IPA string")

# create IPA string from Unicode string
from ipapy.ipastring import IPAString
s_ipa = IPAString(unicode_string=s)

# print the IPAString
print(unicode(s_ipa))   # Python 2
print(s_ipa)            # Python 3

# new IPAStrings containing only...
s_cv = s_ipa.cns_vwl                    # vowels and consonants
s_cvs = s_ipa.cns_vwl_str               # idem + stress marks
s_cvsl = s_ipa.cns_vwl_str_len          # idem + lenght marks
s_cvslw = s_ipa.cns_vwl_str_len_wb      # idem + word breaks 

# iterate over each IPA char, print it, and,
# if it is a diacritic, print its properties
from ipapy.ipachar import IPADiacritic
for c_ipa in s_ipa:
    print(c_ipa)
    if isinstance(c_ipa, IPADiacritic):
        print(c_ipa.properties)        

# print the name and properties of all the vowels in the string
for c_ipa in [c for c in s_ipa if c.is_vowel]:
    print(u"%s => %s" % (c_ipa, c_ipa.name))

# print the name and properties of all the consonants in the string
for c_ipa in [c for c in s_ipa if c.is_consonant]:
    print(u"%s => %s" % (c_ipa, c_ipa.name))

# convert IPAString to ASCII-IPA (Kirshenbaum)
from ipapy.asciiipa import ipa_string_to_ascii_string
ascii_ipa = ipa_string_to_ascii_string(s_ipa)  # u"i'taljans#'tail"

# convert Unicode string to ASCII-IPA (Kirshenbaum)
from ipapy.asciiipa import unicode_string_to_ascii_string
ascii_ipa = unicode_string_to_ascii_string(s)  # u"i'taljans#'tail"

# load IPA char from its Unicode representation
from ipapy import UNICODE_TO_IPA
c1 = UNICODE_TO_IPA["a"]
>>> c1
open front unrounded vowel (frozenset({'unrounded', 'vowel', 'front', 'open'}))
c2 = UNICODE_TO_IPA["e"]
>>> c2
close-mid front unrounded vowel (frozenset({'close-mid', 'unrounded', 'vowel', 'front'}))
c3 = UNICODE_TO_IPA[u"\u03B2"]
>>> c3
voiced bilabial non-sibilant-fricative consonant (frozenset({'non-sibilant-fricative', 'bilabial', 'voiced', 'consonant'}))

# build new IPA chars
from ipapy.ipachar import IPAVowel
my_a1 = IPAVowel(name="my_a", properties="open front unrounded", unicode_repr="a")
my_a2 = IPAVowel(name="my_a", properties=["open", "front", "unrounded"], unicode_repr="a")
my_a3 = IPAVowel(name="my_a", height="open", backness="front", roundness="unrounded", unicode_repr="a")
my_a4 = IPAVowel(name="my_a", properties=["low", "fnt", "unr"], unicode_repr="a")
my_e = IPAVowel(name="my_e", properties="close-mid front unrounded", unicode_repr="e")

from ipapy.ipachar import IPAConsonant
my_bf = IPAConsonant(name="bilabial fricative", properties="voiced bilabial non-sibilant-fricative", unicode_repr=u"\u03B2")

# compare IPA chars
my_a1 == my_a2  # True
my_a1 == my_a3  # True
my_a1 == my_a4  # True
my_a1 == my_e   # False
my_a1 == my_bf  # False

# compare against a Unicode character (or string)
my_bf == 'β'    # True
my_bf == 'b'    # False

# compare against a string listing properties (any order, known synonyms/abbreviations allowed)
my_a1 == "open front unrounded"                                 # False (you need to specify 'vowel')
my_a1 == "open front unrounded vowel"                           # True
my_a1 == "low fnt unr vwl"                                      # True
my_e == "open front unrounded vowel"                            # False
my_bf == "voiced bilabial non-sibilant-fricative"               # False (you need to specify 'consonant')
my_bf == "voiced bilabial non-sibilant-fricative consonant"     # True
my_bf == "consonant non-sibilant-fricative bilabial voiced"     # True
my_bf == "consonant non-sibilant-fricative bilabial voiceless"  # False

# create IPA String from IPA chars
my_ipa_s = IPAString([my_bf, my_e, my_e, my_a1])                # 'βeea'
```

## License

**ipapy** is released under the MIT License.




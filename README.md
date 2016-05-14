# ipapy

**ipapy** is a Python module to work with IPA strings.

* Version: 0.0.1
* Date: 2016-05-14
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

# print the IPAString (Python 3)
print(s_ipa)

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
```

## License

**ipapy** is released under the MIT License.




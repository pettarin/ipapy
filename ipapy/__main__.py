#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.

This is the main script, intended to be run from command line.
"""

from __future__ import absolute_import
from __future__ import print_function
import argparse
import sys
import unicodedata

from ipapy import is_valid_ipa
from ipapy import remove_invalid_ipa_characters
from ipapy.asciiipa import unicode_string_to_ascii_string
from ipapy.compatibility import to_unicode_string
from ipapy.compatibility import unicode_to_hex
from ipapy.ipastring import IPAString

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Production"

DESCRIPTION = "ipapy perform a command on the given IPA/Unicode string"

ARGUMENTS = [
    {
        "long": "command",
        "short": None,
        "nargs": None,
        "type": str,
        "default": None,
        "help": "[canonize|chars|check|clean|u2a]"
    },
    {
        "long": "string",
        "short": None,
        "nargs": None,
        "type": str,
        "default": None,
        "help": "String to canonize, check, or convert"
    },
    {
        "long": "--ignore",
        "short": "-i",
        "action": "store_true",
        "help": "Ignore Unicode characters that are not IPA valid"
    },
    {
        "long": "--print-invalid",
        "short": "-p",
        "action": "store_true",
        "help": "Print Unicode characters that are not IPA valid"
    },
    {
        "long": "--single-char-parsing",
        "short": "-s",
        "action": "store_true",
        "help": "Perform single character parsing instead of maximal parsing"
    },
    {
        "long": "--unicode",
        "short": "-u",
        "action": "store_true",
        "help": "Print each Unicode character that is not IPA valid with its Unicode codepoint and name"
    },
]

def print_error(msg):
    """
    Print the given error message and exit.

    :param str msg: the error message
    """
    print(msg)
    sys.exit(1)

def print_invalid_chars(invalid_chars, vargs):
    """
    Print Unicode characterss that are not IPA valid,
    if requested by the user.

    :param list invalid_chars: a list (possibly empty) of invalid Unicode characters
    :param dict vargs: the command line parameters
    """
    if len(invalid_chars) > 0:
        if vargs["print_invalid"]:
            print(u"".join(invalid_chars))
        if vargs["unicode"]:
            for u_char in sorted(set(invalid_chars)):
                print(u"'%s'\t%s\t%s" % (u_char, hex(ord(u_char)), unicodedata.name(u_char, "UNKNOWN")))

def command_canonize(string, vargs):
    """
    Print the canonical representation of the given string. 

    It will replace non-canonical compound characters
    with their canonical synonym.

    :param str string: the string to act upon
    :param dict vargs: the command line arguments
    """
    try:
        ipa_string = IPAString(
            unicode_string=string,
            ignore=vargs["ignore"],
            single_char_parsing=vargs["single_char_parsing"]
        )
        print(ipa_string)
    except ValueError as exc:
        print_error(str(exc))

def command_chars(string, vargs):
    """
    Print a list of all IPA characters in the given string.

    It will print the Unicode representation, the full IPA name,
    and the Unicode "U+"-prefixed hexadecimal codepoint representation
    of each IPA character.

    :param str string: the string to act upon
    :param dict vargs: the command line arguments
    """
    try:
        ipa_string = IPAString(
            unicode_string=string,
            ignore=vargs["ignore"],
            single_char_parsing=vargs["single_char_parsing"]
        )
        for c in ipa_string:
            print(u"'%s'\t%s (%s)" % (c.unicode_repr, c.name, unicode_to_hex(c.unicode_repr)))
    except ValueError as exc:
        print_error(str(exc))

def command_check(string, vargs):
    """
    Check if the given string is IPA valid.

    If the given string is not IPA valid,
    print the invalid characters.

    :param str string: the string to act upon
    :param dict vargs: the command line arguments
    """
    is_valid = is_valid_ipa(string)
    print(is_valid)
    if not is_valid:
        valid_chars, invalid_chars = remove_invalid_ipa_characters(
            unicode_string=string,
            return_invalid=True
        )
        print_invalid_chars(invalid_chars, vargs)

def command_clean(string, vargs):
    """
    Remove characters that are not IPA valid from the given string,
    and print the remaining string.

    :param str string: the string to act upon
    :param dict vargs: the command line arguments
    """
    valid_chars, invalid_chars = remove_invalid_ipa_characters(
        unicode_string=string,
        return_invalid=True,
        single_char_parsing=vargs["single_char_parsing"]
    )
    print(u"".join(valid_chars))
    print_invalid_chars(invalid_chars, vargs)

def command_u2a(string, vargs):
    """
    Print the ASCII IPA string corresponding to the given Unicode IPA string. 

    :param str string: the string to act upon
    :param dict vargs: the command line arguments
    """
    try:
        print(unicode_string_to_ascii_string(
            unicode_string=string,
            ignore=vargs["ignore"],
            single_char_parsing=vargs["single_char_parsing"]
        ))
    except ValueError as exc:
        print_error(str(exc))

COMMAND_MAP = {
    "canonize": command_canonize,
    "chars": command_chars,
    "check": command_check,
    "clean": command_clean,
    "u2a": command_u2a,
}

def main():
    """
    Entry point.
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    for arg in ARGUMENTS:
        if "action" in arg:
            if arg["short"] is not None:
                parser.add_argument(arg["short"], arg["long"], action=arg["action"], help=arg["help"])
            else:
                parser.add_argument(arg["long"], action=arg["action"], help=arg["help"])
        else:
            if arg["short"] is not None:
                parser.add_argument(arg["short"], arg["long"], nargs=arg["nargs"], type=arg["type"], default=arg["default"], help=arg["help"])
            else:
                parser.add_argument(arg["long"], nargs=arg["nargs"], type=arg["type"], default=arg["default"], help=arg["help"])
    vargs = vars(parser.parse_args())
    command = vargs["command"]
    string = to_unicode_string(vargs["string"])
    if command not in COMMAND_MAP:
        parser.print_help()
        sys.exit(2)
    COMMAND_MAP[command](string, vargs)
    sys.exit(0)



if __name__ == "__main__":
    main()




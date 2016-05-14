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

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

DESCRIPTION = "ipapy converts Unicode-IPA to ASCII-IPA"

ARGUMENTS = [
    {
        "long": "command",
        "short": None,
        "nargs": None,
        "type": str,
        "default": None,
        "help": "[u2a|ucheck|uclean]"
    },
    {
        "long": "string",
        "short": None,
        "nargs": None,
        "type": str,
        "default": None,
        "help": "String to check or convert"
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
        "long": "--unicode",
        "short": "-u",
        "action": "store_true",
        "help": "Print Unicode characters that are not IPA valid with their Unicode codepoint and name"
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
    ignore = vargs["ignore"]
    if command == "u2a":
        try:
            print(unicode_string_to_ascii_string(unicode_string=string, ignore=ignore))
        except ValueError as exc:
            print_error(str(exc))
    elif command == "ucheck":
        is_valid = is_valid_ipa(string)
        print(is_valid)
        if not is_valid:
            valid_chars, invalid_chars = remove_invalid_ipa_characters(unicode_string=string, return_invalid=True)
            print_invalid_chars(invalid_chars, vargs)
    elif command == "uclean":
        valid_chars, invalid_chars = remove_invalid_ipa_characters(unicode_string=string, return_invalid=True)
        print(u"".join(valid_chars))
        print_invalid_chars(invalid_chars, vargs)
    else:
        parser.print_help()
        sys.exit(2)
    sys.exit(0)



if __name__ == "__main__":
    main()




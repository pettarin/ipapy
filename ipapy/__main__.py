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

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alberto@albertopettarin.it"
__status__ = "Development"

DESCRIPTION = "ipapy converts Unicode-IPA to/from ASCII-IPA"

ARGUMENTS = [
    {
        "long": "command",
        "short": None,
        "nargs": None,
        "type": str,
        "default": None,
        "help": "[a2u|acheck|u2a|ucheck]"
    },
    {
        "long": "string",
        "short": None,
        "nargs": None,
        "type": str,
        "default": None,
        "help": "String to check or convert"
    },
    #{
    #    "long": "--quiet",
    #    "short": "-q",
    #    "action": "store_true",
    #    "help": "Do not output"
    #},
]

def print_error(msg):
    """
    Print the given error message and exit.

    :param str msg: the error message
    """
    print(msg)
    sys.exit(1)

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
    string = vargs["string"]
    if command == "u2a":
        print("TODO")
    elif command == "a2u":
        print("TODO")
    elif command == "acheck":
        print("TODO")
    elif command == "ucheck":
        print("TODO")
    else:
        parser.print_help()
        sys.exit(2)
    sys.exit(0)



if __name__ == "__main__":
    main()




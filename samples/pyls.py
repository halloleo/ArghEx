#!/usr/bin/env python3
# coding: utf-8
#
#  Copyright © 2017 halloleo
#
#  small example how to use arghex to write a toold which passes unkown args to a unix command
#  General Public License version 3 (LGPLv3)
#
"""
py ls - an ls command that has an additional switch for python files
~~~~~~~
"""

from __future__ import print_function
import argh
import arghex
import os
import subprocess

HELP_EPILOG="""
All other options are passed down to the ls command
"""

@argh.arg('-p', '--python', help="make sure to list python files")
def main(python=False, other_args={}):
    if python:
        other_args.append('*.py')
    other_args.insert(0, 'ls')
    print("call %s with %s" % (other_args[0], " ".join(other_args[1:])))

    subprocess.call(other_args, shell=True)

if __name__ == '__main__':
    parser = arghex.ArghParserWithUnknownArgs('other_args',
                                              epilog=HELP_EPILOG)
    arghex.set_default_command(parser, main)
    argh.dispatch(parser)

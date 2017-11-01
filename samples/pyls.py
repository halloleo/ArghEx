#!/usr/bin/env python3
# coding: utf-8
#
#  Copyright © 2017 halloleo
#
#  small example how to use arghex to write a toold which passes unkown args to a unix command
#  General Public License version 3 (LGPLv3)
#
"""
pyls - an ls command that has an additional switch for python files
~~~~~~~
"""

from __future__ import print_function
import argh
import arghex
import subprocess

HELP_EPILOG="""
All other options are passed through to the ls command
"""

@argh.arg('-p', '--python', help="make sure to list python files")
def main(python=False, ls_args={}):
    if python:
        ls_args.append('*.py')
    ls_args.insert(0, 'ls')
    print("call '%s' with '%s':" % (ls_args[0], " ".join(ls_args[1:])))

    subprocess.call(ls_args, shell=True)

if __name__ == '__main__':
    parser = arghex.ArghParserWithUnknownArgs('ls_args',
                                              epilog=HELP_EPILOG)
    arghex.set_default_command(parser, main)
    argh.dispatch(parser)

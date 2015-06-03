#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jack Cherng
# Copyright (c) 2015 jfcherng
# https://github.com/jfcherng/SublimeLinter-contrib-iverilog
#
# License: MIT
#

import sublime
from SublimeLinter.lint import Linter, util


class Iverilog(Linter):
    # linter basic settings
    syntax = ('verilog')
    cmd = 'iverilog -t null'
    tempfile_suffix = 'verilog'
    error_stream = util.STREAM_BOTH

    # what kind of message should be caught?
    if sublime.platform() == 'windows':
        regex = (
            r'^([^:]+):.*:(?P<line>\d*):'
            r'.((?P<error>error)|(?P<warning>warning))?'
            r'(?P<message>.*)'
        )
    else:
        regex = (
            r'^([^:]+):(?P<line>\d+): '
            r'(?:(?P<error>error)|(?P<warning>warning): )?'
            r'(?P<message>.+)'
        )

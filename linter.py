#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jack Cherng
# Copyright (c) 2013 jfcherng
#
# License: MIT
#

from SublimeLinter.lint import Linter, util


class Iverilog (Linter):
    syntax = ('verilog')
    cmd = 'iverilog -t null'
    tempfile_suffix = 'verilog'
    # We are missing out on some errors by ignoring multiline messages.
    regex = (
        r'^([^:]+):.*:(?P<line>\d*):'
        r'.((?P<error>error)|(?P<warning>warning))?'
        r'(?P<message>.*)'
    )
    error_stream = util.STREAM_BOTH

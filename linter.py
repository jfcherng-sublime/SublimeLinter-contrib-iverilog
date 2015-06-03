#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jack Cherng
# https://github.com/jfcherng/SublimeLinter-contrib-iverilog
# Copyright (c) 2015 jfcherng
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
    multiline = False
    error_stream = util.STREAM_BOTH

    # there is a ":" in the filepath under Windows
    # like C:\SOME_FOLDERS\...\FILE
    if sublime.platform() == 'windows':
        filepath = r'[^:]+:[^:]+'
    else:
        filepath = r'[^:]+'

    # what kind of message should be caught?
    regex = (
        r'(?P<file>{0}):(?P<line>\d+): '
        r'((?P<warning>warning: )|(?P<error>error: |))'
        r'(?P<message>.*)'
        .format(filepath)
    )

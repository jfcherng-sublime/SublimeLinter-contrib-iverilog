#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Jack Cherng
# Copyright (c) 2017-2018 jfcherng
#
# License: MIT
#

from SublimeLinter.lint import Linter, util
import sublime
import SublimeLinter.lint


def get_SL_version():
    """
    Return the major version number of SublimeLinter.
    """

    return getattr(SublimeLinter.lint, 'VERSION', 3)


class Iverilog(Linter):
    # http://www.sublimelinter.com/en/stable/linter_attributes.html
    cmd = 'iverilog -t null'
    tempfile_suffix = 'verilog'
    multiline = False
    error_stream = util.STREAM_BOTH

    if get_SL_version() == 3:
        syntax = ('verilog')
    else:
        on_stderr = None  # handle stderr via split_match
        defaults = {
            'selector': 'source.verilog',
        }

    # there is a ":" in the filepath under Windows like C:\DIR\FILE
    if sublime.platform() == 'windows':
        filepath = r'[^:]+:[^:]+'
    else:
        filepath = r'[^:]+'

    # what kind of messages should be caught?
    regex = (
        r'(?P<file>{0}):(?P<line>\d+):\s*'
        r'(?:(?:(?P<warning>warning)|(?P<error>error)):)?\s*'
        r'(?P<message>.*)'
        .format(filepath)
    )

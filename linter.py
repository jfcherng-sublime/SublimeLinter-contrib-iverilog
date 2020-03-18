#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Jack Cherng
# Copyright (c) 2017-2020 jfcherng
#
# License: MIT
#

from SublimeLinter.lint import Linter
import sublime


class Iverilog(Linter):
    # http://www.sublimelinter.com/en/stable/linter_attributes.html
    name = "iverilog"
    cmd = "iverilog ${args}"
    tempfile_suffix = "verilog"
    multiline = True
    on_stderr = None

    defaults = {
        "selector": "source.verilog | source.systemverilog",
        # @see https://iverilog.fandom.com/wiki/Iverilog_Flags
        "-t": "null",
        "-g": 2012,
        "-I +": [],
        "-y +": [],
    }

    # there is a ":" in the filepath under Windows like C:\DIR\FILE
    if sublime.platform() == "windows":
        filepath_regex = r"[^:]+:[^:]+"
    else:
        filepath_regex = r"[^:]+"

    # what kind of messages should be caught?
    regex = (
        r"(?P<file>{0}):(?P<line>\d+):\s*"
        r"(?:(?:(?P<warning>warning)|(?P<error>error)):)?\s*"
        r"(?P<message>.*)"
    ).format(filepath_regex)

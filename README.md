# SublimeLinter-contrib-iverilog

This linter plugin for [SublimeLinter](https://sublimelinter.readthedocs.org)
provides an interface to [iverilog](http://iverilog.wikia.com/wiki/Main_Page) into Sublime Text.
To make this plugin work, you need to have `iverilog` installed.
This plugin will be activated with files that have the `Verilog` syntax.

By the way, I also recommend the
[Verilator Linter](https://packagecontrol.io/packages/SublimeLinter-contrib-verilator).


## Installation

SublimeLinter must be installed in order to use this plugin.
If SublimeLinter is not installed, please follow the instructions
[here](https://sublimelinter.readthedocs.org/en/latest/installation.html).

Verilog syntax highlight is not natively supplied by Sublime Text.
You may install [Sublime Text Verilog](https://sublime.wbond.net/packages/Verilog) to do the job.


### Linter installation

Before installing this plugin, you must ensure that `iverilog` is installed on your system.
To install `iverilog`, please see [this](https://iverilog.wikia.com/wiki/Installation_Guide).


### Plugin installation

Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin.
This will ensure that the plugin will be updated when new versions are available.
If you want to install from source so you can modify the source code,
you probably know what you are doing so we won't cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the `Command Palette` by <kbd>Ctrl + Shift + P</kbd> and type `install`.
   Among the commands you should see `Package Control: Install Package`.
   If that command is not highlighted, use the keyboard or mouse to select it.
   There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `iverilog`. Among the entries you should see `SublimeLinter-contrib-iverilog`.
   If that entry is not highlighted, use the keyboard or mouse to select it.


## Settings

For general information on how SublimeLinter works with settings, please see
[Settings](https://sublimelinter.readthedocs.org/en/latest/settings.html).
For information on generic linter settings, please see
[Linter Settings](https://sublimelinter.readthedocs.org/en/latest/linter_settings.html).


## Demo

![linting_example](https://raw.githubusercontent.com/jfcherng/SublimeLinter-contrib-iverilog/gh-pages/images/linting_example.png)


## Contributing

If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Probably format codes with [black](https://github.com/psf/black) code formatter.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!


Supporters <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ATXYY9Y78EQ3Y" target="_blank"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" /></a>
==========

Thank you guys for sending me some cups of coffee.

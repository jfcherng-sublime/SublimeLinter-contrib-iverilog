SublimeLinter-contrib-iverilog
==============================

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [iverilog](http://iverilog.wikia.com/wiki/Main_Page) into Sublime Text.
It will be used with files that have the "Verilog" syntax.


Installation
============

SublimeLinter 3 must be installed in order to use this plugin.
If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

Verilog syntax highlight is not natively supplied by Sublime Text.
You may install [Sublime Text Verilog](https://sublime.wbond.net/packages/Verilog) to do the job.


## Linter installation

Before installing this plugin, you must ensure that `iverilog` is installed on your system.
To install `iverilog`, please see [this](http://iverilog.wikia.com/wiki/Installation_Guide).


## Plugin installation

Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin.
This will ensure that the plugin will be updated when new versions are available.
If you want to install from source so you can modify the source code, you probably know what you are doing so we won't cover that here.

To install via Package Control, do the following:

0. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`.
   Among the commands you should see `Package Control: Install Package`.
   If that command is not highlighted, use the keyboard or mouse to select it.
   There will be a pause of a few seconds while Package Control fetches the list of available plugins.

0. When the plugin list appears, type `iverilog`. Among the entries you should see `SublimeLinter-contrib-iverilog`.
   If that entry is not highlighted, use the keyboard or mouse to select it.


Settings
========

For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html).
For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).


## Examples

![linting_example](https://raw.githubusercontent.com/jfcherng/SublimeLinter-contrib-iverilog/gh-pages/images/linting_example.png)


## Constraints

If your module references design(s) from other .v file(s), you must use ```include "module.v"`` to include them for this linting plugin.

For example, one of ways to do a simulation is `iverilog module.v module_t.v -o a.out` where `module_t.v` is a testbench file.
This way does not use the ```include`` syntax in `module_t.v` but lists files in the command line.
Therefore, you will see ``Unknown module type: module`` in `module_t.v` since this plugin only check the current file.
To avoid this, you have to modify `module_t.v` to include `module.v` and use `iverilog module_t.v -o a.out` instead.

![include_module_file](http://jfcherng.github.io/SublimeLinter-contrib-iverilog/images/include_module_file.png)

You may use "include guard" to prevent from module redefinition.

```verilog
`ifndef _MODULE_
`define _MODULE_
    // your module design here
`endif
```

But honestly, this is pretty annoying and `iverilog module.v module_t.v -o a.out` is more sweet for scripts...


Contributing
============

If you would like to contribute enhancements or fixes, please do the following:

0. Fork the plugin repository.
0. Hack on a separate topic branch created from the latest `master`.
0. Commit and push the topic branch.
0. Make a pull request.
0. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don't be afraid to use it.

Thank you for helping out!


License
=======

The MIT License (MIT)

Copyright (c) 2016 Jack Cherng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

SublimeLinter-contrib-iverilog has been updated. To see the changelog, visit
Preferences » Package Settings » SublimeLinter-contrib-iverilog » CHANGELOG


# SublimeLinter-contrib-iverilog 2.1.2

- Update readme.

  It looks like the `-i` flag is only supported in the `master` branch of `iverilog`.
  It's used to ignore `Unknown module type: XXX` linting error.
  I **strongly** recommend use the `-i` flag rather than writing `` `include`` everywhere.

  To use the `-i` flag and the `master` branch of `iverilog`, please see https://git.io/fjH92.

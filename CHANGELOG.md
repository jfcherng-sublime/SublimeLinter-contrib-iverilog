## 2.1.4

No changes. Just to annotate that this is the last version for Sublime Text 3.
The next release will only run in Sublime Text 4 (or later) with its Python 3.8 plugin host.

## 2.1.3

- Enabled in `source.systemverilog` as well.

## 2.1.2

- Update readme.

  It looks like the `-i` flag is only supported in the `master` branch of `iverilog`.
  It's used to ignore `Unknown module type: XXX` linting error.
  I **strongly** recommend use the `-i` flag rather than writing `` `include`` everywhere.

  To use the `-i` flag and the `master` branch of `iverilog`, please see https://git.io/fjH92.

## 2.1.1

- Revert "No longer emits error about module not found."

## 2.1.0

- No longer emits error about module not found.

## 2.0.0

- Drop support for SublimeLinter 3.

## 1.1.0

- Compatible with SublimeLinter 4.6.2.

## 1.0.4

- Just some directory structure tweaks.

## 1.0.0

- Initial release.

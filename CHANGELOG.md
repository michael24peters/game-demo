# Changelog

## v0.0.6
- Updated docstrings
- Added update_stat()
- Moved create_character() functionality to update_stat()
- Fixed: can now add skill points to languages
- Changed create_character
  - Displays all languages

## v0.0.5
- Added NPC subclass
  - __init__()
- Changes to Character
  - If name and background given in constructor args, skip create_character() and use default values
  - __str__() now formatted to look like proper character sheet
- Added supermemo()
- Finished create_character()
- Added report.md

## v0.0.4
- Added methods for Character
  - create_character() (WIP)
  - __str__()

## v0.0.3
- Added noxfile.py
- Added pyproject.toml
- Added ci.yaml
- Added tests/test_character.py with dummy method for debugging
- Added .gitignore

## v0.0.2
- Added sphinx documentation support
  - Added docs/conf.py
  - Added docs/index.rst
  - Added docs/make.bat
  - Added docs/Makefile

## v0.0.1
- Added character.py
- Added CHANGELOG.py
# Changelog

All notable changes to the Get Recent Sublime Text Files action are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-03

### Fixed

- LaunchBar named the action "Recent Sublime Text Projects" and described it as a list of Sublime Text 3 files; it now names it "Recent Sublime Opened Files", a list of files recently opened in Sublime Text 4.

### Changed

- The action requires macOS 12.0 or later (`LSMinimumSystemVersion`; was 10.10).
- `Get-Recent-ST-Files-For-LaunchBar.zip` is attached to each GitHub release, with a build provenance attestation, instead of `Action.zip`.

### Removed

- `open_with_sublime.py`, which the action never ran.

[Unreleased]: https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar/compare/1.0.1...v1.1.0

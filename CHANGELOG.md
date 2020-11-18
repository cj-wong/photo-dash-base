# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.1] - 2020-11-17
### Changed
- In [base.sh], additional code should go into the `else`, not outside the conditionals. Because `exit` can't be used in sourced files, all code that depends on a working configuration must go into the `else`.

## [0.1.0] - 2020-11-14
### Added
- Initial version

[base.sh]: base.sh

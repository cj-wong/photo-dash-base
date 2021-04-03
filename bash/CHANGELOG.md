# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.3] - 2021-04-03
### Changed
- Cleaned up documentation (return codes).

### Fixed
- Fixed parameter substitution of `+x` in `[ -z "${matched_name+x}" ]` to `:+x`; this checks both whether `$matched_name` is empty and whether `$matched_name` was declared. Specifically, in the old syntax, if `$matched_name` was empty but declared, it would be substituted with `x`. In the new syntax, the substitution only takes place if `$matched_name` is empty (regardless of declaration).
- Fixed incorrect condition `if [[ -z "${QUIET_START:+x}" || -z "${QUIET_START:+x}" ]]`: the second `QUIET_START` has been changed to `QUIET_END`.

## [0.1.2] - 2021-01-05
### Changed
- [bash]/[base.sh] now suppresses `curl` output except for errors when retrieving quiet hours.

## [0.1.1] - 2020-11-17
### Added
- Added a snippet in [example.sh] that stops execution of the main script if quiet hours are in effect.

### Changed
- Likewise to the above, in [base.sh], quiet hours are checked *before* executing any code (but after dependency checks) to see if the file already exists and sources it if so. **The weakness of this change is that quiet hours cannot be updated while they were previously in effect.** If quiet hours were changed on the endpoint during the previous quiet hours, the script won't attempt to update until the previous quiet hours are no longer in effect. On the flip side, the endpoint won't be requested as much.

### Fixed
- In [base.sh], additional code should go into the `else`, not outside the conditionals. Because `exit` can't be used in sourced files, all code that depends on a working configuration must go into the `else`.

## [0.1.0] - 2020-11-14
### Added
- Initial version

[base.sh]: base.sh
[example.sh]: example.sh

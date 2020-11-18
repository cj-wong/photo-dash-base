# base.py module for [photo-dash]

## Overview

The `photo-dash` project is a series of modules and an endpoint. This repository specifically is the base module in Python from which all other Python-based modules should inherit.

Specifically, in [photo_dash_MODULE], both [base.py] and [config.py] are provided barebones.

## Usage

Clone (and fork) the repository to create modules in Python for `photo-dash`.

## Requirements

This code is designed around the following:

- Python 3.7+
    - `pendulum`
    - `requests`

## Setup

1. Rename the `MODULE` in the module directory [photo_dash_MODULE]. You must use underscores here, as Python cannot import names with dashes.
2. Similarly, change `_LOGGER_NAME` in [config.py] to match the new module directory name. Note that the delimiter here is a dash (`-`), not an underscore (`_`), which should match the project name.
3. Add any extra config-level changes to [config.py]. They should be inserted within the sections marked with `pass`: after `ENDPOINT` in the `try: except:` block, and one at the end of the file. At this step, you can also make changes to the provided [configuration](config.json.example) to suit the new module.
4. Add a new module in the directory and create a class that subclasses `base.BaseModule`. Run `self.setup_quiet_hours()` at least once, preferably near initialization in the inheriting class. Whenever quiet hours are needed, use `self.in_quiet_hours()`.
5. Add the module to [\_\_init\_\_.py](photo_dash_MODULE/__init__.py).

## Disclaimer

See [LICENSE](../LICENSE) for more detail.

[photo-dash]: https://github.com/cj-wong/photo-dash
[photo_dash_MODULE]: photo_dash_MODULE
[base.py]: photo_dash_MODULE/base.py
[config.py]: photo_dash_MODULE/config.py

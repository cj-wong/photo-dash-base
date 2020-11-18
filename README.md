# Base modules for [photo-dash]

## Overview

The `photo-dash` project is a series of modules and an endpoint. This repository contains all of the base modules, separated by language, to simplify the module creation process.

New modules should subclass or import the base modules to take advantage of universal functionality. Currently, that includes reading quiet hours from the endpoint and checking whether quiet hours is in effect at any specific moment.

Each base module contains documentation on requirements (dependencies) and how to use it. For example, the [Python](python) module uses both a [configuration loader](python/photo_dash_MODULE/config.py) and a [base class](python/photo_dash_MODULE/base.py).

## Disclaimer

See [LICENSE](LICENSE) for more detail.

[photo-dash]: https://github.com/cj-wong/photo-dash

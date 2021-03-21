import json
import logging
import logging.handlers


_LOGGER_NAME = 'photo-dash-MODULE'

LOGGER = logging.getLogger(_LOGGER_NAME)
LOGGER.setLevel(logging.DEBUG)

_FH = logging.handlers.RotatingFileHandler(
    f'{_LOGGER_NAME}.log',
    maxBytes=40960,
    backupCount=5,
    )
_FH.setLevel(logging.DEBUG)

_CH = logging.StreamHandler()
_CH.setLevel(logging.WARNING)

_FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
_FH.setFormatter(_FORMATTER)
_CH.setFormatter(_FORMATTER)

LOGGER.addHandler(_FH)
LOGGER.addHandler(_CH)

_CONFIG_LOAD_ERRORS = (
    FileNotFoundError,
    KeyError,
    TypeError,
    ValueError,
    json.decoder.JSONDecodeError,
    )

try:
    with open('config.json', 'r') as f:
        CONFIG = json.load(f)
    ENDPOINT = CONFIG['endpoint']
    # Module-specific config continues below
    pass
    # Module-specific config ends here
except _CONFIG_LOAD_ERRORS as e:
    LOGGER.error('config.json doesn\'t exist or is malformed.')
    LOGGER.error(f'More information: {e}')
    raise e

# Remaining module-specific code continues below

pass

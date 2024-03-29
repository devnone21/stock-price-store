import os
import json
import logging.config
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

_logging_json = {
  "version": 1,
  "disable_existing_loggers": False,
  "formatters": {
    "default": {
      "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
      "datefmt": "%Y-%m-%d %H:%M:%S"
    }
  },
  "handlers": {
    "console": {
      "class": "logging.StreamHandler",
      "formatter": "default"
    },
    "rotating": {
      "class": "logging.handlers.TimedRotatingFileHandler",
      "formatter": "default",
      "filename": os.getenv("LOG_PATH", default="store.log"),
      "when": "midnight",
      "backupCount": 3
    }
  },
  "loggers": {
    "": {
      "handlers": ["console"],
      "level": "CRITICAL",
      "propagate": True
    },
    "xtb": {
      "handlers": ["rotating"],
      "level": "DEBUG"
    }
  }
}
logging.config.dictConfig(_logging_json)

accounts: dict = json.load(open('xtb/account.json'))
settings: dict = json.load(open('xtb/settings.json'))
user = settings.get('user', '')
symbols = settings.get('symbols', [])
timeframes = settings.get('timeframes', [])
# symbols = ['GOLD', 'GOLD.FUT']
# timeframes = [15, 30]

"""This module defines variables that are used by 'main.py' and provide a standard import for cogs

THIS MODULE SHOULD NOT BE EDITED!
"""
import os
import dotenv
import logging
from typing import Any
from importlib import import_module
from disnake.ext.commands.cog import Cog


class ConfigurationError(BaseException):
    """Error used to indicate that this container is improperly configured"""


# Load environment variables
dotenv.load_dotenv()
ENV = dict(os.environ)

# Configure disnake
DISCORD_TOKEN = ENV.get("DISCORD_TOKEN")
DISCORD_TESTING_GUILD_ID = ENV.get("DISCORD_TESTING_GUILD_ID")

if not DISCORD_TOKEN:
    raise ConfigurationError("the environment variable 'DISCORD_TOKEN' must be defined")

if DISCORD_TESTING_GUILD_ID:
    try:
        DISCORD_TESTING_GUILD_ID = int(DISCORD_TESTING_GUILD_ID)
    except ValueError:
        raise ConfigurationError(
            "the environment variable 'DISCORD_TESTING_GUILD_ID' must be a positive integer if it is defined"
        )

# Configure logging
LOG_BACKUP_COUNT = ENV.get("LOG_BACKUP_COUNT", 7)
LOG_LEVEL = ENV.get("LOG_LEVEL", logging.INFO)

logger = logging.getLogger("disnake")

if LOG_BACKUP_COUNT:
    try:
        LOG_BACKUP_COUNT = int(LOG_BACKUP_COUNT)
    except ValueError:
        raise ConfigurationError(
            "the environment variable 'LOG_BACKUP_COUNT' must be a positive integer if it is defined"
        )

try:
    logger.setLevel(LOG_LEVEL)
except TypeError:
    raise ConfigurationError(
        "the environment variable 'LOG_LEVEL' must be the name of logging level or a positive integer if it is defined"
    )
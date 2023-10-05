"""This module defines variables that are used by 'main.py' and provide a standard import for cogs

THIS MODULE SHOULD NOT BE EDITED!
"""
import os
import logging
from logging import StreamHandler, Formatter
from logging.handlers import TimedRotatingFileHandler
from disnake import Intents
from disnake.ext import commands


def bot_intents(bot: commands.Bot):
    """Returns a mutable view of the bot's configured intents"""
    return bot._connection._intents


class ConfigurationError(BaseException):
    """Error used to indicate that this container is improperly configured"""


# Load environment variables
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


# Perform additional logging configuration
formatter = Formatter("%(asctime)s:%(levelname)s:%(message)s")

log_path = "/app/logs/disnake-core.log"
log_handler = TimedRotatingFileHandler(
    log_path, when="d", interval=1, backupCount=LOG_BACKUP_COUNT
)
log_handler.setFormatter(formatter)

stdout_handler = StreamHandler()
stdout_handler.setFormatter(formatter)

logger.addHandler(log_handler)
logger.addHandler(stdout_handler)

# Configure the bot
TEST_GUILDS = [DISCORD_TESTING_GUILD_ID] if DISCORD_TESTING_GUILD_ID else []
COMMAND_SYNC_FLAGS = commands.CommandSyncFlags.default()
INTENTS = Intents.default()

"""This module defines the 'bot' instance used by the container

This module can be safely edited as long as it exports an instance called 'bot' that extends 'disnake.Client'.
"""
from common import *
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler
from disnake import Intents
from disnake.ext import commands
from disnake.ext.commands import InteractionBot

# Perform additional logging configuration
log_path = "/app/logs/disnake-core.log"
log_handler = TimedRotatingFileHandler(
    log_path, when="d", interval=1, backupCount=LOG_BACKUP_COUNT
)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.addHandler(StreamHandler())

# Configure the bot
TEST_GUILDS = [DISCORD_TESTING_GUILD_ID] if DISCORD_TESTING_GUILD_ID else []
COMMAND_SYNC_FLAGS = commands.CommandSyncFlags.default()
INTENTS = Intents.default()
# INTENTS.members = True

# To use a different bot as the base, edit this file
bot = InteractionBot(
        test_guilds=TEST_GUILDS, intents=INTENTS, command_sync_flags=COMMAND_SYNC_FLAGS
    )

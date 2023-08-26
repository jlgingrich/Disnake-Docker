"""This module is executed by the container to load the cogs and run the bot

THIS MODULE SHOULD NOT BE EDITED!
"""
from common import *
import multiprocessing
import asyncio
from disnake.utils import search_directory
from disnake.ext.commands import InteractionBot
from disnake.ext.commands.errors import ExtensionError
from watchfiles import watch, Change

# Import and check bot
from bot import bot

if not isinstance(bot, InteractionBot):
    raise ConfigurationError(
        "the imported 'bot' in 'bot.py' is not a subclass of 'disnake.ext.commands.InteractionBot'"
    )

# Load extensions

EXT_PATH = "exts"
for extension in search_directory(EXT_PATH):
    try:
        bot.load_extension(extension)
        logger.info(f"Loaded '{extension}'")
    except:
        logger.info(f"Failed to load '{extension}'")

# Run the bot!
logger.info(f"Bot '{bot.__class__.__name__}' started successfully")
bot.run(DISCORD_TOKEN)

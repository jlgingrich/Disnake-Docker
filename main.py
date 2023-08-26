"""This module is executed by the container to load the cogs and run the bot

THIS MODULE SHOULD NOT BE EDITED!
"""
from common import *
from disnake.utils import search_directory
from disnake.ext.commands import InteractionBot
from disnake.ext.commands.errors import ExtensionError

# Import and check bot
from bot import bot

if not isinstance(bot, InteractionBot):
    raise ConfigurationError(
        "the imported 'bot' in 'bot.py' is not a subclass of 'disnake.ext.commands.InteractionBot'"
    )

# Load extensions

for extension in search_directory("exts"):
    try:
        bot.load_extension(extension)
        logger.info(f"Loaded '{extension}'")
    except ExtensionError:
        logger.info(f"Failed to load '{extension}'")

# Run the bot!
logger.info(f"Bot '{bot.__class__.__name__}' started successfully")
bot.run(DISCORD_TOKEN)

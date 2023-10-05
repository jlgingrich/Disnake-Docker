"""This module is executed by the container to load the cogs and run the bot

THIS MODULE SHOULD NOT BE EDITED!
"""
from common import TEST_GUILDS, INTENTS, COMMAND_SYNC_FLAGS, DISCORD_TOKEN, logger
from disnake.utils import search_directory
from disnake.ext.commands import InteractionBot
from disnake.ext.commands.errors import ExtensionError

bot = InteractionBot(
    test_guilds=TEST_GUILDS, intents=INTENTS, command_sync_flags=COMMAND_SYNC_FLAGS
)

# Load extensions

for extension in search_directory("exts"):
    try:
        bot.load_extension(extension)
        logger.info(f"Loaded '{extension}'")
    except ExtensionError as e:
        logger.info(f"Failed to load {extension!r} due to below errors:\n\t{e}")

# Run the bot!
logger.info(f"Bot started successfully")
bot.run(DISCORD_TOKEN)

"""This module is executed by the container to load the cogs and run the bot

THIS MODULE SHOULD NOT BE EDITED!
"""
from disnake.ext import commands
import disnake
from loguru import logger
from bot import Bot
import os
import sys
import asyncio

# Read environment variables
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError("the environment variable 'DISCORD_TOKEN' must be defined")

try:
    TEST_GUILDS = [
        int(guild_id)
        for guild_id in os.environ.get("DISCORD_TESTING_GUILDS").split(":")
    ]
except ValueError:
    raise ValueError(
        "the environment variable 'DISCORD_TESTING_GUILDS' must be a list of integers separated by colons"
    )


# Configure logging
logformat = "{time} | {level} | {message}"
logger.remove(0)
logger.add(sys.stderr, format=logformat, level="SUCCESS")
logger.add("/app/logs/disnake.log", rotation="500 MB", format=logformat, level="INFO")

# Run bot process


async def main():
    bot = Bot(test_guilds=TEST_GUILDS)
    bot.load_extensions("core/plugins")
    await bot.start(DISCORD_TOKEN)


asyncio.run(main())

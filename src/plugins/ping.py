"""A sample plugin for testing purposes"""
from loguru import logger
from disnake import CommandInteraction, Member
from disnake.ext import plugins

plugin = plugins.Plugin()


@plugin.slash_command()
async def ping(inter: CommandInteraction):
    """Make sure that the bot is working."""
    await inter.response.send_message("Pong!", ephemeral=True)
    logger.success(f"Responsed to ping from '{inter.author.name}'")


setup, teardown = plugin.create_extension_handlers()

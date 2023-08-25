"""This module shows an example cog that will be loaded into the bot

This module can be used as a base for other cogs.
"""
from common import logger
from typing import Optional
from disnake import Member
from disnake.ext.commands import slash_command
from disnake.ext.commands.cog import Cog


class Greetings(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @slash_command()
    async def hello(self, ctx, *, member: Optional[Member] = None):
        """Says hello to you or someone else!"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}!")
        else:
            await ctx.send(f"Hello {member.name}!\n*This feels familiar...*")
        self._last_member = member
        logger.info(f"Greeted {member.name}")

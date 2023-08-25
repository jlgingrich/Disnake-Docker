"""This module shows an example cog that will always fail on load

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
    async def error(self, ctx, *, member: Optional[Member] = None):
        """You'll never see this command description!"""
        A = 12sa

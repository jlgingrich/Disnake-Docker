import os, platform
from disnake.flags import Intents
from loguru import logger

import disnake
from disnake.ext import commands
from disnake.ext.commands import Context, InteractionBot
from disnake import ApplicationCommandInteraction


class Bot(InteractionBot):
    """An overridden version of the Bot class with extra logging"""

    def __init__(self, config=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def intents(self) -> Intents:
        """Returns a mutable version of the bot's Intents so that plugins can declare privileged intents on setup."""
        return self._connection._intents

    def load_extensions(self, path: str):
        exts = [".".join(ext.split('.')[1:]) for ext in disnake.utils.search_directory(path)]
        count = 0
        for ext in exts:
            try:
                self.load_extension(ext)
                logger.success(f"Load ext: '{ext}' complete.")
                count += 1
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                logger.error(f"Unable to load extension: {ext}\n{exception}.")

        logger.info(f"{count} extension(s) have loaded successfully.")

    async def on_connect(self) -> None:
        logger.success("Bot is connected to the gateway.")
        logger.info(f"Connected to {len(self.guilds)} guild(s.)")
        logger.info(f"Logged in as {self.user.name} ({self.user.id})")
        logger.info(f"API Version: {disnake.__version__}")
        logger.info(f"Platform: {platform.system()} {platform.release()} {os.name}")

    async def on_ready(self) -> None:
        logger.success("Bot is ready.")

    async def on_command_error(self, ctx: Context, error) -> None:
        if isinstance(error, commands.errors.CommandNotFound):
            return

        logger.error(f"Ignoring exception in command {ctx.command}: {error}")

    async def on_slash_command_error(
        self, inter: ApplicationCommandInteraction, error
    ) -> None:
        if isinstance(error, commands.errors.CommandNotFound):
            return

        logger.error(
            f"Ignoring exception in slash command {inter.application_command.name}: {error}"
        )

"""This module is executed by the container to load the cogs and run the bot

THIS MODULE SHOULD NOT BE EDITED!
"""
from common import *
from disnake import Client

# Import and check bot
from bot import bot

if not isinstance(bot, Client):
    raise ConfigurationError(
        "the imported 'bot' in 'bot.py' is not a subclass of 'disnake.Client'"
    )

# Import and install cogs
for cogfile in [
    f[:-3]
    for f in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/cogs")
    if f.endswith(".py")
]:
    try:
        mod = import_module(f".{cogfile}", "cogs")
    except (ImportError, SyntaxError):
        # If a cogfile failed to load, skip it
        logger.error(f"Failed to load cogs from '{cogfile}'")
        continue
    for cog_class in [
            getattr(mod, x)
            for x in dir(mod)
            if isinstance(getattr(mod, x), type) and getattr(mod, x) != Cog and issubclass(getattr(mod, x), Cog)
        ]:
            try:
                cog = cog_class(bot)
                bot.add_cog(cog)
            except BaseException as e:
                logger.error(f"Failed to load cog '{cog_class.__name__}':")
                logger.error(e)
            logger.info(f"Loaded cog '{cog_class.__name__}' from '{cogfile}'")



# Run the bot!
logger.info(f"Bot {bot.__class__.__name__} started successfully")
bot.run(DISCORD_TOKEN)

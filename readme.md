# Disnake-Docker

This container image provides a simple way to rapidly iterate on Discord bots using the [Disnake](https://docs.disnake.dev/en/stable/index.html) Python library.

## Use

The easiest way to use this image is to create a `docker-compose.yaml` like the one below:

```yaml
name: my-disnake-container

volumes:
  data:
  logs:

services:
  core:
    container_name: core
    build:
      dockerfile_inline: |
        FROM jlgingrich/disnake
        COPY ./cogs ./cogs
    env_file:
      - .env
    volumes:
      - data:/app/data
      - logs:/app/logs

```

The inline `Dockerfile` here is essential, as it allows you to add a folder of Python files containing [Cogs](https://docs.disnake.dev/en/stable/ext/commands/cogs.html) to the final image. The `.env` file contains the `DISCORD_TOKEN` used by the bot to connect to Discord and can contain other environment variables used to modify the image. See [example.env](./example.env) for the other suggested environment variables.

## Structure
```
app
├── common.py
├── bot.py
├── main.py
├── cogs
│   ├── examples.py
│   ├── bad_cog.py
│   └── ...
├── data
│   └── ...
└── logs
   └── ...
```

### `common.py`
This module defines variables that are used by `main.py` and provide a standard import for cogs. This module should not be directly edited, but can be imported from any cog in `/app/cogs` or a custom `bot.py`.

### `bot.py`
This module defines the 'bot' instance used by the container. For most cogs, this file doesn't need to be changed. However, it can be overridden with a different file to have `main.py` use a different subclass of `disnake.Client`. See [bot.py](./bot.py) for more details.

### `main.py`
This module is executed by the container to load the cogs and run the bot. This module should not be directly edited, and represents the primary automation component provided by this image.

### `app/cogs`
This directory is where Cogs can be defined to be automatically imported and attached to the bot at container startup.

### `app/data`
This is a volume where persistant data can be stored by the bot. This is not used by this base image.

### `app/logs`
This is a volume where persistant logs can be stored by the bot. The default logging configuration provided by the base image puts a timed rotating log here named `disnake-core.log`.

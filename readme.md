# disnake-docker

This container image provides a simple way to develop Discord bots using the [Disnake](https://docs.disnake.dev/en/stable/index.html) Python library. It comes with Python 3.11, the `disnake` library, several community-developed extensions for `disnake`, and a default bot setup that can be easily extended through plugins.

This base image is built and available on [Docker Hub](https://hub.docker.com/r/jlgingrich/disnake) and can be pulled with `docker pull jlgingrich/disnake:latest`.

## Use

```text
project/
├── Dockerfile
├── data/
└── plugins/
```

`./Dockerfile`

```Dockerfile
# Using this base image
FROM jlgingrich/disnake

# Install any new requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

# Copy in new plugins
COPY ./plugins /app/core/plugins
COPY ./data /app/data
# Remove the testing plugin
RUN rm app/core/plugins/ping.py

# Run the CMD from the base image on start
```

## Structure

```text
/app/
├── core/            # Code central to the container, probably don't modify
│   ├── bot.py         # An improved subclass of disnake.InteractionBot
│   ├── main.py        # The launch script for the container
│   └── plugins/       # The folder where plugins will be loaded from
│       └── ping.py      # An example plugin that responds to a slash command
├── data/            # Can be set up as a volume for persistant data
└── logs/            # Logs output here, should be set as a volume
```

## Utilities

### Loguru

[Loguru](https://loguru.readthedocs.io/en/stable/) is a library intended to make Python logging less painful by adding a bunch of useful functionalities that solve caveats of the standard loggers. Using logs in your application should be an automatism, Loguru tries to make it both pleasant and powerful.

### Components

[Components](https://github.com/DisnakeCommunity/disnake-ext-components) is a `disnake` extension aimed at making component interactions with listeners somewhat less cumbersome.

### Plugins

[Plugins](https://github.com/DisnakeCommunity/disnake-ext-plugins) is a `disnake` extension that replaces cogs. No more pointless inheritance, no more singleton classes serving as little more than a namespace, and no more unexpected behaviour when you get anywhere near the inner workings of your extensions.

### Formatter

[Formatter](https://github.com/DisnakeCommunity/disnake-ext-formatter) is a `disnake` extension that provides a `string.Formatter` subclass with special handling for `disnake` objects to hide attributes that shouldn't be otherwise exposed.

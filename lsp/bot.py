import os

import hikari
import lightbulb
import uvloop
from dotenv import load_dotenv

from lsp.core import color_logs
from lsp.errors import *
import aiohttp

load_dotenv()


bot = lightbulb.BotApp(
    TOKEN=os.getenv("TOKEN"), banner=None, ignore_bots=True, intents=hikari.Intents.ALL,
)


@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()


@bot.listen()
async def on_started(event: hikari.StartedEvent) -> None:
    update_presence.start()


bot.load_extensions_from("./lsp/plugins/", must_exist=True)


if os.name != "nt":
    uvloop.install()

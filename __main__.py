# Local imports
import modules.simple_logger as logger
import modules.env as env

# locales import
import modules.locales.pl_PL as pl_PL
import modules.locales.en_US as en_US

# 3-rd party imports
import asyncio, os, nextcord
from nextcord.ext import commands

# Logger configuration
log = logger.LOG(level = 0, filename = "latest.log", filepath = "logs/")

# Client configuration
bot = commands.Bot(
    command_prefix = '!s',
    intents = nextcord.Intents.all(),
    loop = asyncio.get_event_loop(),
    case_insensitive = True,
    help_command = None
)

@bot.event
async def on_ready():
    # Fires when bot connects to Discord and is ready to operate
    log.info(f"Logged in as: {bot.user}")

@bot.event
async def on_disconnect():
    # Fires when bot disconnects from Discord
    log.warn("Lost connection to Discord.")

@bot.event
async def on_member_join(member):
    pass

@bot.event
async def on_member_remove(member):
    pass

@bot.event
async def on_command_error(ctx, error):
    # Error handling
    pass

@bot.event
async def on_message(message):
    pass

@bot.event
async def on_raw_message_edit(payload: nextcord.RawMessageUpdateEvent):
    pass

@bot.event
async def on_raw_message_delete(payload: nextcord.RawMessageDeleteEvent):
    pass

# Loading cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        log.debug(f'{filename} Cog has been loaded')

if __name__ == "__main__":
    log.debug(f"Starting S-bot at version: {env.VER}")
    bot.run(env.TOKEN, reconnect=True)
    log.save("time")
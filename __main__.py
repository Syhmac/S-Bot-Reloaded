# Local imports
import modules.simple_logger as logger
import modules.env as env
import modules.utils as utils
import modules.errors as botErr

# 3-rd party imports
import asyncio, os, nextcord, sqlite3
from nextcord.ext import commands
from nextcord import Interaction
from cooldowns import CallableOnCooldown

# Logger configuration
log = logger.LOG(level = 0, filename = "latest.log", filepath = "logs/")

# Client configuration
bot = commands.Bot(
    command_prefix = '!s',
    intents = nextcord.Intents.all(),
    loop = asyncio.new_event_loop(),
    case_insensitive = True,
    help_command = None
)

# Make sure that database file exists and contains the necessary tables
dbCon = sqlite3.connect('database.db')
cursor = dbCon.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS economy (
balance_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
server_id INTEGER NOT NULL,
balance INTEGER NOT NULL DEFAULT 0,
jobs_done INTEGER NOT NULL DEFAULT 0,
job_earn_mult REAL NOT NULL DEFAULT 1.0,
gambling_wins INTEGER NOT NULL DEFAULT 0,
gambling_losses INTEGER NOT NULL DEFAULT 0,
fish_caught INTEGER NOT NULL DEFAULT 0,
fish_sell_mult REAL NOT NULL DEFAULT 1.0,
crimes_committed INTEGER NOT NULL DEFAULT 0)
''')

@bot.event
async def on_ready():
    # Fires when bot connects to Discord and is ready to operate
    log.info(f"Logged in as: {bot.user}. Bot is ready to operate.")

@bot.event
async def on_disconnect():
    # Fires when bot disconnects from Discord
    log.info("Lost connection to Discord.")

async def on_resumed():
    # Fires when bot resumes connection to Discord after a disconnect
    log.info("Connection to Discord has been resumed.")

@bot.event
async def on_member_join(member):
    pass

@bot.event
async def on_member_remove(member):
    pass

@bot.event
async def on_application_command_error(interaction: Interaction, error: Exception):
    # Error handling
    original = getattr(error, "original", error)
    locale = utils.resolveServerLocale(interaction)
    errorMessage = ""
    if isinstance(original, nextcord.Forbidden):
        errorMessage = locale.errorForbidden
    elif isinstance(original, commands.MissingPermissions):
        errorMessage = locale.errorNoPermission
    elif isinstance(original, CallableOnCooldown):
        errorMessage = locale.errorCooldown.format(time = round(original.retry_after))
    elif isinstance(original, botErr.InsufficientBalance):
        errorMessage = locale.errorInsufficientBalance.format(amount_needed = original.amount_needed, amount_got = original.amount_got)

    # send the error Message if exists
    if errorMessage != "":
        if interaction.response.is_done():
            await interaction.followup.send(errorMessage)
            return
        else:
            await interaction.response.send_message(errorMessage)
            return

    # Fallback for unexpected errors
    if interaction.response.is_done():
        await interaction.followup.send(locale.errorUnexpected)
    else:
        await interaction.response.send_message(locale.errorUnexpected)
    log.error(f"An error occurred while executing a command: {type(original)} | {error}")

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
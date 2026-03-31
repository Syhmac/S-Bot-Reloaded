from __main__ import bot, log

# locales
import modules.locales.en_US as en_US
import modules.locales.pl_PL as pl_PL
import modules.utils as utils

import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption
from nextcord import ChannelType
from nextcord import Locale as Loc

class UTILS(commands.Cog, name='utility', description='Utility commands'):
    """
    Selection of utility commands that might be handy for all the users.
    Available commands:
    """

    def __init__(self, bot):
        self.count = 0
        self.bot = bot

    @bot.slash_command(
        name = en_US.pingCommandName,
        name_localizations={Loc.pl: pl_PL.pingCommandName},
        description= en_US.pingCommandDescription,
        description_localizations={Loc.pl: pl_PL.pingCommandDescription}
    )
    async def ping(self, interaction: Interaction):
        locale = utils.resolveServerLocale(interaction)
        await interaction.response.send_message(locale.pingCommandResponse.format(latency=round(self.bot.latency * 1000)))

def setup(bot):
    bot.add_cog(UTILS(bot))
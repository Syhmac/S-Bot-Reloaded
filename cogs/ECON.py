from __main__ import bot, log
import modules.env as env

# economy data
from modules.economy.jobs import JOB_LIST

# locales
import modules.locales.en_US as en_US
import modules.locales.pl_PL as pl_PL
import modules.utils as utils

import sqlite3, random, cooldowns
import datetime as dt
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption
from nextcord import ChannelType
from nextcord import Locale as Loc
from cooldowns import SlashBucket

class ECON(commands.Cog, name='economy', description='Economy commands'):
    """
    Selection of economy commands made for fun ant time-killing.
    Available commands:
    """

    def __init__(self, bot):
        self.count = 0
        self.bot = bot

    # * COMMAND: -- BALANCE --
    @bot.slash_command(
        name = en_US.balanceCommandName,
        name_localizations={Loc.pl: pl_PL.balanceCommandName},
        description= en_US.balanceCommandDescription,
        description_localizations={Loc.pl: pl_PL.balanceCommandDescription}
    )
    async def balance(self, interaction: Interaction):
        locale = utils.resolveServerLocale(interaction)
        # Connect to the database
        dbCon = sqlite3.connect('database.db')
        cursor = dbCon.cursor()
        # Check if user has an account in the database, if not - create one
        res = cursor.execute("SELECT balance FROM economy WHERE user_id = ? AND server_id = ?", (interaction.user.id, interaction.guild.id))
        bal = res.fetchone()
        if bal is None:
            cursor.execute("INSERT INTO economy (user_id, server_id) VALUES (?, ?)", (interaction.user.id, interaction.guild.id))
            dbCon.commit()
            bal = 0
        else:
            bal = bal[0]
        await interaction.response.send_message(locale.balanceCommandResponse.format(balance=bal))

    @bot.slash_command(
        name= en_US.jobCommandName,
        name_localizations={Loc.pl: pl_PL.jobCommandName},
        description= en_US.jobCommandDescription,
        description_localizations={Loc.pl: pl_PL.jobCommandDescription}
    )
    @cooldowns.cooldown(1, 60, bucket=SlashBucket.author)
    async def job(self, interaction: Interaction):
        locale = utils.resolveServerLocale(interaction)
        # Connect to the database
        dbCon = sqlite3.connect('database.db')
        cursor = dbCon.cursor()
        # Check if user has an account in the database, if not - create one
        res = cursor.execute("SELECT balance FROM economy WHERE user_id = ? AND server_id = ?", (interaction.user.id, interaction.guild.id))
        bal = res.fetchone()
        if bal is None:
            cursor.execute("INSERT INTO economy (user_id, server_id) VALUES (?, ?)", (interaction.user.id, interaction.guild.id))
            dbCon.commit()
            bal = 0
        else:
            bal = bal[0]

        # Get a random job from the list and calculate earnings and tip
        key = random.choice(list(JOB_LIST.keys()))
        job = JOB_LIST[key]
        earn = job.calculateEarnings()
        tip = job.calculateTips()

        # Update the user's balance and jobs done in the database
        new_bal = bal + earn + tip
        cursor.execute("UPDATE economy SET balance = ?, jobs_done = jobs_done + 1 WHERE user_id = ? AND server_id = ?", (new_bal, interaction.user.id, interaction.guild.id))
        dbCon.commit()

        # Send response
        await interaction.response.send_message(locale.jobList[key].format(user=interaction.user.display_name, earnings=earn, tips=tip))

def setup(bot):
    bot.add_cog(ECON(bot))
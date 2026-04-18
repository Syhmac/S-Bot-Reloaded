from __main__ import bot, log, botErr
import modules.env as env
import random

# economy data
from modules.economy.jobs import JOB_LIST

# locales
import modules.locales.en_US as en_US
import modules.locales.pl_PL as pl_PL
import modules.utils as utils

import sqlite3, random, cooldowns
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
        description_localizations={Loc.pl: pl_PL.balanceCommandDescription},
        integration_types=[0], contexts=[0],
        force_global=True,
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
        name = en_US.balTopCommandName,
        name_localizations={Loc.pl: pl_PL.balTopCommandName},
        description= en_US.balTopCommandDescription,
        description_localizations={Loc.pl: pl_PL.balTopCommandDescription},
        integration_types=[0], contexts=[0],
        force_global=True, #guild_ids=env.TEST_SERVER_ID
    )
    async def bal_top(self, interaction: Interaction):
        locale = utils.resolveServerLocale(interaction)
        # Connect to the database
        dbCon = sqlite3.connect('database.db')
        cursor = dbCon.cursor()
        # Get top 10 users with the highest balance in the server
        res = cursor.execute("SELECT user_id, balance FROM economy WHERE server_id = ? ORDER BY balance DESC LIMIT 10", (interaction.guild.id,))
        top = res.fetchall()
        if len(top) == 0:
            await interaction.response.send_message(locale.balTopCommandNoData)
            return

        # Format the response message
        embed = nextcord.Embed(
            title=locale.balTopCommandEmbedTitle,
            color=0xffcc00
        )

        ranking = ""
        for i, (user_id, balance) in enumerate(top):
            user = interaction.guild.get_member(user_id)
            if user is not None:
                ranking += "#{rank} - {user} - {balance}\n".format(rank = i+1, user = user.display_name, balance = balance)

        embed.add_field(
            name=locale.balTopCommandResponse,
            value=ranking
        )

        await interaction.response.send_message(embed=embed)

    @bot.slash_command(
        name=en_US.balStatsCommandName,
        name_localizations={Loc.pl: pl_PL.balStatsCommandName},
        description= en_US.balStatsCommandDescription,
        description_localizations={Loc.pl: pl_PL.balStatsCommandDescription},
        integration_types=[0], contexts=[0],
        force_global=True, #guild_ids=env.TEST_SERVER_ID
    )
    async def bal_stats(self, interaction: Interaction):
        locale = utils.resolveServerLocale(interaction)
        # Connect to the database
        dbCon = sqlite3.connect('database.db')
        cursor = dbCon.cursor()
        # Get all user economy data
        res = cursor.execute("SELECT balance, jobs_done, job_earn_mult, gambling_wins, gambling_losses, fish_caught, fish_sell_mult, crimes_committed FROM economy WHERE server_id = ? AND user_id = ?", (interaction.guild.id, interaction.user.id))
        balance, jobs_done, job_earn_mult, gambling_wins, gambling_losses, fish_caught, fish_sell_mult, crimes_committed = res.fetchone()
        if balance is None:
            await interaction.response.send_message(locale.balStatsCommandNoData)
            return

        # Building the embed
        embed = nextcord.Embed(
            title=locale.balStatsEmbedTitle,
            color=0xffcc00
        )

        embed.add_field(
            name=locale.balStatsEmbedFiledBalanceName,
            value=f'{balance} :coin:',
            inline=True
        )

        embed.add_field(
            name=locale.balStatsEmbedFiledJobsName,
            value=jobs_done,
            inline=True
        )

        embed.add_field(
            name=locale.balStatsEmbedFiledJobMultName,
            value=str(job_earn_mult) + "x",
            inline=True
        )

        embed.add_field(name="", value="", inline=False) # Empty field as a line break

        embed.add_field(
            name=locale.balStatsEmbedFiledGamblingWinsName,
            value=gambling_wins,
            inline=True
        )

        embed.add_field(
            name=locale.balStatsEmbedFiledGamblingLossesName,
            value=gambling_losses,
            inline=True
        )

        embed.add_field(name="", value="", inline=False) # Empty field as a line break

        embed.add_field(
            name=locale.balStatsEmbedFiledFishCaughtName,
            value=fish_caught,
            inline=True
        )

        embed.add_field(
            name=locale.balStatsEmbedFiledFishMultName,
            value=str(fish_sell_mult) + "x",
            inline=True
        )

        embed.add_field(name="", value="", inline=False) # Empty field to make the distances equal between line breaks

        embed.add_field(
            name=locale.balStatsEmbedFieldCrimesName,
            value=crimes_committed,
            inline=False
        )

        await interaction.response.send_message(embed=embed)

    @bot.slash_command(
        name=en_US.jobCommandName,
        name_localizations={Loc.pl: pl_PL.jobCommandName},
        description= en_US.jobCommandDescription,
        description_localizations={Loc.pl: pl_PL.jobCommandDescription},
        integration_types=[0], contexts=[0],
        force_global=True,
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

    @bot.slash_command(
        name=en_US.coinflipCommandName,
        name_localizations={Loc.pl: pl_PL.coinflipCommandName},
        description= en_US.coinflipCommandDescription,
        description_localizations={Loc.pl: pl_PL.coinflipCommandDescription},
        integration_types=[0], contexts=[0],
        force_global=True, #guild_ids=env.TEST_SERVER_ID,
    )
    @cooldowns.cooldown(1, 60, bucket=SlashBucket.author)
    async def coinflip(self, interaction: Interaction,
        choice: bool = SlashOption(
            name=en_US.genericChoice,
            name_localizations={Loc.pl: pl_PL.genericChoice},
            description=en_US.coinflipCommandChoiceDescription,
            description_localizations={Loc.pl: pl_PL.coinflipCommandChoiceDescription},
            choices={
                "heads" : True,
                "tails": False,
            },
            choice_localizations={
                "heads": {
                    Loc.en_GB: en_US.coinflipCommandChoiceHeads,
                    Loc.en_US: en_US.coinflipCommandChoiceHeads,
                    Loc.pl: pl_PL.coinflipCommandChoiceHeads,
                },
                "tails": {
                    Loc.en_GB: en_US.coinflipCommandChoiceTails,
                    Loc.en_US: en_US.coinflipCommandChoiceTails,
                    Loc.pl: pl_PL.coinflipCommandChoiceTails,
                }
            }
        ),
        amount: int = SlashOption(
            name=en_US.genericAmount,
            name_localizations={Loc.pl: pl_PL.genericAmount},
            description=en_US.genericAmount,
            description_localizations={Loc.pl: pl_PL.genericAmount},
        )
    ):
        locale = utils.resolveServerLocale(interaction)
        # Connect to the database
        dbCon = sqlite3.connect('database.db')
        cursor = dbCon.cursor()
        # Check if user has an account in the database, if not - create one
        res = cursor.execute("SELECT balance FROM economy WHERE user_id = ? AND server_id = ?",
                             (interaction.user.id, interaction.guild.id))
        bal = res.fetchone()
        if bal is None:
            cursor.execute("INSERT INTO economy (user_id, server_id) VALUES (?, ?)",
                           (interaction.user.id, interaction.guild.id))
            dbCon.commit()
            raise botErr.InsufficientBalance(amount, 0)
        else:
            bal = bal[0]

        # Check if user has enough coins
        if amount > bal:
            raise botErr.InsufficientBalance(amount, bal)

        # Pick randomly between heads and tails
        coinResult = bool(random.randint(0, 1))

        # Check if result is the same as user choice
        if coinResult == choice: # win
            color = 0x00ff00
            title = locale.economyCommonWin
            if choice: # heads win
                description = locale.coinflipCommandEmbedHeadsCorrect.format(amount=amount)
            else: # tails win
                description = locale.coinflipCommandEmbedTailsCorrect.format(amount=amount)

            # Update user's balance in the database
            new_bal = bal + amount
            cursor.execute("UPDATE economy SET balance = ?, gambling_wins = gambling_wins + 1 WHERE user_id = ? AND server_id = ?",
                           (new_bal, interaction.user.id, interaction.guild.id))
        else: # loss
            color = 0xff0000
            title = locale.economyCommonLoss
            if choice: # heads loss
                description = locale.coinflipCommandEmbedHeadsIncorrect.format(amount=amount)
            else: # tails loss
                description = locale.coinflipCommandEmbedTailsIncorrect.format(amount=amount)

            # Update user's balance in the database
            new_bal = bal - amount
            if new_bal < 0: # Just to be safe. Can't have negative balance. This should NEVER pass.
                new_bal = 0
            cursor.execute("UPDATE economy SET balance = ?, gambling_losses = gambling_losses + 1 WHERE user_id = ? AND server_id = ?",
                           (new_bal, interaction.user.id, interaction.guild.id))
        dbCon.commit()

        # Create embed
        embed = nextcord.Embed(title=title, description=description, color=color)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(ECON(bot))
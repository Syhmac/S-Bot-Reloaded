from __main__ import bot, log
import modules.env as env

# locales
import modules.locales.en_US as en_US
import modules.locales.pl_PL as pl_PL
import modules.utils as utils

import datetime as dt
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption
from nextcord import ChannelType
from nextcord import Locale as Loc

class ADMIN(commands.Cog, name='admin', description='Administrative commands'):
    """
    Selection of commands for server administrators. Requires the user to have right permissions.
    Available commands:
    """

    def __init__(self, bot):
        self.count = 0
        self.bot = bot

    # * COMMAND: -- KICK --
    @bot.slash_command(
        name = en_US.kickCommandName,
        name_localizations={Loc.pl: pl_PL.kickCommandName},
        description= en_US.kickCommandDescription,
        description_localizations={Loc.pl: pl_PL.kickCommandDescription},
        default_member_permissions=nextcord.permissions.Permissions(kick_members=True),
        integration_types=[0], contexts=[0],
        force_global=True
    )
    async def kick(self, interaction: Interaction,
        member: nextcord.Member = SlashOption(
            name = en_US.genericMember,
            name_localizations={Loc.pl: pl_PL.genericMember},
            description = en_US.kickCommandMemberDescription,
            description_localizations={Loc.pl: pl_PL.kickCommandMemberDescription},
            required = True
        ),
        reason: str = SlashOption(
            name = en_US.genericReason,
            name_localizations={Loc.pl: pl_PL.genericReason},
            description = en_US.kickCommandReasonDescription,
            description_localizations={Loc.pl: pl_PL.kickCommandReasonDescription},
            required = False,
            default = ""
        )
    ):
        locale = utils.resolveServerLocale(interaction)
        if reason != "":
            await member.kick(reason=reason)
            await interaction.response.send_message(locale.kickCommandResponse.format(member=member, reason=reason))
        else:
            await member.kick()
            await interaction.response.send_message(locale.kickCommandResponseNoReason.format(member=member))

    # * COMMAND: -- BAN --
    @bot.slash_command(
        name=en_US.banCommandName,
        name_localizations={Loc.pl: pl_PL.banCommandName},
        description=en_US.banCommandDescription,
        description_localizations={Loc.pl: pl_PL.banCommandDescription},
        default_member_permissions=nextcord.permissions.Permissions(ban_members=True),
        integration_types=[0], contexts=[0],
        force_global=True
    )
    async def ban(self, interaction: Interaction,
        member: nextcord.Member = SlashOption(
            name=en_US.genericMember,
            name_localizations={Loc.pl: pl_PL.genericMember},
            description=en_US.banCommandMemberDescription,
            description_localizations={Loc.pl: pl_PL.banCommandMemberDescription},
            required=True
        ),
        delete_time: int = SlashOption(
            name=en_US.banCommandTime,
            name_localizations={Loc.pl: pl_PL.banCommandTime},
            description=en_US.banCommandTimeDescription,
            description_localizations={Loc.pl: pl_PL.banCommandTimeDescription},
            choices={
                'None': 0,
                '1hr': 3600,
                '6hr': 21600,
                '12hr': 43200,
                '24hr': 86400,
                '3d': 259200,
                '7d': 604800
            },
            choice_localizations={
                'None': {
                    Loc.en_US: en_US.banCommandTimeNone,
                    Loc.en_GB: en_US.banCommandTimeNone,
                    Loc.pl: pl_PL.banCommandTimeNone
                },
                '1hr': {
                    Loc.en_US: en_US.banCommandTime1hr,
                    Loc.en_GB: en_US.banCommandTime1hr,
                    Loc.pl: pl_PL.banCommandTime1hr
                },
                '6hr': {
                    Loc.en_US: en_US.banCommandTime6hr,
                    Loc.en_GB: en_US.banCommandTime6hr,
                    Loc.pl: pl_PL.banCommandTime6hr
                },
                '12hr': {
                    Loc.en_US: en_US.banCommandTime12hr,
                    Loc.en_GB: en_US.banCommandTime12hr,
                    Loc.pl: pl_PL.banCommandTime12hr
                },
                '24hr': {
                    Loc.en_US: en_US.banCommandTime24hr,
                    Loc.en_GB: en_US.banCommandTime24hr,
                    Loc.pl: pl_PL.banCommandTime24hr
                },
                '3d': {
                    Loc.en_US: en_US.banCommandTime3d,
                    Loc.en_GB: en_US.banCommandTime3d,
                    Loc.pl: pl_PL.banCommandTime3d
                },
                '7d': {
                    Loc.en_US: en_US.banCommandTime7d,
                    Loc.en_GB: en_US.banCommandTime7d,
                    Loc.pl: pl_PL.banCommandTime7d
                }
            },
            required=False,
            default=0
        ),
        reason: str = SlashOption(
            name=en_US.genericReason,
            name_localizations={Loc.pl: pl_PL.genericReason},
            description=en_US.banCommandReasonDescription,
            description_localizations={Loc.pl: pl_PL.banCommandReasonDescription},
            required=False,
            default=""
        )
    ):
        locale = utils.resolveServerLocale(interaction)
        if reason != "":
            await interaction.guild.ban(user=member, delete_message_seconds=delete_time, reason=reason)
            await interaction.response.send_message(locale.banCommandResponse.format(member=member, reason=reason))
        else:
            await interaction.guild.ban(user=member, delete_message_seconds=delete_time)
            await interaction.response.send_message(locale.banCommandResponseNoReason.format(member=member))

    # * COMMAND: -- UNBAN --
    @bot.slash_command(
        name=en_US.unbanCommandName,
        name_localizations={Loc.pl: pl_PL.unbanCommandName},
        description=en_US.unbanCommandDescription,
        description_localizations={Loc.pl: pl_PL.unbanCommandDescription},
        default_member_permissions=nextcord.permissions.Permissions(ban_members=True),
        integration_types=[0], contexts=[0],
        force_global=True
    )
    async def unban(self, interaction: Interaction,
    member: nextcord.Member = SlashOption(
        name=en_US.genericMember,
        name_localizations={Loc.pl: pl_PL.genericMember},
        description=en_US.unbanCommandMemberDescription,
        description_localizations={Loc.pl: pl_PL.unbanCommandMemberDescription},
        required=True
    )):
        locale = utils.resolveServerLocale(interaction)
        await member.unban()
        await interaction.response.send_message(locale.unbanCommandResponse.format(member=member))

    # * COMMAND: -- TIMEOUT --
    @bot.slash_command(
        name=en_US.timeoutCommandName,
        name_localizations={Loc.pl: pl_PL.timeoutCommandName},
        description=en_US.timeoutCommandDescription,
        description_localizations={Loc.pl: pl_PL.timeoutCommandDescription},
        default_member_permissions=nextcord.permissions.Permissions(mute_members=True),
        integration_types=[0], contexts=[0],
        force_global=True
    )
    async def timeout(self, interaction: Interaction,
        member: nextcord.Member = SlashOption(
            name=en_US.genericMember,
            name_localizations={Loc.pl: pl_PL.genericMember},
            description=en_US.timeoutCommandMemberDescription,
            description_localizations={Loc.pl: pl_PL.timeoutCommandMemberDescription},
            required=True
        ),
        timeout_duration: int = SlashOption(
            name=en_US.timeoutCommandTime,
            name_localizations={Loc.pl: pl_PL.timeoutCommandTime},
            description=en_US.timeoutCommandTimeDescription,
            description_localizations={Loc.pl: pl_PL.timeoutCommandTimeDescription},
            choices={
                '10m': 600,
                '30m': 1800,
                '1hr': 3600,
                '3hr': 10800,
                '6hr': 21600,
                '12hr': 43200,
                '24hr': 86400,
                '3d': 259200,
                '7d': 604800
            },
            choice_localizations={
                '10m': {
                    Loc.en_US: en_US.timeoutCommandTime10m,
                    Loc.en_GB: en_US.timeoutCommandTime10m,
                    Loc.pl: pl_PL.timeoutCommandTime10m
                },
                '30m': {
                    Loc.en_US: en_US.timeoutCommandTime30m,
                    Loc.en_GB: en_US.timeoutCommandTime30m,
                    Loc.pl: pl_PL.timeoutCommandTime30m
                },
                '1hr': {
                    Loc.en_US: en_US.timeoutCommandTime1hr,
                    Loc.en_GB: en_US.timeoutCommandTime1hr,
                    Loc.pl: pl_PL.timeoutCommandTime1hr
                },
                '3hr': {
                    Loc.en_US: en_US.timeoutCommandTime3hr,
                    Loc.en_GB: en_US.timeoutCommandTime3hr,
                    Loc.pl: pl_PL.timeoutCommandTime3hr
                },
                '6hr': {
                    Loc.en_US: en_US.timeoutCommandTime6hr,
                    Loc.en_GB: en_US.timeoutCommandTime6hr,
                    Loc.pl: pl_PL.timeoutCommandTime6hr
                },
                '12hr': {
                    Loc.en_US: en_US.timeoutCommandTime12hr,
                    Loc.en_GB: en_US.timeoutCommandTime12hr,
                    Loc.pl: pl_PL.timeoutCommandTime12hr
                },
                '24hr': {
                    Loc.en_US: en_US.timeoutCommandTime24hr,
                    Loc.en_GB: en_US.timeoutCommandTime24hr,
                    Loc.pl: pl_PL.timeoutCommandTime24hr
                },
                '3d': {
                    Loc.en_US: en_US.timeoutCommandTime3d,
                    Loc.en_GB: en_US.timeoutCommandTime3d,
                    Loc.pl: pl_PL.timeoutCommandTime3d
                },
                '7d': {
                    Loc.en_US: en_US.timeoutCommandTime7d,
                    Loc.en_GB: en_US.timeoutCommandTime7d,
                    Loc.pl: pl_PL.timeoutCommandTime7d
                }
            },
            required=True
        ),
        reason: str = SlashOption(
            name=en_US.genericReason,
            name_localizations={Loc.pl: pl_PL.genericReason},
            description=en_US.banCommandReasonDescription,
            description_localizations={Loc.pl: pl_PL.banCommandReasonDescription},
            required=False,
            default=""
        )
    ):
        locale = utils.resolveServerLocale(interaction)
        delta = dt.timedelta(seconds=timeout_duration)

        time_dict = {
            600: locale.timeoutCommandTime10m,
            1800: locale.timeoutCommandTime30m,
            3600: locale.timeoutCommandTime1hr,
            10800: locale.timeoutCommandTime3hr,
            21600: locale.timeoutCommandTime6hr,
            43200: locale.timeoutCommandTime12hr,
            86400: locale.timeoutCommandTime24hr,
            259200: locale.timeoutCommandTime3d,
            604800: locale.timeoutCommandTime7d
        }

        if reason != "":
            await member.timeout(timeout=delta, reason=reason)
            await interaction.response.send_message(locale.timeoutCommandResponse.format(member=member, time=time_dict[timeout_duration], reason=reason))
        else:
            await member.timeout(timeout=delta)
            await interaction.response.send_message(locale.timeoutCommandResponseNoReason.format(member=member, time=time_dict[timeout_duration]))

def setup(bot):
    bot.add_cog(ADMIN(bot))
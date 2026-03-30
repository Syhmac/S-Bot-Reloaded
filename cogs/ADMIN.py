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

class ADMIN(commands.Cog, name='admin', description='Administrative commands'):
    """
    Selection of commands for server administrators. Requires the user to have right permissions.
    Available commands:
    """

    def __init__(self, bot):
        self.count = 0
        self.bot = bot

    @bot.slash_command(
        name = en_US.kickCommandName,
        name_localizations={Loc.pl: pl_PL.kickCommandName},
        default_member_permissions=nextcord.permissions.Permissions(kick_members=True),
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

def setup(bot):
    bot.add_cog(ADMIN(bot))
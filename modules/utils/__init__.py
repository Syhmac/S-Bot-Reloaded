import nextcord
import modules.locales.pl_PL as pl_PL
import modules.locales.en_US as en_US

def resolveServerLocale(interaction: nextcord.Interaction):
    if interaction.guild_id is None:
        if interaction.locale == nextcord.Locale.pl:
            return pl_PL
        else:
            return en_US
    if interaction.guild.preferred_locale == nextcord.Locale.pl:
        return pl_PL
    else:
        return en_US

def resolveServerLocaleBuGuild(guild: nextcord.Guild):
    if guild.preferred_locale == nextcord.Locale.pl:
        return pl_PL
    else:
        return en_US
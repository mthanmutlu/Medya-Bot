import discord
from utils.randomColor import randColor


class Logger():
    def __init__(
        self,
        client: discord.Client,
        logChannelId: int,
        guildId: int,
        command: str = None,
        logDescription: str = None
    ):
        self.client = client
        self.logChannelId = logChannelId
        self.guildId = guildId

        self.command = command
        self.logDescription = logDescription

    async def sendLogEmbed(self):
        embed = discord.Embed()
        embed.color = randColor()
        embed.title = self.command
        embed.description = self.logDescription
        logChannel: discord.TextChannel = await self.getLogChannel()
        await logChannel.send(embed=embed)

    async def getLogChannel(self):
        guild: discord.Guild = self.client.get_guild(self.guildId)
        logChannel: discord.TextChannel = discord.utils.find(
            lambda c: c.id == self.logChannelId, guild.text_channels)
        return logChannel

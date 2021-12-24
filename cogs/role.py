import asyncio
import discord
from discord.ext import commands
from discord.channel import TextChannel, VoiceChannel
from discord.ext.commands.bot import Bot
from utils.logger import Logger
from discord.ext.commands.context import Context
from discord.member import Member, VoiceState
from discord.message import Message
import os
import json

configPath = os.path.dirname(__file__) + '/../config.json'
with open(configPath, encoding='UTF-8') as file:
    config = json.load(file)


class Role(commands.Cog):
    def __init__(self, client: Bot) -> None:
        self.client = client

    @commands.has_permissions(kick_members=True)
    @commands.command(name='rolver')
    async def add_role(self, ctx: Context, member: Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.reply(f'**{member.mention} Kullanıcısına {role.mention} rolü verildi.**')
        logger = Logger(
            self.client,
            config['logChannel'],
            ctx.guild.id,
            'Kick',
            f'**{ctx.author.mention}, {member.mention} Kullanıcısına {role.mention} rolünü verdi.**'
        )
        await logger.sendLogEmbed()

    @commands.has_permissions(kick_members=True)
    @commands.command(name='rolal')
    async def remove_role(self, ctx: Context, member: Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.reply(f'**{member.mention} Kullanıcısından {role.mention} rolü alındı.**')
        logger = Logger(
            self.client,
            config['logChannel'],
            ctx.guild.id,
            'Kick',
            f'**{ctx.author.mention}, {member.mention} Kullanıcısından {role.mention} rolünü aldı.**'
        )
        await logger.sendLogEmbed()


def setup(client: Bot):
    client.add_cog(Role(client))

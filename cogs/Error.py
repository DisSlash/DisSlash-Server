import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import has_role
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import cooldown, BucketType

class Error(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            await ctx.send(f'Sorry {ctx.message.author.mention}, This Command Does Not Exist.')

def setup(client):
    client.add_cog(Error(client))
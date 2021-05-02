import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="DisSlash Playground Help")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
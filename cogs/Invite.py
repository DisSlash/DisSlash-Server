import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def invite(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="DisSlash Invite Info")
        embed.add_field(name="DisSlash Bot:", value=f'You Can Invite DisSlash With This Link: [DisSlash](https://dsc.gg/disslash)', inline=False)
        embed.add_field(name="DisSlash Playground", value=f'You Can Share This Link With Your Friends To Join DisSlash Playground: [DisSlash Playground](https://discord.gg/QUzvj5y5kB)', inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/US4aSgW.png")
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Invite(client))
import discord
from discord.ext import commands

class OnMemberJoin(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='welcome')
        embed = discord.Embed(title="Welcome To DisSlash Playground!", description=f'Welcome, {member.mention} To DisSlash Playground!')
        await channel.send(embed=embed)
        print(f'{member} Has Joined DisSlash Playground')

def setup(client):
    client.add_cog(OnMemberJoin(client))
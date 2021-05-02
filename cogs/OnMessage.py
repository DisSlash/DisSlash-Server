import discord
import os
from discord.ext import commands

with open('profanity.txt') as input_file:
        bad = [line.strip() for line in input_file]

class OnMessage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        for word in bad:
            if word in message.content:
                await message.delete()


def setup(client):
    client.add_cog(OnMessage(client))
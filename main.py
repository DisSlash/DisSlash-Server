import discord
import os
from discord.ext import commands
from discord_slash import SlashCommand


intents = discord.Intents().all()
client = commands.Bot(command_prefix = '!', intents=intents)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

client.remove_command('help')
@client.event
async def on_ready():
    print("Bot Is Online")

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token = os.environ.get('TOKEN')
client.run(TOKEN)
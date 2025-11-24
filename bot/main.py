"""
Main entry point for the Discord Partnership Management Bot
"""
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot intents
intents = discord.Intents.default()
intents.members = True

# Custom prefix function for per-guild prefixes
async def get_prefix(bot, message):
    # For now, default to 'p!'
    # This will be replaced with a database lookup later
    return 'p!'

# Create bot instance
bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)

# Event: on_ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    # Start background tasks here if any

# Load cogs from cogs directory
cogs = [
    'cogs.auto_partner',
    'cogs.partner',
    'cogs.giveaway',
    'cogs.tracking',
    'cogs.stats',
    'cogs.config',
    'cogs.blacklist',
    'cogs.alerts',
    'cogs.events',
    'cogs.user_dm',
]

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f'Loaded cog {cog}')
    except Exception as e:
        print(f'Failed to load cog {cog}: {e}')

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))

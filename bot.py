import discord
import discord.ext.commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.ext.commands.Bot(command_prefix='!Jarvis')

@bot.event
async def on_ready():
    print(bot.owner_id)
tok = os.getenv('TOKEN')
print(tok)
bot.run(tok)
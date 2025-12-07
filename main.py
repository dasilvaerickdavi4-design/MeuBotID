import os
import json
import sys
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

def get_token():
    token = os.getenv("TOKEN")
    if token:
        return token

    try:
        with open("id.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("TOKEN")
    except:
        return None

if __name__ == "__main__":
    token = get_token()

    if not token:
        print("ERRO: Nenhum token encontrado.")
        sys.exit(1)

    bot.run(token)
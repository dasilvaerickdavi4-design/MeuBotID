import discord
from discord.ext import commands
import json
import os

CARGO_ID = 1446878840516509868
ID_FILE = "id.json"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def load_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as f:
            return json.load(f)
    return {}

def save_id(data):
    with open(ID_FILE, "w") as f:
        json.dump(data, f)

@bot.event
async def on_ready():
    print(f"Bot está online como {bot.user}")

@bot.command()
async def setid(ctx, *, texto):
    if CARGO_ID in [role.id for role in ctx.author.roles]:
        data = load_id()
        data[str(ctx.author.id)] = texto
        save_id(data)
        await ctx.send("ID salvo com sucesso!")
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

@bot.command()
async def getid(ctx, membro: discord.Member = None):
    membro = membro or ctx.author
    data = load_id()
    texto = data.get(str(membro.id), "Nenhum ID salvo.")
    await ctx.send(texto)

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)

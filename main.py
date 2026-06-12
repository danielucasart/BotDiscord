import discord
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")

class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = Bot()

def transformar_fonte(texto: str) -> str:
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    estilizado = "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"

    tabela = str.maketrans(normal, estilizado)
    return texto.translate(tabela)

@bot.tree.command(
    name="fonte",
    description="Transforma um texto em fonte matemática"
)
@app_commands.describe(
    texto="Texto que será transformado"
)
async def fonte(interaction: discord.Interaction, texto: str):
    resultado = transformar_fonte(texto)
    await interaction.response.send_message(resultado)

@bot.event
async def on_ready():
    print(f"✅ Logado como {bot.user}")

bot.run(TOKEN)
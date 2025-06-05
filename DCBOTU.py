import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
atik_gruplari = {
    "pet şişe": "plastik",
    "kola kutusu": "metal",
    "cam şişe": "cam",
    "gazete": "kağıt",
    "pil": "tehlikeli atık",
    "yumurta kabuğu": "organik atık",
    "peçete": "organik atık",
    "plastik poşet": "plastik",
    "teneke kutu": "metal",
    "şampuan şişesi": "plastik",
    "su şişesi": "plastik"
}
@bot.event
async def on_ready():
    print(f'Bot aktif oldu: {bot.user}')
    @bot.command()
    async def sor(ctx, *, atik):
        atik = atik.lower()
        if atik in atik_gruplari:
            grup = atik_gruplari[atik] 
            await ctx.send(f"**{grup} atık** grubuna girer. {grup.title()} geri dönüşüm kutusuna atabilirsin.")
        else:
            await ctx.send("üzgünüm böyle bir kod bulunmuyor")
bot.run("Your discord token")

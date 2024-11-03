import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def kirlilik(ctx):
    await ctx.send(f'Kirliliği önlemekle ilgili bir kaç şey söyleye bilirim: {bot.user}!')
    await ctx.send(f'1-Daha az araç kullanmak , bunun yerine bisiklet kullanabilir ve ya yürüye biirsiniz bu sizin sağlığınız açısından daha iyi. {bot.user}!')
    await ctx.send(f'2-Daha az atık üretimi , bunun yerine geri dönüşümü kullanmanızı öneririm.  {bot.user}!')
    await ctx.send(f'3-Kirliliği önlemenin en güzel yolu ağaçlar ekmek ve onları korumaktır. {bot.user}!')

@bot.command()
async def foto(ctx):
    image_list = os.listdir('image')
    randompic = random.choice(image_list)
    with open(f'./image/{randompic}', 'rb') as img:
        picture= discord.File(img)
    await ctx.send(file=picture)

    

bot.run("MTMwMDE1MjM4Mjk1MjU3MDkzMQ.G4vSfv.okJoNyjvmfx1CevozwhJWLOMtXuRlphaMU0Bl4")
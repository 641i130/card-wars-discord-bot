import os
import discord
from discord.ext import commands
import datetime
import data
import configparser

configuration = configparser.ConfigParser()
configuration.read("settings.ini")

def log_write(text):
    with open(configuration.get('Logging', 'LogFile'),"a") as log:
        all = "[{}] : \t{}\n".format(str(datetime.datetime.now()),text)
        print(text)
        log.write(all)

log_write("Starting BOT!!!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Card Wars'))
    log_write('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx,error):
    await ctx.send("Try `$help` for examples on how to use this.")
    log_write("No arguments given with $c lol")
    log_write(error)

@bot.command()
async def c(ctx, *, arg):
    embed = discord.Embed(color=0xfff100)

    log_write("{1} \t$c {0}".format(arg,ctx.message.author))

    cardData = data.getData(configuration.get('DataSources', 'CardJsonFiles'))
    search = data.findMatchingCards(cardData, arg)

    if len(search) != 1:
        if len(search) == 0:
            embed.set_author(name="No results found, Please try again.".format(str(len(search))))
            await ctx.send(embed=embed)
            log_write("Call for {} cards.".format(str(len(search))))
            return

        if len(search) > 24:
            embed.set_author(name="That search exceeds the limit ({} cards were returned). Please be more specific.".format(str(len(search))))
            await ctx.send(embed=embed)
            log_write("Call for {} cards.".format(str(len(search))))
            return

        if len(search) > 1:
            embed.set_author(name="Multiple Results:")

            x=1
            for ting in search:
                embed.add_field(name=str(x)+".", value=ting['name'], inline=False)
                x+=1

            embed.add_field(name="Hot Tip", value='insert quotes for more specific search results. eg "Jake"', inline=False)
            await ctx.send(embed=embed)
            log_write("Mulitple ({}) Results found".format(str(len(search))))

    if len(search) == 1:
        print(search)
        returned_card=search[0]
        embed = discord.Embed(color=0xfff100)

        embed.set_author(name=returned_card['name'], icon_url=configuration.get("Discord", "IconUrl"))
        embed.add_field(name="Set Release", value=data.convertSetToString(returned_card['set']), inline=False)
        embed.set_thumbnail(url=os.path.join(configuration.get('DataSources', 'CardImages'), returned_card["imageurl"]))

        if (returned_card["type"] == 0):
            embed.add_field(name="Landscape", value=data.convertLandscapeToString(returned_card['landscape']), inline=True)
            embed.add_field(name="Type", value=data.convertCardTypeToString(returned_card['type']), inline=True)
            embed.add_field(name="Cost", value=returned_card['cost'], inline=True)
            embed.add_field(name="ATK", value=returned_card['attack'], inline=True)
            embed.add_field(name="DEF", value=returned_card['defense'], inline=True)
            embed.add_field(name="Description", value=returned_card['ability'], inline=True)

        if (returned_card["type"] == 1 or returned_card['type'] == 2 or returned_card['type'] == 5):
            embed.add_field(name="Landscape", value=data.convertLandscapeToString(returned_card['landscape']), inline=True)
            embed.add_field(name="Type", value=data.convertCardTypeToString(returned_card['type']), inline=True)
            embed.add_field(name="Cost", value=returned_card['cost'], inline=True)
            embed.add_field(name="Description", value=returned_card['ability'], inline=True)

        if (returned_card["type"] == 4):
            embed.add_field(name="Type", value=data.convertCardTypeToString(returned_card['type']), inline=True)
            embed.add_field(name="Description", value=returned_card['ability'], inline=True)
            embed.add_field(name="Card Set", value=data.convertSetToString(returned_card['set']), inline=True)

        embed.add_field(name="Report a problem: ", value=f"Message {configuration.get('Discord', 'UserId')}", inline=True)
        await ctx.send(embed=embed)
        log_write(returned_card["name"])
        log_write("")

@bot.command()
async def img(ctx, *, arg):
    embed = discord.Embed(color=0xfff100)

    log_write("{1} \timg {0}".format(arg,ctx.message.author))

    cardData = data.getData(configuration.get('DataSources', 'CardJsonFiles'))
    search = data.findMatchingCards(cardData, arg)

    if len(search) != 1:
        if len(search) == 0:
            embed.set_author(name="No results found, Please try again.".format(str(len(search))))
            await ctx.send(embed=embed)
            log_write("Call for {} cards.".format(str(len(search))))
            return

        if len(search) > 24:
            embed.set_author(name="That search exceeds the limit ({} cards were returned). Please be more specific.".format(str(len(search))))
            await ctx.send(embed=embed)
            log_write("Call for {} cards.".format(str(len(search))))
            return

        if len(search) > 1:
            embed.set_author(name="Multiple Results:")

            x=1
            for ting in search:
                embed.add_field(name=str(x)+".", value=ting['name'], inline=False)
                x+=1

            embed.add_field(name="Hot Tip", value='insert quotes for more specific search results. eg "Jake"', inline=False)
            await ctx.send(embed=embed)
            log_write("Mulitple ({}) Results found".format(str(len(search))))

    if len(search) == 1:
        returned_card=search[0]

        await ctx.send(os.path.join(configuration.get('DataSources', 'CardImages'), returned_card["imageurl"]))
        print(','.join(str(v) for v in search))
        log_write("")

@bot.command()
async def help(ctx, message=None):
    # This should DM the user that requested it.
    embed = discord.Embed(color=0xfff100)
    embed.set_author(name="Help Page")
    embed.add_field(name="Commands:", value="`$c [card name]` shows details of a card. \n `$img [card name]` shows just the image of a card.", inline=True)
    embed.add_field(name="Report a problem: ", value=f"Message {configuration.get('Discord', 'UserId')}", inline=True)
    await ctx.author.send(embed=embed)
    log_write("Sent help message to {} DMS.".format(ctx.message.author))
    await ctx.send("Check your dms!")

bot.run(configuration.get('Discord', 'Token'))
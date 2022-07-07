import os
import discord
from discord.ext import commands
import csv
import datetime
import urllib.parse

def log_write(text):
    with open("log.log","a") as log:
        all = "[{}] : \t{}\n".format(str(datetime.datetime.now()),text)
        print(text)
        log.write(all)

log_write("Starting BOT!!!")

TOKEN = "insert your token"
bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Card Wars'))
    log_write('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_command_error(ctx,error):
    await ctx.send("Try `$help` for examples on how to use this.")
    log_write("No arguments given with $c lol")
    log_write("")


@bot.command()
async def c(ctx, *, arg):
    embed = discord.Embed(color=0xfff100)
    with open('./cards.csv') as cfile:
        csv_file = csv.reader(cfile, delimiter=',',quotechar='"')
        # Find card and return value
        log_write("{1} \t$c {0}".format(arg,ctx.message.author))

        search=[]
        for row in csv_file:
            if (arg.startswith('"') and arg.endswith('"')):
                    if (arg.replace('"',"").lower() == row[0].lower()):
                        search.append(row)
        cfile.seek(0)

        for row in csv_file:
            if arg.lower() in row[0].lower():
                search.append(row)

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
                    embed.add_field(name=str(x)+".", value=ting[0], inline=False)
                    x+=1

                embed.add_field(name="Hot Tip", value='insert quotes for more specific search results. eg "Jake"', inline=False)
                await ctx.send(embed=embed)
                log_write("Mulitple ({}) Results found".format(str(len(search))))

        if len(search) == 1:
            returned_card=search[0]

            embed = discord.Embed(color=0xfff100)

            embed.set_author(name=returned_card[0], icon_url="insert your icon")
            embed.add_field(name="Deck / Quantity", value=returned_card[8].rstrip(), inline=False)
            embed.set_thumbnail(url="https://yourserver.com/cardwarsimages/{}.jpg".format(urllib.parse.quote(returned_card[0])))

            if (returned_card[2].rstrip() == "Creature"):
                embed.add_field(name="Landscape", value=returned_card[3].rstrip(), inline=True)
                embed.add_field(name="Type", value=returned_card[2].rstrip(), inline=True)
                embed.add_field(name="Cost", value=returned_card[4].rstrip(), inline=True)
                embed.add_field(name="ATK", value=returned_card[5].rstrip(), inline=True)
                embed.add_field(name="DEF", value=returned_card[6].rstrip(), inline=True)
                embed.add_field(name="Description", value=returned_card[1].rstrip(), inline=True)

            if (returned_card[2].rstrip() == "Spell" or returned_card[2].rstrip() == "Building" or returned_card[2].rstrip() == "Teamwork"):
                embed.add_field(name="Landscape", value=returned_card[3].rstrip(), inline=True)
                embed.add_field(name="Type", value=returned_card[2].rstrip(), inline=True)
                embed.add_field(name="Cost", value=returned_card[4].rstrip(), inline=True)
                embed.add_field(name="Description", value=returned_card[1].rstrip(), inline=True)

            if (returned_card[2].rstrip() == "Hero"):
                embed.add_field(name="Type", value=returned_card[2].rstrip(), inline=True)
                embed.add_field(name="Description", value=returned_card[1].rstrip(), inline=True)
                #embed.add_field(name="Card Set", value=returned_card[9].rstrip(), inline=True)

            embed.add_field(name="Report a problem: ", value="Message <@!INSERT YOUR USER ID>", inline=True)
            await ctx.send(embed=embed)
            log_write(text.join(returned_card[0]))
            log_write("")

@bot.command()
async def img(ctx, *, arg):

    embed = discord.Embed(color=0xfff100)

    with open('./cards.csv') as cfile:
        csv_file = csv.reader(cfile, delimiter=',',quotechar='"')
        # Find card and return value
        log_write("{1} \timg {0}".format(arg,ctx.message.author))

        search=[]
        for row in csv_file:
            if (arg.startswith('"') and arg.endswith('"')):
                    if (arg.replace('"',"").lower() == row[0].lower()):
                        search.append(row)
        cfile.seek(0)

        for row in csv_file:
            if arg.lower() in row[0].lower():
                search.append(row)

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
                    embed.add_field(name=str(x)+".", value=ting[0], inline=False)
                    x+=1

                embed.add_field(name="Hot Tip", value='insert quotes for more specific search results. eg "Jake"', inline=False)
                await ctx.send(embed=embed)
                log_write("Mulitple ({}) Results found".format(str(len(search))))

        if len(search) == 1:
            returned_card=search[0]

            await ctx.send(file=discord.File("./images/{}.jpg".format(returned_card[0])))
            print(','.join(str(v) for v in search))
            log_write("")

@bot.command()
async def help(ctx, message=None):
    # THis should DM the user that requested it.
    embed = discord.Embed(color=0xfff100)
    embed.set_author(name="Help Page")
    embed.add_field(name="Commands:", value="`$c [card name]` shows details of a card. \n `$img [card name]` shows just the image of a card.", inline=True)
    embed.add_field(name="Report a problem: ", value="Message INSERT YOUR USER ID", inline=True)
    await ctx.author.send(embed=embed)
    log_write("Sent help message to {} DMS.".format(ctx.message.author))
    await ctx.send("Check your dms!")

bot.run(TOKEN)

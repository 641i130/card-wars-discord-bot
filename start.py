# Discord Card Wars Bot
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

TOKEN = "INSERT BOT TOKEN!!!"
bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Card Wars'))
    log_write('We have logged in as {0.user}'.format(bot))

@bot.command()
async def c(ctx, *, arg):
    with open('./cards.csv') as cfile:
        csv_file = csv.reader(cfile, delimiter=',',quotechar='"')
        # Find card and return value
        log_write("{1} \t$c {0}".format(arg,ctx.message.author))
        search=[]
        s2=[]
        for row in csv_file:
            if arg.lower() in row[0].lower():
                search.append(row[0])
                returned_card=row
            if arg == row[0]:
                s2.append(row[0])
                returned_card=row
        if len(search) != 1:
            if len(s2)==1:
                search = s2
            if len(search) > 1:
                embed = discord.Embed(color=0xfff100)
                embed.set_author(name="Did you mean:")
                x=1
                for ting in search:
                    embed.add_field(name=str(x)+".", value=ting, inline=False)    
                    x+=1
                try:
                    embed.add_field(name="Disclaimer", value="Try typing it with proper capitalization.", inline=False)    
                    await ctx.send(embed=embed)
                    log_write("".join(search))
                    log_write("")
                except:
                    await ctx.send("That search exceeds the limit ({} cards were returned). Please be more specific.".format(str(len(search))))
                    log_write("Call for {} cards.".format(str(len(search))))


        if len(search) == 1:
            embed = discord.Embed(color=0xfff100)

            embed.set_author(name=returned_card[0], icon_url="https://cdn.discordapp.com/avatars/705581980628025415/0a89eae2186c741e269d72b10c407b47.webp")
            embed.add_field(name="Deck / Quantity", value=returned_card[8].rstrip(), inline=False)
            embed.set_thumbnail(url="http://35.184.199.95/images/{}.jpg".format(urllib.parse.quote(returned_card[0])))

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
                
            embed.add_field(name="Report a problem: ", value="Message <@!234651024634281984>", inline=True)
            await ctx.send(embed=embed)

            log_write("".join(search))
            log_write("")

@bot.command()
async def img(ctx, *, arg):
    with open('./cards.csv') as cfile:
        csv_file = csv.reader(cfile, delimiter=',',quotechar='"')
        # Find card and return value
        log_write("{1} \t$c {0}".format(arg,ctx.message.author))
        search=[]
        s2=[]
        for row in csv_file:
            if arg.lower() in row[0].lower():
                search.append(row[0])
                returned_card=row
            if arg == row[0]:
                s2.append(row[0])
                returned_card=row
        if len(search) != 1:
            if len(s2)==1:
                search = s2
            if len(search) > 1:
                embed = discord.Embed(color=0xfff100)
                embed.set_author(name="Did you mean:")
                x=1
                for ting in search:
                    embed.add_field(name=str(x)+".", value=ting, inline=False)    
                    x+=1
                try:
                    embed.add_field(name="Disclaimer", value="Try typing it with proper capitalization.", inline=False)    
                    await ctx.send(embed=embed)
                    log_write("".join(search))
                    log_write("")
                except:
                    await ctx.send("That search exceeds the limit ({} cards were returned). Please be more specific.".format(str(len(search))))
                    log_write("Call for {} cards.".format(str(len(search))))
        if len(search) == 1:
            await ctx.send(file=discord.File("/home/carrotkumiko/images/{}.jpg".format(returned_card[0])))

            log_write("".join(search))
            log_write("")

@bot.command()
async def help(ctx, message=None):
    # THis should DM the user that requested it.
    embed = discord.Embed(color=0xfff100)
    embed.set_author(name="Help Page")
    embed.add_field(name="Commands:", value="`$c [card name]` shows details of a card. \n `$img [card name]` shows just the image of a card.", inline=True)
    embed.add_field(name="Report a problem: ", value="Message <@!234651024634281984>", inline=True)
    await ctx.author.send(embed=embed)
    log_write("Sent help message to {} DMS.".format(ctx.message.author))

bot.run(TOKEN)


# card-wars-discord-bot
 A Discord bot with every card in the trading card game.
 
## What is this?
This is the source code for the discord bot that has every card in card wars indexed with its img data as well! Feel free to host this yourself or use the one thats being hosted on the discord server! Link below.

Modified and added data from https://github.com/TJSoler/cardwars

Thanks to ``Baconator#2332`` on the discord server for formating the cards and database.

Join the server to try it out live:
https://discord.gg/pH2AS45


## Deployment Guide

1. `git clone https://github.com/itderrickh/CardWarsData` to the location where you will be hosting the card images
2. `git clone https://github.com/641i130/card-wars-discord-bot.git` to where you plan on hosting the bot
3. Create `settings.ini` in the directory `card-wars-discord-bot` with values filled in from your discord. Refer to `settings.sample.ini` for an example.
4. Run `pip install -r requirements.txt` to get the python packages
5. Run `python start.py` or setup that file to run with your favorite task manager


## Updating the card data

If you use `git pull` where you cloned the `CardWarsData` project the bot should automatically pick up the changes.

You can submit a PR to `https://github.com/itderrickh/CardWarsData` if the data needs an update or you want to make changes.

## settings.ini value meanings

* CardImages - The web address where you will serve the card images
* CardJsonFiles - The machine address of where the CardWarsData json files are stored (ie. `/appdata/CardWarsData/data/cards`)

* Token - Token for your bot
* IconUrl - Web address for your bots icon
* UserId - The owner of the bots discord username

* LogFile - The directory to store the log file (ie. `/logs/log.log`)

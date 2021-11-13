"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
A Discord bot that plays cricket with the user.

Version: 1.1
"""

# Importing all libraries
import asyncio
from collections import UserList
import os
import random
from random import choice, randrange
import dotenv
from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands
from message import *

load_dotenv(find_dotenv())
TOKEN = os.getenv('BOTTOKEN')

# Registring the client
client = commands.Bot(command_prefix=">")

# Once the bot is connected
# this will ping on terminal
# the bot is ready
@client.event
async def on_ready():
    print("The bot is ready!")

# CricBot Start

class cricBot():
    @client.group(name='cric', invoke_without_command=True)
    async def cric(ctx):
        
        # EMBED SETTINGS
        embed_home = discord.Embed(
            title="Welcome to CricBot!",
            url="https://github.com/Raveesh1505/CricBot",
            description=f"{OPEN}",
            color = discord.Color.red()
        )

        embed_home.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_home.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")

        await ctx.send(embed=embed_home)

    @cric.command(name='play')
    async def play(ctx):

        # EMBED SETTINGS

        ## Creating embed templates for scorecard
        embed_score = discord.Embed(
            title='CricBot Scoreboard',
            url="https://github.com/Raveesh1505/CricBot",
            description='Great Shot!!!',
            color=discord.Color.red()
        )

        embed_out = discord.Embed(
            title='CricBot Scoreboard',
            url="https://github.com/Raveesh1505/CricBot",
            description='OUT!!!',
            color=discord.Color.red()
        )
        embed_inning = discord.Embed(
            title='CricBot Scoreboard',
            url="https://github.com/Raveesh1505/CricBot",
            description='INNINGS OVER!! Well Played. Have a look at innings scorecard below.',
            color=discord.Color.red()
        )

        embed_go = discord.Embed(
            title = 'CricBot Scoreboard', 
            url="https://github.com/Raveesh1505/CricBot",
            color=discord.Color.red()
        )

        embed_start = discord.Embed(
            title = 'CricBot Game Start',
            url = "https://github.com/Raveesh1505/CricBot",
            description = f'Hello **{ctx.author}** 👋\n\nLet us begin with toss. Enter **"heads"** or **"tails"** as your choice for the toss.\n\nBest of luck!!!',
            color=discord.Color.red()
        )

        embed_sec_start = discord.Embed(
            title='SECOND INNINGS',
            url="https://github.com/Raveesh1505/CricBot",
            description=f'{ctx.author} it is your time to rock the pitch with some cool bowling action. Let the **SECOND INNINGS** begin!!!' 
        )

        embed_toss_sys = discord.Embed(
            title='CricBot Scoreboard',
            description='**System** won the toss. System chooses to **bowl first**. Best of luck!!!\n\n*Enter any number from 1 to 6 to begin the match.*'
        )
        embed_toss_user_ch = discord.Embed(
            title='CricBot Scoreboard',
            description='You have won the toss!! What do you choose? Enter **bat** for batting first and **bowl** for bowling first.'
        )
        embed_toss_user = discord.Embed(
            title='CricBot Scoreboard',
            description=f'Well that sound a good choice. Best of luck!!\n\n*Enter any number from 1 to 6 to start*'
        )

        ## Setting embed footers
        embed_score.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_out.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_inning.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_go.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_start.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_sec_start.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_toss_sys.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_toss_user_ch.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_toss_user.set_footer(text='CricBot! The ultimate cricket discord bot.')        

        ## Setting embed thumbnails
        embed_score.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_out.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_inning.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_go.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_start.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_sec_start.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_toss_sys.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_toss_user_ch.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")
        embed_toss_user.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")

        # BOT SETTINGS
        ## Send start message at beginning
        await ctx.send(embed=embed_start)

        ## Setting variables
        toss_choice = ['heads', 'tails']
        user_score = 0
        user_wick = 0
        sys_score = 0
        sys_wick = 0
        sys_ch = random.randrange(start = 1, stop = 6)
        sys_toss = random.choice(toss_choice)

        # Toss
        try:
            user_toss_ch = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

            if sys_toss != user_toss_ch:
                await ctx.send(embed=embed_toss_sys)

                # User batting

                while (user_wick != 1):
                    try:
                        bat_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                        if int(bat_msg.content) < 1 or int(bat_msg.content) > 6: 
                            await ctx.send("Invalid input.")
                        
                        elif int(bat_msg.content) != sys_ch:
                            user_score = user_score + int(bat_msg.content)
                            await ctx.send(embed=embed_score)
                            await ctx.send(f'**{ctx.author.name} Score:** {user_score}')

                        elif int(bat_msg.content) == sys_ch:
                            user_wick = user_wick + 1
                            await ctx.send(embed=embed_out)

                    except asyncio.TimeoutError:
                        await ctx.send("Sorry. you did not gave input in time. Game over!")
                        break

                embed_inning.add_field(
                    name=f'{ctx.author} Score',
                    value=f'{user_score}'
                )
                embed_inning.add_field(
                    name="System Score",
                    value=f'{sys_score}'
                )
                await ctx.send(embed=embed_inning)
                await ctx.send(embed=embed_sec_start)

                # System batting

                while (sys_wick != 1) and (sys_score <= user_score):
                    try:
                        bowl_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)        
                    
                        if int(bowl_msg.content) < 1 or int(bowl_msg.content) > 6:
                            await ctx.send("Invalid input.")
                        
                        elif int(bowl_msg.content) != sys_ch:
                            sys_score = sys_score + sys_ch
                            await ctx.send(embed=embed_score)
                            await ctx.send(f'**System score:** {sys_score}')
                        
                        elif int(bowl_msg.content) == sys_ch:
                            sys_wick = sys_wick + 1
                            await ctx.send(embed=embed_out)
                    
                    except asyncio.TimeoutError:
                        await ctx.send("Sorry. you did not gave input in time. Game over!\n\n Want to play again? Type `>cric` to sstart over the match.")
                        break
                
                # Final scorecard if system wins

                if sys_score > user_score:

                    embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}", inline=False)
                    embed_go.add_field(name="System Score: ", value=f"{sys_score}", inline=False)
                    embed_go.add_field(name="Result", value='What a game!! Well played both sides. However, today **system** won the game.', inline=False)
                    await ctx.send(embed=embed_go)

                # Final scorecard if user wins

                elif sys_score < user_score:
                    embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}")
                    embed_go.add_field(name="System Score: ", value=f"{sys_score}")
                    embed_go.add_field(name="Result", value=f'What a game!! Well played both sides. **{ctx.author}** won the game.', inline=False)
                    await ctx.send(embed=embed_go)
            
            elif sys_toss == (user_toss_ch):
                
                await ctx.send(embed=embed_toss_user_ch)
                user_ch_bb = await client.wait_for("message", timout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                if (user_ch_bb) == "bat":
                    
                    await ctx.send(embed=embed_toss_user)

                    # User batting

                    while (user_wick != 1):
                        try:
                            bat_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                            if int(bat_msg.content) < 1 or int(bat_msg.content) > 6: 
                                await ctx.send("Invalid input.")
                            
                            elif int(bat_msg.content) != sys_ch:
                                user_score = user_score + int(bat_msg.content)
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**{ctx.author.name} Score:** {user_score}')

                            elif int(bat_msg.content) == sys_ch:
                                user_wick = user_wick + 1
                                await ctx.send(embed=embed_out)

                        except asyncio.TimeoutError:
                            await ctx.send("Sorry. you did not gave input in time. Game over!")
                            break

                    embed_inning.add_field(
                        name=f'{ctx.author} Score',
                        value=f'{user_score}'
                    )
                    embed_inning.add_field(
                        name="System Score",
                        value=f'{sys_score}'
                    )
                    await ctx.send(embed=embed_inning)
                    await ctx.send(embed=embed_sec_start)

                    # System batting

                    while (sys_wick != 1) and (sys_score <= user_score):
                        try:
                            bowl_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)        
                        
                            if int(bowl_msg.content) < 1 or int(bowl_msg.content) > 6:
                                await ctx.send("Invalid input.")
                            
                            elif int(bowl_msg.content) != sys_ch:
                                sys_score = sys_score + sys_ch
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**System score:** {sys_score}')
                            
                            elif int(bowl_msg.content) == sys_ch:
                                sys_wick = sys_wick + 1
                                await ctx.send(embed=embed_out)
                        
                        except asyncio.TimeoutError:
                            await ctx.send("Sorry. you did not gave input in time. Game over!\n\n Want to play again? Type `>cric` to sstart over the match.")
                            break
                    
                    # Final scorecard if system wins

                    if sys_score > user_score:

                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}", inline=False)
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}", inline=False)
                        embed_go.add_field(name="Result", value='What a game!! Well played both sides. However, today **system** won the game.', inline=False)
                        await ctx.send(embed=embed_go)

                    # Final scorecard if user wins

                    elif sys_score < user_score:
                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}")
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}")
                        embed_go.add_field(name="Result", value=f'What a game!! Well played both sides. **{ctx.author}** won the game.', inline=False)
                        await ctx.send(embed=embed_go)
                
                elif user_ch_bb == "bowl":

                    await ctx.send (embed=embed_toss_user)

                    # System batting

                    while (sys_wick != 1) and (sys_score <= user_score):
                        try:
                            bowl_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)        
                        
                            if int(bowl_msg.content) < 1 or int(bowl_msg.content) > 6:
                                await ctx.send("Invalid input.")
                            
                            elif int(bowl_msg.content) != sys_ch:
                                sys_score = sys_score + sys_ch
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**System score:** {sys_score}')
                            
                            elif int(bowl_msg.content) == sys_ch:
                                sys_wick = sys_wick + 1
                                await ctx.send(embed=embed_out)
                        
                        except asyncio.TimeoutError:
                            await ctx.send("Sorry. you did not gave input in time. Game over!\n\n Want to play again? Type `>cric` to sstart over the match.")
                            break

                    embed_inning.add_field(
                        name=f'{ctx.author} Score',
                        value=f'{user_score}'
                    )
                    embed_inning.add_field(
                        name="System Score",
                        value=f'{sys_score}'
                    )
                    await ctx.send(embed=embed_inning)
                    await ctx.send(embed=embed_sec_start)                

                    # User batting

                    while (user_wick != 1):
                        try:
                            bat_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                            if int(bat_msg.content) < 1 or int(bat_msg.content) > 6: 
                                await ctx.send("Invalid input.")
                            
                            elif int(bat_msg.content) != sys_ch:
                                user_score = user_score + int(bat_msg.content)
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**{ctx.author.name} Score:** {user_score}')

                            elif int(bat_msg.content) == sys_ch:
                                user_wick = user_wick + 1
                                await ctx.send(embed=embed_out)

                        except asyncio.TimeoutError:
                            await ctx.send("Sorry. you did not gave input in time. Game over!")
                            break
                    
                    # Final scorecard if system wins

                    if sys_score > user_score:

                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}", inline=False)
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}", inline=False)
                        embed_go.add_field(name="Result", value='What a game!! Well played both sides. However, today **system** won the game.', inline=False)
                        await ctx.send(embed=embed_go)

                    # Final scorecard if user wins

                    elif sys_score < user_score:
                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}")
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}")
                        embed_go.add_field(name="Result", value=f'What a game!! Well played both sides. **{ctx.author}** won the game.', inline=False)
                        await ctx.send(embed=embed_go)

        except asyncio.TimeoutError:
            await ctx.send("Sorry. You did not gave input in time. Try again by running the game again")        

    @cric.command(name="help")
    async def help(ctx):

        # EMBED SETTINGS
        embed_rules = discord.Embed(
            title="CricBot Rules",
            url="https://github.com/Raveesh1505/CricBot",
            description=f'{RULES}',
            color= discord.Color.red()
        )

        embed_rules.set_footer(text='CricBot! The ultimate cricket discord bot.')
        embed_rules.set_thumbnail(url="https://github.com/Raveesh1505/CricBot/blob/main/CRIC%20BOT.png?raw=true")

        await ctx.send(embed=embed_rules)


# Run the bot
client.run(TOKEN)
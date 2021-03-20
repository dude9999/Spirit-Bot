import discord
from discord.ext import commands, tasks
import random
import praw
from random import choice
import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv('.env')

reddit = praw.Reddit(client_id = os.getenv('CLIENT_ID'),
                     client_secret = os.getenv('CLIENT_SECRET'),
                     username = os.getenv('USERNAME'),
                     password = os.getenv('PASSWORD'),
                     user_agent = os.getenv('USER_AGENT'))

# intents 
intents = discord.Intents.all()

# prefix
client = commands.Bot(command_prefix = ["s.","S."], intents=intents)
client.remove_command('help')


# saying the bot is active/ready
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

# status of Bot
@tasks.loop(seconds=15)
async def change_status():
  statuses = ['s.help','DTS']
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=choice(statuses)),status=discord.Status.idle)
  

# RESTART COMMAND
@client.command(aliases=['shutdown','logout'])
@commands.is_owner()
async def shut(ctx):
    await ctx.message.add_reaction('✅')
    await ctx.send('Shutting down the bot!')
    await client.close()

@shut.error
async def shut_error(ctx, error):
  await ctx.message.add_reaction('❌')
  if isinstance(error, commands.CheckFailure):

      em = discord.Embed(color=discord.Color.blue())
      em.add_field(name=':warning:  ALERT  :warning:',value='<a:pepeFoff:802977689736314900>  You\'re not <@710247495334232164> to perform this action!')
      await ctx.send(embed=em)

# meme command
@client.command()
async def meme(ctx):
    
    if not hasattr(client, 'nextMeme'):
        client.nextMeme = getMeme()

    name, url = client.nextMeme
    embed = discord.Embed(title = name)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    client.nextMeme = getMeme()

def getMeme():
    all_subs = []
    subreddit = reddit.subreddit("dankmemes")   
    top = subreddit.top(limit=150)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    return name, url

# animal images
# dog image 
@client.command()
async def dog(ctx):

    if not hasattr(client, 'nextDog'):
        client.nextDog = getDog()

    name, url = client.nextDog
    embed = discord.Embed(title = name)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    client.nextDog = getDog()

def getDog():
    all_subs = []
    subreddit = reddit.subreddit("Corgi")   
    top = subreddit.top(limit=100)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    return name, url

# cat image
@client.command()
async def cat(ctx):

    if not hasattr(client, 'nextCat'):
        client.nextCat = getCat()

    name, url = client.nextCat
    embed = discord.Embed(title = name)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    client.nextCat = getCat()

def getCat():
    all_subs = []
    subreddit = reddit.subreddit("Cats")   
    top = subreddit.top(limit=100)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    return name, url

# rip command
@client.command()
async def rip(ctx, member: discord.Member = None):

    if not member:
      member = ctx.author
 
    rip = Image.open('rip.jpg')
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.resize((300, 300))
    rip.paste(pfp, (265, 203))
    rip.save('./rip-user.jpg')
    await ctx.send(file=discord.File('./rip-user.jpg'))

# tic-tac-toe command
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.group(aliases=['tictactoe','TTT','TicTacToe'])
async def ttt(ctx, p1: discord.Member, p2: discord.Member = None):

  if not p2:
    p2 = ctx.author

    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command(aliases=['p'])
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the `sb!ttt` command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a player for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

      


# error handling
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("❌ That is not a valid command, try the commands that are mentioned in help command: `s.help`")


# COGS
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")



# token + others
client.run(os.getenv('DISCORD_TOKEN'))

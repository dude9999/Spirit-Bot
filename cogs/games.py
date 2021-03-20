import discord
from discord.ext import commands
import asyncio
import random
from random import randint
import datetime

class Games(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    # catch the pie
    @commands.command(aliases=['pie'])
    async def catch(self,ctx):
        
        # just building the embed
        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='🥧  __Catch The Pie Game__  🥧', value='To catch the pie you must simply react with the emoji, when it appears. Click as fast as you can and see how fast you caught it... \n**Good Luck!** \n\nHere we go in 3...', inline=False)
        pie1 = await ctx.send(embed=em)

        await asyncio.sleep(1)

        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='🥧  __Catch The Pie Game__  🥧', value='To catch the pie you must simply react with the emoji, when it appears. Click as fast as you can and see how fast you caught it... \n**Good Luck!** \n\nHere we go in 2..', inline=False)
        await pie1.edit(embed=em)

        await asyncio.sleep(1)

        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='🥧  __Catch The Pie Game__  🥧', value='To catch the pie you must simply react with the emoji, when it appears. Click as fast as you can and see how fast you caught it... \n**Good Luck!** \n\nHere we go in 1.', inline=False)
        await pie1.edit(embed=em)

        await asyncio.sleep(1)

        await pie1.add_reaction('🥧')

         # the actual magic behind the game
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji)

        before_wait = datetime.datetime.now()
        reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
        after_wait = datetime.datetime.now()
        time_delta = after_wait - before_wait
        time_taken = time_delta.total_seconds()

        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='🥧  __Catch The Pie Game__  🥧', value=f'To catch the pie you must simply react with the emoji, when it appears. Click as fast as you can and see how fast you caught it... \n**Good Luck!** \n\nYou caught it in **{time_taken} seconds**', inline=False)
        await pie1.edit(embed=em)

    # among us
    @commands.command(aliases = ['imposter','findimpostor','findimposter'])
    async def impostor(self, ctx):
        embed1 = discord.Embed(title = "Who's the imposter?" , description = "Find out who the imposter is, before the reactor breaks down!" , color=discord.Color.blue())
        
        # fields
        embed1.add_field(name = 'Red' , value= '<:red:818047547716796416>' , inline=False)
        embed1.add_field(name = 'Blue' , value= '<:blue:818047575319511061>' , inline=False)
        embed1.add_field(name = 'Lime' , value= '<:lime:818045625467666452>' , inline=False)
        embed1.add_field(name = 'Cyan' , value= '<:cyan:818047548346073088>' , inline=False)
        
        # sending the message
        msg = await ctx.send(embed=embed1)
        
        # emojis
        emojis = {
            'red': '<:red:818047547716796416>',
            'blue': '<:blue:818047575319511061>',
            'lime': '<:lime:818045625467666452>',
            'cyan': '<:cyan:818047548346073088>'
        }
        
        # who is the imposter?
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]
        
        # for testing...
        print(emojis[imposter])
        
        # adding choices
        for emoji in emojis.values():
            await msg.add_reaction(emoji)
        
        # a simple check, whether reacted emoji is in given choises.
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

        # waiting for the reaction to proceed
        try: 
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
        
        except TimeoutError:
            # reactor meltdown - defeat
            embed = discord.Embed(title="Defeat", description=f"Reactor Meltdown. {imposter} was the imposter...".format(imposter), color = discord.Color.red())
            embed.set_image(url='https://preview.redd.it/7k5gzsbifco51.jpg?width=960&crop=smart&auto=webp&s=f997bdd801f3225d82de93d04fda906244bbd6a1')
            await ctx.send(embed=embed)
        else:
            # victory
            if str(self.reacted) == emojis[imposter]:
                embed = discord.Embed(title="Victory", description=f"**{imposter}** was the imposter, GG!".format(imposter), color = discord.Color.blue())
                embed.set_image(url='https://i.redd.it/xop0vuu00fr51.png')
                await ctx.send(embed=embed)

            # defeat
            else:
                for key, value in emojis.items(): 
                    if value == str(self.reacted):
                        embed = discord.Embed(title="Defeat", description=f"Your choice was wrong, **{imposter}** was the imposter...".format(key), color = discord.Color.red())
                        embed.set_image(url='https://preview.redd.it/7k5gzsbifco51.jpg?width=960&crop=smart&auto=webp&s=f997bdd801f3225d82de93d04fda906244bbd6a1')
                        await ctx.send(embed=embed)
                        break


    # rock paper scissors
    @commands.command(aliases=['rockpaperscissors'])
    async def rps(self, ctx):
        try:
            rpsEmbed = discord.Embed(color=random.randint(
                0, 0xffffff))
            rpsEmbed.add_field(name='Rock', value='\U0001faa8')
            rpsEmbed.add_field(name='Paper', value='\U0001f4dc')
            rpsEmbed.add_field(name='Scissors', value='\U00002702')
            rpsEmbed.set_footer(text='the message you will be deleted after 1 min')
            question_choose = await ctx.send(embed=rpsEmbed)
            await question_choose.add_reaction('\U0001faa8')
            await question_choose.add_reaction('\U0001f4dc')
            await question_choose.add_reaction('\U00002702')
            reaction, user = await self.client.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and str(reaction.emoji), timeout=60)
            # list of selects 1# scissors 2# rock 3# paper
            selects = [u'\U00002702', u'\U0001faa8', u'\U0001f4dc']
            # choose random sleects from the list
            bot_select = random.choice(selects)
            print(str(bot_select))
            # save the emoji like a var
            user_select = str(reaction.emoji)
            print(str(user_select))
        # if the bot select equal user select its mean is a Tie
            if str(user_select) == str(bot_select):
                await question_choose.delete()
                # change the string select to a emoji
                if str(bot_select) == u'\U00002702':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='Tie', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
                # same
                elif str(bot_select) == u'\U0001faa8':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='Tie', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
                # same
                elif str(bot_select) == u'\U0001f4dc':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='Tie', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
            # if user_select is rock and check if the bot_select
            elif str(user_select) == u'\U0001faa8':
                await question_choose.delete()
                if str(bot_select) == u'\U00002702':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
                elif str(bot_select) == u'\U0001f4dc':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
            elif str(user_select) == u'\U0001f4dc':
                await question_choose.delete()
                if str(bot_select) == u'\U0001faa8':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
                elif str(bot_select) == u'\U00002702':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
            elif str(user_select) == u'\U00002702':
                await question_choose.delete()
                if str(bot_select) == u'\U0001faa8':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
                elif str(bot_select) == u'\U0001f4dc':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=choose_embed)
        except asyncio.TimeoutError:
            timeout = await ctx.send('The Time is end try again')
            await timeout.delete(delay=10)


    # roll dice
    @commands.command(aliases=['dice','diceroll'])
    async def roll(self, ctx):
        message = await ctx.send("Choose a number:\n**4**, **6**, **8**, **10**, **12**, **20** ")
        
        def check(m):
            return m.author == ctx.author

        try:
            message = await self.client.wait_for("message", check = check, timeout = 30.0)
            m = message.content

            if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
                await ctx.send("Sorry, invalid choice.")
                return
            
            await ctx.send(f"**{random.randint(1, int(m))}**")
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Process has been canceled because you didn't respond in **30 seconds**")

    # coinflip command
    @commands.command()
    async def flip(self,ctx):
        try:
            cancel = False
            EmbedHead = discord.Embed(title='__Coin Flipping Challenge__',color=discord.Color.blue())
            EmbedHead.add_field(name='What is your choice?', value='`Heads` or `Tails`', inline=False)
            EmbedHead.set_thumbnail(url='https://media1.tenor.com/images/38bf85bcecdd6aa52300d53e6eea06a1/tenor.gif')
            EmbedHead.set_footer(text='You have 1 minute to choose!')
            headORtail = await ctx.send(embed=EmbedHead)
            message = await self.client.wait_for('message',check=lambda m: m.author == ctx.author and m.channel == ctx.channel , timeout=60)
            if  str(message.content.lower()) == 'heads':
                user_choose = message.content
                fliping = await ctx.send('Flipping. ')
                await asyncio.sleep(1)
                await fliping.edit(content='Flipping.. ')
                chooses = ['heads','tails']
                random_select = random.choice(chooses)
                if user_choose == random_select:
                    choose_embed = discord.Embed(color=discord.Color.blue())
                    choose_embed.add_field(name='User :bust_in_silhouette:', value=f'{user_choose}',inline=False)
                    choose_embed.add_field(name='Bot :robot:',value=f'{random_select}',inline=False)
                    choose_embed.set_author(name='You Win',icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    await ctx.send(embed=choose_embed)
                else:
                    choose_embed = discord.Embed(color=discord.Color.blue())
                    choose_embed.add_field(name='User :bust_in_silhouette:' ,value=f'{user_choose}',inline=False)
                    choose_embed.add_field(name='Bot :robot:', value=f'{random_select}',inline=False)
                    choose_embed.set_author(name='You Lose',icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    await ctx.send(embed=choose_embed)
            if str(message.content.lower()) == 'tails':
                user_choose = message.content
                fliping = await ctx.send('Flipping. ')
                await asyncio.sleep(1)
                await fliping.edit(content='Flipping.. ')
                chooses = ['heads','tails']
                random_select = random.choice(chooses)
                if user_choose == random_select:
                    choose_embed = discord.Embed(color=discord.Color.blue())
                    choose_embed.add_field(name='User :bust_in_silhouette:', value=f'{user_choose}',inline=False)
                    choose_embed.add_field(name='Bot :robot:',value=f'{random_select}',inline=False)
                    choose_embed.set_author(name='You Win',icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    await ctx.send(embed=choose_embed)
                else:
                    choose_embed = discord.Embed(color=discord.Color.blue())
                    choose_embed.add_field(name='User :bust_in_silhouette:' ,value=f'{user_choose}',inline=False)
                    choose_embed.add_field(name='Bot :robot:', value=f'{random_select}',inline=False)
                    choose_embed.set_author(name='You Lose',icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    await ctx.send(embed=choose_embed)
        except asyncio.TimeoutError:
            if not cancel:
                await headORtail.delete()
                await ctx.send('The time ended, please try again')

    
    # guess number
    @commands.command()
    async def guess(self,ctx):
        await ctx.send("Please guess number between 1 and 10")
        answer = randint(1, 10)
        print(answer)

        def check(self,message):
            try:
                int(message.content)
                return True
            except ValueError:
                return False

        msg = await self.client.wait_for('message', check=check)
        guess = int(msg.content)
        tries = 0
        while tries != 3:
            if guess == answer:
                await ctx.send("You got it the first time")
                break
            if guess < answer:
                await ctx.send("Guess higher")
            elif guess > answer:
                await ctx.send("Please guess lower")
                msg = await self.client.wait_for('message', check=check)
                guess = int(msg.content)
            elif guess == answer:
                    await ctx.send("You guessed correct")
                    break
            elif guess >= 3:
                await ctx.send("Sorry you guessed it in-correctly")
            tries += 1




def setup(client):
    client.add_cog(Games(client))

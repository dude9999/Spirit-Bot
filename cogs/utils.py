import discord
from discord.ext import commands
import asyncio

class Utils(commands.Cog):
    def __init__(self,client):
        self.client = client


    # reminder command
    @commands.command()
    async def remind(self, ctx, mins : int, *, reminder):

        if mins > 60:
            await ctx.send("The limit for a reminder is 60 minutes!")
            return

        embed=discord.Embed(title='Reminder set', description=f"{ctx.author.mention}, I have set a reminder for {mins} minutes with the reminder being {reminder}", colour=discord.Colour.blue())
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed=embed)

        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            if counter == int(mins):
                await ctx.send(f"{ctx.author.mention}, your reminder for {reminder} with a time of {mins} minutes has gone off.")
                break

    # poll command
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def poll(self, ctx,*,message):
        await ctx.message.delete()
        embed = discord.Embed(title = f"__{message}__", description = '✅ = Yes\n❌ = No', color = discord.Color.blue()) 
        embed.set_footer(text=f'Poll by {ctx.author.name}')
        msg = await ctx.channel.send(embed = embed)
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')

    @poll.error
    async def poll_error(self,ctx,error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send('You are not allowed to run polls')

    # ask command
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def ask(self, ctx,*,message):
        await ctx.message.delete()
        embed = discord.Embed(title = f"__{message}__", description = '✅ = Yes\n❌ = No', color = discord.Color.blue()) 
        embed.set_footer(text=f'Asked by {ctx.author.name}')
        msg = await ctx.channel.send(embed = embed)
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')

    @ask.error
    async def ask_error(self,ctx,error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send('You are not allowed to ask questions')

    # countdown command
    @commands.command(pass_context = True)
    async def countdown(self, ctx, seconds, *, title):
        counter = 0
        try:
            secondint = int(seconds)
            if secondint > 300:
                await ctx.send("I dont think im allowed to do go above 300 seconds \U0001f914")
                raise BaseException
            if secondint < 0 or secondint == 0:
                await ctx.send("I dont think im allowed to do negatives \U0001f914")
                raise BaseException
            message = await ctx.send("```py" + "\n" + "[" + title +"]" + "\nTimer: " + seconds + "```")
            while True:
                secondint = secondint - 5
                if secondint == 0:
                    await ctx.edit_message(message, new_content=("```Ended!```"))
                    break
                await ctx.edit_message(message, new_content=("```py" + "\n" + "[" + title + "]" + "\nTimer: {0}```".format(secondint)))
                await asyncio.sleep(5.0)
            await ctx.send_message(ctx.message.channel, ctx.message.author.mention + " Your countdown " + "[" + title + "]"  + " Has ended!")
        except ValueError:
            await ctx.send("Must be a number!")



def setup(client):
  client.add_cog(Utils(client))

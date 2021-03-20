import discord
from discord.ext import commands
import wikipedia
import asyncio
import random
import time
from aiohttp import ClientSession
import datetime

start_time = time.time()

class Fun(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    # wiki search command
    @commands.command(aliases=['search'])
    async def wiki(self, ctx, *, question):
        try:
            embed= discord.Embed(color=0x07C9F5,timestamp=ctx.message.created_at)
            embed.add_field(name="✅ Searched-",value=f"`{wikipedia.summary(question, sentences=2)}`", inline=True)
            await ctx.send(embed=embed)
        except:
            embed= discord.Embed(title = "‎‎❌ Invalid command",color=0x07C9F5)
            await ctx.send(embed=embed)

    # hack command
    @commands.command(aliases=['h'])
    async def hack(self, ctx, member: discord.Member):

        used_words = ['Nerd','Sucker','Noob','Sup','Yo','Wassup','Nab','Nub','fool','stupid','b1tch','fvck','idiot']
        mails = ['@gmail.com','@hotmail.com','@yahoo.com']

        hacking = await ctx.send(f"Hacking {member.name}.....")
        await asyncio.sleep(1.5)
        await hacking.edit(content='Finding info....')
        await asyncio.sleep(1.5)
        await hacking.edit(content=f"Discord email address: {member.name}{random.choice(mails)}")
        await asyncio.sleep(2)
        await hacking.edit(content=f"Password: x2yz{member.name}xxy65")
        await asyncio.sleep(2)
        await hacking.edit(content=f'Most used words: {random.choice(used_words)}')
        await asyncio.sleep(1.5)
        await hacking.edit(content='IP address: 127.0.0.1:50')
        await asyncio.sleep(1.5)
        await hacking.edit(content='Selling information to the government....')
        await asyncio.sleep(2)
        await hacking.edit(content=f'Reporting {member.name} to Discord for violating ToS')
        await asyncio.sleep(2)
        await hacking.edit(content='Hacking medical records.....')
        await asyncio.sleep(1.5)
        await hacking.edit(content=f"{ctx.author.mention} successfully hacked {member.mention}")
        await ctx.send("The ultimate, real hacking has been done!")

    @hack.error
    async def hack_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌  You need to mention someone")

    # imagine command
    @commands.command(aliases=['imgne','im','i'])
    async def imagine(self, ctx, *, message):
        await ctx.send(f"**🤔  {ctx.author.name} is really trying hard to imagine:** {(message)}")

    @imagine.error
    async def imagine_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌  What do you want to imagine?")

    # spoiler command
    @commands.command(aliases=['s', 'sp'])
    async def spoiler(self, ctx, *, message):
        await ctx.send(f"||{(message)}||")

    @spoiler.error
    async def spoiler_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌  What's your message?")

    # cell phone command
    @commands.group(aliases=['cell'], invoke_without_command=True)
    async def phone(self, ctx):
        await ctx.send(f'What do you want to do with your phone {ctx.author.mention}? \n`s.phone a`  **Call friend** \n`s.phone b`  **Call for emergency help** \n`s.phone c`  **Call DTS** \n`s.phone d`  **Exit phone**')

    @phone.command()
    async def a(self, ctx):
        friend = ['**You:** Hi \n**Friend:** Hello \n**You:** How are you \n**Friend:** im good, hru \n**You:** Good','**You:** Hey \n**Friend:** Wassup \n**You:** nothing \n**Friend:** Why did u call \n**You:** Simply \n**Friend:** Bruh','**You:** Hey man hru \n**Friend:** Not that great \n**You:** why? \n**Friend:** ....']
        await ctx.send(f"{random.choice(friend)} \n`Call ended`")

    @phone.command()
    async def b(self, ctx):
        responses = ['You dialed 911, they declined your call and you died... RIP', 'You called 911, they came to rescue you, phew!', 'You played prank on the emergency, they shot you and you died, LMFAO :rofl:']
        await ctx.send(f"{random.choice(responses)} \n`Call ended`")

    @phone.command()
    async def c(self, ctx):
        answers =["**You:** Hello, I'm a big fan of you \n**DTS:** Thanks!", "**You:** Hey, I wanna recommend a new command \n**DTS:** oof finally, someone recommended something... What is it? \n**You:** Nothing \n**DTS:** are you serious, thats it ur getting BLACKLISTED and BANNED...", f"**You:** why did you make a bad bot? \n**DTS:** Why would I make a good bot smh?, {ctx.author.name}."]
        await ctx.send(f"{random.choice(answers)} \n`Call ended`")

    @phone.command()
    async def d(self, ctx):
        no_phone = ['Alright, you threw the phone away.', 'Looks like we are not using our phone today', 'Hmmm you dont wanna use your phone, well YEET *(throws the phone to a nearby pond)*']
        await ctx.send(f'{random.choice(no_phone)}')

    # quote command
    @commands.command(aliases=['q'])
    async def quote(self, ctx, *, message):
        await ctx.send(f"'{message}'   \n- **{ctx.author.name}**")

    @quote.error
    async def quote_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌  What do you want to quote?")

    # reverse command
    @commands.command(aliases=['rev'])
    async def reverse(self, ctx, *, arg):
        await ctx.send(arg[::-1])

    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌  Put a msg to reverse")

    # howgay command
    @commands.command(aliases=['gay','gayrate', 'hg'])
    async def howgay(self, ctx, member: discord.Member=None):

        if not member:
            member = ctx.author

        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name="__Gay Rate Calculator__", value=f'{member.name} is `{random.randint(1,99)}%` gay', inline=False)
        em.set_footer(text='Prefix- s.')
        await ctx.send(embed=em)

    # simprate command
    @commands.command(aliases=['sr','simp'])
    async def simprate(self, ctx, member: discord.Member=None):

        if not member:
            member = ctx.author

        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name="<a:sb_simp:815527600230367252>  __Simp Rate Calculator__  <a:sb_simp:815527600230367252>", value=f'{member.name} is `{random.randint(1,99)}%` simp', inline=False)
        em.set_footer(text='Prefix- s.')
        await ctx.send(embed=em)

    # choose command
    @commands.command(aliases=['ch'])
    async def choose(self, ctx, m1, m2):
        random_selects = [m1,m2]
        await ctx.send(f"I choose `{random.choice(random_selects)}`.")

    @choose.error
    async def choose_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌  What do you want me to choose between (2 things)")

    # love calculator command
    @commands.command()
    async def lovecalc(self, ctx, member:discord.Member):

        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='<a:vibes_heart:815527185627873290>  __Love Calculator__  <a:vibes_heart:815527185627873290>', value=f'{ctx.author.name} loves {member.name} `{random.randint(1,100)}%`', inline=False)
        em.set_footer(text='Prefix: s.')
        await ctx.send(embed=em)

    @lovecalc.error
    async def lovecalc_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Mention anyone you want to do the love test, you cant test yourself')

    # dadjoke command
    @commands.command(aliases=['dj'])
    async def dadjoke(self, ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-key': "81dd963d15mshf3e3a91dd6fe3cap1d971djsnbeb11a691831",
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com" 
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n||{r['punchline']}||")

    # avatar command
    @commands.command(aliases=['avatar','profile','pfp'])
    async def av(self, ctx, member: discord.Member=None):

        if not member:
            member = ctx.author
        
        em = discord.Embed(title=f"Avatar of {member.name}", color=discord.Color.blue())
        em.set_image(url=member.avatar_url)
        em.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=em)

    # uptime command
    @commands.command(aliases=['uptym','ut'])
    async def uptime(self,ctx):

        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))

        embed = discord.Embed(colour=discord.Color.blue())
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Prefix: s.")
        await ctx.send(embed=embed)

    # say command
    @commands.command(aliases=['repeat'])
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message=None):

        await ctx.message.delete()
        await ctx.send(message)

    # react command
    @commands.command()
    async def react(self, ctx,emoji):
        await ctx.message.add_reaction(emoji)

    # status command
    @commands.command()
    async def status(self, ctx, member: discord.Member=None):

        if not member:
            member = ctx.author

            await ctx.send(f"{member.name}'s status: **{str(member.status)}**")

    # reply command
    @commands.command()
    async def reply(self, ctx,*,message=None):
        if not message:
            message = ctx.author
            await ctx.reply('I replied!')

    # emojify command
    @commands.command()
    async def emojify(self, ctx, emoji):
        await ctx.send(emoji)




def setup(client):
  client.add_cog(Fun(client))

import discord
from discord.ext import commands
import random
import asyncio

class Giveaway(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def gstart(self, ctx, time:str, prize,*,winner):
    await ctx.message.delete()
    time_convert = {"s":1, "m":60, "h":3600,"d":3600*24}
    newtime= int(time[:-1]) * time_convert[time[-1]]
 
    em = discord.Embed(title='🎉  New Giveaway!  🎉',color=discord.Color.blue())
    em.add_field(name='Prize:', value=f"{prize}", inline=True)
    em.add_field(name='Host:', value=f'{ctx.author.mention}', inline=False)
    em.add_field(name='Time:', value=f"{time}", inline=True)
 
    msg = await ctx.send(embed=em)
 
    await msg.add_reaction('🎉')
    await asyncio.sleep(newtime)

    msg = await msg.channel.fetch_message(msg.id)

    winner = None
 
    for reaction in msg.reactions:
      if reaction.emoji == "🎉":
        users = await reaction.users().flatten()
        users.remove(self.client.user)
        winner = random.choice(users)
      if winner is not None:
        endembed = discord.Embed(title="Giveaway ended!", description="**Prize:** {}\n**Winner:** {}".format(prize, winner.mention))
  
        await msg.edit(embed=endembed)
        await ctx.send(f'{winner.mention} has won the giveaway for **__{prize}__**')
 
  @gstart.error
  async def giveaway_error(self, ctx, error):
    if isinstance(error,commands.CheckFailure):
      await ctx.send('You are not allowed to host giveaways!')

  # reroll command
  @commands.command(aliases=['gend'])
  @commands.has_permissions(manage_messages=True)
  async def greroll(self, ctx, id_ : int, channel : discord.TextChannel = None):

    if not channel:
      channel = ctx.channel

    try:
      new_msg = await channel.fetch_message(id_)
    except:
      await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(self.client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations the new winner is: {winner.mention} for the giveaway!")



def setup(client):
  client.add_cog(Giveaway(client))

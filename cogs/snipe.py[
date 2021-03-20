import discord
from discord.ext import commands
import asyncio

# some things that is a must
color = discord.Color.blue()
snipe_message_author = {}
snipe_message_content = {}
snipe_message_author_avatar = {}

esnipe_message_author = {}
esnipe_message_content = {}
esnipe_message_author_avatar = {}


class Snipe(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.Cog.listener()
  async def on_message_delete(self, message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    snipe_message_author_avatar[message.channel.id] = message.author.avatar_url
    await asyncio.sleep(60)
    
    try:
      del snipe_message_author[message.channel.id]
      del snipe_message_content[message.channel.id]
      del snipe_message_author_avatar[message.channel.id]

    except:
      pass

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    esnipe_message_author[before.channel.id] = before.author
    esnipe_message_content[before.channel.id] = before.content
    esnipe_message_author_avatar[before.channel.id] = before.author.avatar_url
    await asyncio.sleep(60)

    try:
      del esnipe_message_author[before.channel.id]
      del esnipe_message_content[before.channel.id]
      del esnipe_message_author_avatar[before.channel.id]

    except:
      pass

  @commands.command()
  async def snipe(self, ctx):

    channel = ctx.channel

    try:
      em = discord.Embed(title = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
      em.set_footer(text = f"Message sent by {snipe_message_author}")
      em.set_author(name=snipe_message_author[channel.id], icon_url=snipe_message_author_avatar[channel.id])
      await ctx.send(embed = em)

    except:
      await ctx.send("Uh oh! There's nothing to snipe.")

  @commands.command(aliases=['esnipe'])
  async def editsnipe(self, ctx):

    channel = ctx.channel

    try:
      em = discord.Embed(title = f"Last edited message in #{channel.name}", description = esnipe_message_content[channel.id])
      em.set_footer(text = f"Message sent by {snipe_message_author}")
      em.set_author(name=esnipe_message_author[channel.id], icon_url=esnipe_message_author_avatar[channel.id])
      await ctx.send(embed = em)

    except:
      await ctx.send("There's nothing to snipe!")


def setup(client):
  client.add_cog(Snipe(client))

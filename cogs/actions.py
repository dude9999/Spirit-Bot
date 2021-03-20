import discord
from discord.ext import commands
import random

class Actions(commands.Cog):
  def __init__(self,client):
    self.client = client


  # emotions commands
  # hug command
  @commands.command()
  async def hug(self, ctx, member: discord.Member):
    gifs = ['https://media.tenor.com/images/89d1029df24856b6f49eb91ec85fe020/tenor.gif','https://media.tenor.com/images/7fd97036fe16f839730ce7721bcedcae/tenor.gif','https://media.tenor.com/images/d918d53679eef0ce0f441cb5bd65dffe/tenor.gif','https://media.tenor.com/images/09857e9e97959a713d480ec494e81962/tenor.gif']
    em = discord.Embed(title=f'{ctx.author.name} gives a hug to {member.name}', color=discord.Color.blue())
    em.set_image(url=random.choice(gifs))
    await ctx.send(embed=em)

  @hug.error
  async def hug_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 1 person who you wanna hug.")

  # wave command
  @commands.command()
  async def wave(self, ctx, member: discord.Member):
    gifs = ['https://c.tenor.com/_G4SJlstdSMAAAAj/kitty-heart.gif','https://c.tenor.com/6_-osAtLuHUAAAAj/wave-cute.gif','https://media.tenor.com/images/e6afa2be25c23e4c6f82f6e2faeb3400/tenor.gif','https://media1.tenor.com/images/f642e623a1b013cde443bb485969d49a/tenor.gif']
    em = discord.Embed(title=f'{ctx.author.name} waves at {member.name}', color=discord.Color.blue())
    em.set_image(url=random.choice(gifs))
    await ctx.send(embed=em)

  @wave.error
  async def wave_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 1 person who you wanna wave at.")

  # pat command
  @commands.command()
  async def pat(self, ctx, member: discord.Member):
    gifs = ['https://media.tenor.com/images/dfe3267cca9596be840fbf9d5e86b747/tenor.gif','https://media.tenor.com/images/5e0fcbf53276d7b05b6dbf90d38f7fde/tenor.gif','https://media.tenor.com/images/f50130ebede3f4abbe02d52c9a8c7172/tenor.gif','https://media.tenor.com/images/6ee55647893107a455e1bcbfbb57941b/tenor.gif']
    em = discord.Embed(title=f'{ctx.author.name} pats {member.name}', color=discord.Color.blue())
    em.set_image(url=random.choice(gifs))
    await ctx.send(embed=em)

  @pat.error
  async def pat_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 1 person who you wanna pat.")

  # slap command
  @commands.command()
  async def slap(self, ctx, member: discord.Member):
    gifs = ['https://c.tenor.com/YOa3VkjRI1MAAAAj/couple-hit.gif','https://c.tenor.com/x8iNGj9b_9kAAAAj/smack-blob.gif','https://media.tenor.com/images/ac09dd389d43f3bc0adad6432a942532/tenor.gif','https://media.tenor.com/images/bd092fb261df4588a51f9dd1f4815fea/tenor.gif','https://media.tenor.com/images/a74401322cdf4234b306acc7459c5619/tenor.gif']
    em = discord.Embed(title=f'{ctx.author.name} slaps {member.name}', color=discord.Color.blue())
    em.set_image(url=random.choice(gifs))
    await ctx.send(embed=em)

  @slap.error
  async def slap_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 1 person who you wanna slap.")

  # fight command
  @commands.command()
  async def fight(self, ctx, member: discord.Member):
    gifs = ['https://c.tenor.com/UntLK5ZsfrAAAAAM/my-hero-academia-fight.gif','https://c.tenor.com/1hRatB4Sj9sAAAAM/mha907-fight.gif','https://c.tenor.com/xiWWxKFKAesAAAAM/fight-my-hero-academia.gif','https://c.tenor.com/rOFmitdU79oAAAAM/fight-bakugo.gif','https://c.tenor.com/RWLP_ymCg_QAAAAM/all-might-my-hero-academia.gif','https://c.tenor.com/RU7qYqx8_RcAAAAM/deku-kacchan.gif']
    em = discord.Embed(title=f'{ctx.author.name} fights {member.name}', color=discord.Color.blue())
    em.set_image(url=random.choice(gifs))
    await ctx.send(embed=em)

  @fight.error
  async def fight_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 1 person who you wanna fight with.")

  # fight command
  @commands.command()
  async def sad(self, ctx):
    gifs = ['https://c.tenor.com/4SvKpabSPooAAAAM/toga-himiko-anime.gif','https://c.tenor.com/Sfnari3piLAAAAAM/no-deku.gif','https://c.tenor.com/EnZFmgjBaGcAAAAM/tsu-tsuyu-asui.gif','https://c.tenor.com/awOueZ7ZHq4AAAAM/hysterical-crying-mineta.gif','https://c.tenor.com/Iv6MgTK1cPIAAAAM/owo-cry.gif','https://c.tenor.com/FepKKb14wwwAAAAM/anime-my-hero-academia.gif']
    em = discord.Embed(title=f'{ctx.author.name} is sad', color=discord.Color.blue())
    em.set_image(url=random.choice(gifs))
    await ctx.send(embed=em)


def setup(client):
  client.add_cog(Actions(client))

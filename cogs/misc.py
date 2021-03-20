import discord
from discord.ext import commands

class Misc(commands.Cog):
  def __init__(self, client):
    self.client = client

  # vote command
  @commands.command()
  async def vote(self, ctx):
    em = discord.Embed(color=discord.Color.blue())
    em.set_author(name='Vote for Spirit')
    em.add_field(name='__discordbotlist.com__',value='[`Vote for me`](https://discordbotlist.com/bots/spirit-v2/upvote)', inline=False)
    em.add_field(name='__top.gg__',value='[`Vote for me`](https://top.gg/bot/809066203485306912/vote)', inline=False)
    em.set_thumbnail(url='https://st2.depositphotos.com/1742172/9626/v/950/depositphotos_96260568-stock-illustration-cartoon-ballot-box.jpg')
    em.set_footer(text="You can vote every 12 hours", icon_url = ctx.author.avatar_url)
    await ctx.send(embed=em)

  # invite command
  @commands.command(aliases=['links', 'link'])
  async def invite(self, ctx):
      em=discord.Embed(title='Spirit Bot', description='Soo planning on adding the bot or want help?', color=discord.Color.blue())
      em.add_field(name='__Bot Invite__', value='[Click here](https://discord.com/api/oauth2/authorize?client_id=809066203485306912&permissions=2617633910&scope=bot) to invite me', inline=True)
      em.add_field(name='__Get support__', value='[Click here](https://discord.gg/WhNVDTF)', inline=True)
      em.add_field(name='🔗  Some important links:', value ='[Invite](https://discord.com/api/oauth2/authorize?client_id=809066203485306912&permissions=2617633910&scope=bot), [YouTube](https://www.youtube.com/c/TheCreativeSquadYT), [Twitter](https://twitter.com/official_DTS_11), [Instagram](https://instagram.com/official_dts_11)', inline=False)
      em.set_thumbnail(url=self.client.user.avatar_url)
      em.set_footer(text= 'Prefix- s.')
      await ctx.send(embed=em)

  # support command
  @commands.command()
  async def support(self, ctx):
    await ctx.send('Did you say u want help? Join here and ask your doubts!\nhttps://discord.gg/WhNVDTF')

  # ping of bot
  @commands.command(aliases=['latency','pong'])
  async def ping(self, ctx):
      await ctx.send(f'🏓 Pong! {round(self.client.latency * 1000)}ms')

  # suggest command
  @commands.command()
  async def suggest(self, ctx,*,suggestion):

    em = discord.Embed(color=discord.Color.blue())
    em.add_field(name='__New suggestion!__', value=suggestion, inline=False)
    em.set_footer(text=f'Sent by {ctx.author}', icon_url = ctx.author.avatar_url)
    await ctx.send(f'{ctx.author.mention}, Your suggestion has been recorded!')

    channel = self.client.get_channel(818927218884345866)

    await channel.send(embed=em)



def setup(client):
  client.add_cog(Misc(client))

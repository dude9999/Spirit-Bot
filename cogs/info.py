import discord
from discord.ext import commands

class Info(commands.Cog):
  def __init__(self,client):
    self.client = client

  # userinfo command
  @commands.command(aliases=['me','ui'])
  async def userinfo(self, ctx, member: discord.Member=None):

      if not member:
        member = ctx.author

      roles = [role for role in member.roles]

      em = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
      em.set_author(name = f"User info of {member}")
      em.set_thumbnail(url = member.avatar_url)
      em.add_field(name='ID', value=member.id, inline=False)
      em.add_field(name='Guild name', value=member.display_name, inline=False)
      em.add_field(name='Account creation', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M, %p UTC"), inline=False)
      em.add_field(name='Date joined', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M, %p UTC"), inline=False)
      em.add_field(name=f"Roles ({len(roles)})", value=" ".join ([role.mention for role in roles]), inline=False)
      em.add_field(name='Bot', value=member.bot, inline=False)
      em.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

      await ctx.send(embed=em)
    
  # server info command
  @commands.command(aliases=['si','server'])
  async def serverinfo(self, ctx):
      em = discord.Embed(color=discord.Color.blue(), title=f"{ctx.guild.name}")
      em.set_thumbnail(url=f"{ctx.guild.icon_url}")
      em.add_field(name='<:owner:811749694744297502>  Server Owner', value=f"`{ctx.guild.owner}`", inline=True)
      em.add_field(name='<:region:811750344685125675>  Region', value=f"`{ctx.guild.region}`", inline=True)
      em.add_field(name='<:textthumbsup:819941761467416584>  Roles', value=f"`{len(ctx.guild.roles)}`", inline=True)
      em.add_field(name='<:memberlist:811747305543434260>  Members', value=f"`{ctx.guild.member_count}`", inline=True)
      em.add_field(name='<:memberlist:811747305543434260>  Humans', value=f"`{len([m for m in ctx.guild.members if not m.bot])}`", inline=True)
      em.add_field(name='<:bot:802614960038608956>  Bots', value=f"`{sum(member.bot for member in ctx.guild.members)}`", inline=True)
      em.add_field(name='<:textchannel:811747767763992586>  Text channels',value=f"`{len(ctx.guild.text_channels)}`", inline=True)
      em.add_field(name='<:voicechannel:811748732906635295>  Voice channels',value=f"`{len(ctx.guild.voice_channels)}`", inline=True)
      em.add_field(name='📁  Categories',value=f"`{len(ctx.guild.categories)}`", inline=True)
      em.set_footer(icon_url=f"{ctx.guild.icon_url}", text=f"Guild ID: {ctx.guild.id}")
      await ctx.send(embed=em)

  # info command
  @commands.command(aliases=['information', 'stats', 'statistics'])
  async def info(self, ctx):

    server_count = len(self.client.guilds)
    total_members = len(set(self.client.get_all_members()))

    em = discord.Embed(color=discord.Color.blue())
    em.add_field(name='Bot Info', value="<:botdevbadge:804721967289991189>  Developer: <@710247495334232164>\n🗓️  Date created: `10 Feb 2021`\n<:python:819942756314906655>  Language: `Python 3`\n", inline=False)
    em.add_field(name='Bot Stats', value=f"<:partnerbadge:819942435550396448>  Servers: `{server_count} servers`\n<:memberlist:811747305543434260>  Members: `{total_members} members`")
    await ctx.send(embed=em)




def setup(client):
  client.add_cog(Info(client))

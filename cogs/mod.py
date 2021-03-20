import discord
from discord.ext import commands
import asyncio

class Mod(commands.Cog):
  def __init__(self,client):
    self.client = client

  
  # change nickname command
  @commands.command(aliases=['sn'])
  @commands.has_permissions(manage_roles=True)
  async def setnick(self, ctx, member: discord.Member, *, nick=None):

    if nick is None:
      await ctx.send('What should the new nick-name be? You didn\'t mention that.')

    else:
      await member.edit(nick=nick)
      await ctx.send(f'Nickname for {member.name} was changed to {member.mention}')

  @setnick.error
  async def setnick_perms(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
      await ctx.send("You don't have the permission to do this.")

  # slow-mode command
  @commands.command(aliases=['sm'])
  @commands.has_permissions(manage_messages=True)
  async def slowmode(self, ctx, seconds: int=None):

      if seconds is None:
        seconds = ctx.channel.slowmode_delay
        await ctx.send(f'The slowmode in this channel is `{seconds} seconds`')

      else:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slow-mode in this channel changed to **{seconds} seconds!**")

  @slowmode.error
  async def slowmode_error(self, ctx, error):
      if isinstance(error,commands.CheckFailure):
          await ctx.send('You cannot change the slow-mode of channels.')

  # lock the channel
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, role: discord.Role=None, channel : discord.TextChannel=None):

      role = role or ctx.guild.default_role
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(role)
      overwrite.send_messages = False

      await channel.set_permissions(role, overwrite=overwrite)
      await ctx.send(f'{ctx.channel.mention} is now locked for `{role.name}``.')

  @lock.error
  async def lock_error(self, ctx, error):
      if isinstance(error,commands.CheckFailure):
          await ctx.send('You do not have permission to use this command!')

  # unlock channel command
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, role: discord.Role=None, channel : discord.TextChannel=None):

    role = role or ctx.guild.default_role
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = True

    await channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'{ctx.channel.mention} has been unlocked for `{role.name}``.')

  @unlock.error
  async def unlock_error(self, ctx, error):
      if isinstance(error,commands.CheckFailure):
          await ctx.send('You do not have permission to use this command!')

  # clear messages
  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount= 100):

      await ctx.channel.purge(limit=amount)
      await ctx.send(f'{amount} messages cleared by {ctx.author}', delete_after=2.5)

  @clear.error
  async def clear_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You're not allowed to clear messages")

  # kick member
  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):

      if reason is None:
        reason = 'No reason provided'
      await member.kick(reason=reason)

      em = discord.Embed(color=discord.Color.blue())
      em.add_field(name=f'{ctx.author} kicked {member} from {ctx.guild.name}', value=f'Reason: {reason}')
      await ctx.send(embed=em)

  @kick.error
  async def kick_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to kick people")

  # ban member
  @commands.command()
  @commands.has_guild_permissions(ban_members=True)
  async def ban(self, ctx, user: discord.Member, *, reason=None):

      if reason is None:
        reason = 'No reason provided'
      await user.ban(reason=reason)

      em = discord.Embed(color=discord.Color.blue())
      em.add_field(name=f'{ctx.author} banned {user} from {ctx.guild.name}', value=f'Reason: {reason}')
      await ctx.send(embed=em)

  @ban.error
  async def ban_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to ban people")

  # unban command
  @commands.command()
  @commands.has_guild_permissions(ban_members=True)
  async def unban(self, ctx, *, member):

    banned_users = await ctx.guild.bans()
    
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
      
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await self.ctx.guild.unban(user)
        
        await ctx.send(f"Unbanned: {user}")

  @unban.error
  async def unban_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to unban people")

  # mute command
  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):

      if not member:
          await ctx.send("Please specify a member")
          return

      if reason is None:
        reason = 'No reason provided'

      role = discord.utils.get(ctx.guild.roles, name="Muted")
      await member.add_roles(role)
      await ctx.send(f"{member.mention} has been muted, reason: {reason}")

  @mute.error
  async def mute_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to mute people")

  # temp-mute command
  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(manage_messages=True)
  async def tempmute(self, ctx, member: discord.Member,time,*,reason=None):

      if reason is None:
        reason = 'No reason provided'

      muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
      time_convert = {"s":1, "m":60, "h":3600,"d":86400}
      tempmute= int(time[0]) * time_convert[time[-1]]
      await member.add_roles(muted_role)
      embed = discord.Embed(description= f"{member.mention} has been temprarily muted, reason: {reason}", color=discord.Color.blue())
      await ctx.send(embed=embed)
      await asyncio.sleep(tempmute)
      await member.remove_roles(muted_role)

  @tempmute.error
  async def tempmute_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to temp-mute people")

  # unmute command
  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member):
      if not member:
          await ctx.send("Please specify a member")
          return
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      await member.remove_roles(role)
      await ctx.send(f"{member.mention} has been unmuted!")
  @unmute.error
  async def unmute_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send('You are not allowed to unmute people')

  # add role command
  @commands.command(aliases=['addr'])
  @commands.guild_only()
  @commands.has_guild_permissions(manage_roles=True)
  async def addrole(self, ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.message.add_reaction('✅')
    await ctx.send(f"Successfully given **{role.name}** to {user.mention}!")

  @addrole.error
  async def addrole_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to add role to people")

  # remove role command
  @commands.command(aliases=['rem-role'])
  @commands.guild_only()
  @commands.has_guild_permissions(manage_roles=True)
  async def removerole(self, ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.message.add_reaction('✅')
    await ctx.send(f"Successfully removed **{role.name}** from {user.mention}!")

  @removerole.error
  async def removerole_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          await ctx.send("You are not allowed to remove roles!")



def setup(client):
  client.add_cog(Mod(client))

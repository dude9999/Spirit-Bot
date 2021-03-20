import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,client):
        self.client = client

    # help command
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            color = discord.Color.blue()
        )
        em.set_author(name='Spirit Commands')
        em.add_field(name='🔨  Moderation  🔨', value='`s.help mod`', inline=False)
        em.add_field(name='🥳  Fun  🥳', value='`s.help fun`', inline=False)
        em.add_field(name='<a:rooClap:819957713890705439>  Actions  <a:rooClap:819957713890705439>', value='`s.help action`', inline=False)
        em.add_field(name='<:gamedev:819957465160220734>  Games  <:gamedev:819957465160220734>', value='`s.help game`', inline=False)
        em.add_field(name='🎉  Giveaway  🎉', value='`s.help giveaway`', inline=False)
        em.add_field(name='🛠️  Utilites  🛠️', value='`s.help utils`', inline=False)
        em.add_field(name='🧮   Mathematics  🧮', value='`s.help math`', inline=False)
        em.add_field(name='🔗  Some important links:', value ='[Invite](https://discord.com/api/oauth2/authorize?client_id=809066203485306912&permissions=2617633910&scope=bot), [YouTube](https://www.youtube.com/c/TheCreativeSquadYT), [Twitter](https://twitter.com/official_DTS_11), [Instagram](https://instagram.com/official_dts_11)', inline=False)
        em.set_image(url='https://media.discordapp.net/attachments/804760214456369172/813290154013622332/standard_1.gif')
        em.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=em)
        await ctx.send('https://discord.gg/WhNVDTF')

    # mod help
    @help.command()
    async def mod(self, ctx):
        em = discord.Embed(
            color = discord.Color.blue()
        )
        em.add_field(name='🔨  Moderation Commands  🔨', value ='`clear`, `kick`, `ban`, `unban`, `mute`, `unmute`, `tempmute`, `lock`, `unlock`, `slowmode`, `setnick`, `addrole <@user> <@role/ID>`, `removerole <@user> <@role/ID> `, `warn @user`', inline=False)
        em.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=em)

    # fun help
    @help.command()
    async def fun(self, ctx):
        em = discord.Embed(
            color = discord.Color.blue()
        )
        em.add_field(name='🥳  Fun Commands  🥳', value='`ping`, `dadjoke`, `imagine`, `quote`, `reverse`, `choose`, `spoiler`, `wiki`, `hack <@user>`, `snipe`, `poll`, `say`, `serverinfo`, `userinfo`, `vote`, `howgay`, `react`, `simprate`,`status`, `emojify`, `av`, `reply`, `phone`, `uptime`, `suggest`, `lovecalc`, `reminder`, `info`, `esnipe`', inline=False)
        em.add_field(name='📷  Image commands  📷', value='`meme`, `rip`, `dog`, `cat`', inline=False)
        em.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=em)

    # game help
    @help.command()
    async def game(self, ctx):
        embed = discord.Embed(
            color = discord.Color.blue()
        )
        embed.add_field(name='<:gamedev:819957465160220734>  Game Commands  <:gamedev:819957465160220734>',value='`catch`, `flip`, `rps`, `roll`, `ttt`, `guess`, `impostor`', inline=False)
        embed.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=embed)

    # emo help
    @help.command()
    async def action(self, ctx):
        embed = discord.Embed(
            color = discord.Color.blue()
        )
        embed.add_field(name='<a:rooClap:819957713890705439>  Emotion/Action Commands  <a:rooClap:819957713890705439>',value='`hug`, `slap`, `wave`, `pat`, `fight`, `sad`', inline=False)
        embed.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=embed)

    # math help
    @help.command()
    async def math(self, ctx):
        embed = discord.Embed(
            color = discord.Color.blue()
        )
        embed.add_field(name='🧮   Math Commands   🧮',value='`add`, `sub`, `multi`, `div`, `sqrt`', inline=False)
        embed.add_field(name='Command Usage:', value="This is the way to use the commands, no signs in middle, just the numbers with space. \n`s.add <no: 1> <no: 2>`")
        embed.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=embed)


    # giveaway help
    @help.command()
    async def giveaway(self, ctx):
        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='🎉  Giveaway  🎉', value='`gstart <time prize winner(s)>`, `greroll <msg_id>`, `gend <msg_id>`', inline=False)
        em.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=em)


    # utils help
    @help.command()
    async def utils(self,ctx):
        em = discord.Embed(color=discord.Color.blue())
        em.add_field(name='🛠️  Utility  🛠️', value='`taxcalc`, `cdn <time(secs)>`, `remind <time(mins)>`, `poll`, `ask`')
        em.set_footer(text= 'Prefix- s.')
        await ctx.send(embed=em)



def setup(client):
  client.add_cog(Help(client))

import discord
from discord.ext import commands

class Warns(commands.Cog):
    def __init__(self,client):
        self.client = client

    # warn command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self,ctx,member: discord.Member,*,reason):

        if member.id in [ctx.author.id, self.client.user.id]:
            return await ctx.send('You can\'t warn yourself.')
        
        if reason is None:
            reason = 'No reason provided'

        current_warn_count = len(
            await self.client.warns.find_many_by_custom(
                {
                    "user_id": member.id, 
                    "guild_id": member.guild.id
                }
            )
        ) + 1

        warn_filter = {"user_id": member.id, "guild_id": member.guild.id, "number": current_warn_count}
        warn_data = {"reason": reason, "timestamp": ctx.message.created_at, "warned_by": ctx.author.id}

        await self.client.warns.upsert_custom(warn_filter, warn_data)

        em = discord.Embed(
            title='You are being warned',
            description=f"__**Reason**__:\n{reason}",
            color=discord.Color.blue(),
            timestamp=ctx.message.created_at
            )
        em.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        em.set_footer(text=f"{current_warn_count}")

        try:
            await member.send(embed=em)
            await ctx.send('Warned that user in DM\'s')
        except discord.HTTPException:
            await ctx.send(member.mention, embed=em)



def setup(client):
    client.add_cog(Warns(client))

import discord
from discord.ext import commands
import asyncio

class Tax(commands.Cog):
    def __init__(self,client):
        self.client = client

    # dank tax calc
    @commands.command(aliases=['taxcalculator', 'tc'])
    async def taxcalc(self, ctx, num : int):

        if num < 0:
            await ctx.send("<a:seriously:805141760602800129>  Seriously, you know that currency can't go negatives unless its a loss...")

        if num == 0:
            await ctx.send("<:hmmm:819960230602473472>  Bruh its 0, u silly goose")

        if num > 0:
            embed=discord.Embed(title='Calculating Tax', description='Just a sec...',  color=discord.Color.orange())
            embed.set_footer(text="Prefix:  s.")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(1.25)

            calculation = round(num * 1.05263157895)
            amtLost = round(num * 1.052632 - num)
            z = round(num - amtLost)

            number_with_commas = '{:,}'.format(calculation)
            number_with_commas_amt_lost = '{:,}'.format(amtLost)
            to_calculate_with_commas = '{:,}'.format(num)
            user_gets_with_commas = '{:,}'.format(z)

            embed = discord.Embed(title='Dank Memer Tax Calculator',description=f"Amount to calculate```\n⏣ {to_calculate_with_commas}```\nAmount expected to pay```css\n⏣ {number_with_commas}```\nAmount lost by tax (5%)```diff\n- ⏣ {number_with_commas_amt_lost}```\nUser gets```fix\n⏣ {user_gets_with_commas}```",color=discord.Color.blue())
            embed.set_footer(text='Prefix: s.')
            
            await message.edit(embed=embed)




def setup(client):
    client.add_cog(Tax(client))

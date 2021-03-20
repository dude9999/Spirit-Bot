from discord.ext import commands
import math
import random

class Math(commands.Cog):
    def __init__(self,client):
        self.client = client

    # addition
    @commands.command(aliases=['add'])
    async def mathadd(self, ctx, x: float, y: float):
        def add(n: float, n2: float):
            return n + n2
        result = add(x, y)
        await ctx.send(result)

    # subtraction
    @commands.command(aliases=['sub','subtract'])
    async def mathsub(self, ctx, x: float, y: float):
        def sub(n: float, n2: float):
            return n - n2
        result = sub(x, y)
        await ctx.send(result)

    # random no:
    @commands.command(aliases=['random','rando'])
    async def mathrando(self, ctx, x: int, y: int):
        def rando(n: int, n2: int):
            return random.randint(n, n2)
        result = rando(x, y)
        await ctx.send(result)

    # division
    @commands.command(aliases=['div','divide'])
    async def mathdiv(self, ctx, x: float, y: float):
        def div(n: float, n2: float):
            return n / n2
        result = div(x, y)
        await ctx.send(result)

    # multiplication
    @commands.command(aliases=['mult','multi','multiply'])
    async def mathmulti(self, ctx, x: float, y: float):
        def mult(n: float, n2: float):
            return n * n2
        result = mult(x, y)
        await ctx.send(result)

    # square root
    @commands.command(aliases=['sqrt','squareroot'])
    async def mathsqrt(self, ctx, x: float):
        def sqrt(n: float):
            return math.sqrt(n)
        result = sqrt(x)
        await ctx.send(result)

#   BOTH METHODS WORK

    # calc command
    @commands.command(aliases=['calculate'])
    async def calc(self, ctx, num1:int, operation, num2:int):
        
        symbols = ['+','-','*','/']
        if operation not in symbols:
            await ctx.send('Please pick from a valid operation type.\n\n**Available operations:** `+`, `-`, `*`, `/`')

        # operational thingies
        if operation == '+':
            add = num1 + num2
            await ctx.send(add)

        elif operation == '-':
            sub = num1 - num2
            await ctx.send(sub)
        
        elif operation == '*':
            multiply = num1 * num2
            await ctx.send(multiply)

        elif operation =='/':
            divide = num1 / num2
            await ctx.send(divide)


  


def setup(client):
  client.add_cog(Math(client))

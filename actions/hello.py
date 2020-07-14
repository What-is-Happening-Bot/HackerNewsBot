from discord.ext import commands

class Hello(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  # Simple test command to help us get used to commands in the module.
  @commands.command()
  async def hello(self, ctx):
    print('!hello command was called')
    await ctx.send('Hello! ヾ(•ω•`)o')
  

  # This command is to help us get used to taking in arguments from the user.
  # Could potentially be used to get their preferences.
  @commands.command()
  async def echo(self, ctx, *args):
    print('!echo command was called')
    await ctx.send(' '.join(args))

def setup(bot):
  bot.add_cog(Hello(bot))
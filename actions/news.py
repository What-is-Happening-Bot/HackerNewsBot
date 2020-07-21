import aiohttp
from discord.ext import commands
from hackernews.news_type import getType
from hackernews.firstthree import getFirstThree
import discord

class HackerNews(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context = True)
  async def news(self, ctx, *args):
    if len(args)!=2:
      await ctx.send("Please input both item type and topic")
    elif args[0].lower() not in ['jobstories', 'newstories', 'topstories', 'beststories', 'showstories']:
      await ctx.send("Please input a supported item type")
    else: 
      async with ctx.channel.typing():
        BASE_URL = 'https://hacker-news.firebaseio.com/v0/'
        await ctx.send("Here you go...")
        getTypeInstance = getType()
        typeIds = await getTypeInstance.get_stories(args[0].lower(), BASE_URL)
        getFirstThreeInstance = getFirstThree()
        await getFirstThreeInstance.firstThree(ctx, typeIds, BASE_URL)
        
    
def setup(bot):
  bot.add_cog(HackerNews(bot))
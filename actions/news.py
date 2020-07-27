import aiohttp
from discord.ext import commands
from hackernews.news_type import getType
from hackernews.firstthree import getFirstThree
import discord
from hackernews.dictionary import similarTerms

# This file holds the code for bot commands.
# The bot currently supports the following commands: 
# [!help news] [!storytypes] [!topics]

class HackerNews(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context = True, 
  brief= 'Type in \'!help news\' to learn how to use the command',
  usage= '[jobstories, newstories, topstories, beststories, showstories] [your_topic]')
  async def news(self, ctx, *args):
    news_arg = args[0].lower()
    topic_arg = args[1].lower()
    if len(args)!=2:
      await ctx.send("Please input both item type and topic")
    elif news_arg not in ['jobstories', 'newstories', 'topstories', 'beststories', 'showstories']:
      await ctx.send("Please input a supported item type... Try !help or !storytypes")
    elif topic_arg not in similarTerms:
      await ctx.send("Topic is currently not supported... Try !help or !topics")
    else: 
      async with ctx.channel.typing():
        BASE_URL = 'https://hacker-news.firebaseio.com/v0/'
        await ctx.send("Here you go...")
        getTypeInstance = getType()
        typeIds = await getTypeInstance.get_stories(news_arg, BASE_URL)
        getFirstThreeInstance = getFirstThree()
        await getFirstThreeInstance.firstThree(ctx, typeIds, BASE_URL, news_arg, topic_arg)
    
  @commands.command(
    brief= 'Displays the available story types'
  )
  async def storytypes(self, ctx):
    await ctx.send("```jobstories, newstories, topstories, beststories, showstories```")

  @commands.command(
    brief= 'Displays the available search topics'
  )
  async def topics(self, ctx):
    finalTopics = ', '.join(similarTerms)
    await ctx.send("```"+finalTopics+"```")

def setup(bot):
  bot.add_cog(HackerNews(bot))
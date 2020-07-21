import aiohttp
from discord.ext import commands
import discord

class HackerNews(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def news(self, ctx):
    BASE_URL = 'https://hacker-news.firebaseio.com/v0/'
    TOP_STORIES = 'topstories'
    ITEM = 'item'
    ITEM_ID = []

    async with ctx.channel.typing():
      # async with aiohttp.ClientSession() as session:
      #   async with session.get(
      #     BASE_URL + TOP_STORIES + '.json?print=pretty') as top_ids:

      #     data = await top_ids.json()

      #     count = 0
      #     while count < 100:
      #       ITEM_ID.append(data[count])
      #       count += 1

          # print(ITEM_ID)

          curr_res = 0
          limit = 3

          for id in ITEM_ID:
            async with session.get(
              BASE_URL + ITEM + '/' + str(id) + '.json?print=pretty') as curr_id:

              curr_data = await curr_id.json()

              embed = discord.Embed(colour=discord.Colour.dark_green())

              if (curr_data.get('url')) and (curr_res < limit):
                curr_res += 1

                embed.add_field(name=curr_data.get('title'), value=curr_data.get('url'), inline=False)
                embed.set_author(name=curr_data.get('by'))

                await ctx.send(embed=embed)
                

          
def setup(bot):
  bot.add_cog(HackerNews(bot))
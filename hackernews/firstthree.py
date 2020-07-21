import aiohttp
import discord

class getFirstThree():
  async def firstThree(self, ctx, idList, BASE_URL):
    curr_res = 0
    limit = 3

    async with aiohttp.ClientSession() as session:
      embed = discord.Embed(colour=discord.Colour.dark_green())
      embed.set_author(name=str(ctx.message.author))

      for id in idList:
        async with session.get(
          BASE_URL + 'item/' + str(id) + '.json?print=pretty') as curr_id:

          curr_data = await curr_id.json()

          if (curr_data.get('url')) and (curr_res < limit):
            curr_res += 1
            embed.add_field(name=curr_data.get('title'), value=curr_data.get('url', 'no url'), inline=False)
            
      await ctx.send(embed=embed)
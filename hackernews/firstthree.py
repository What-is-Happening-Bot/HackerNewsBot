import aiohttp
import discord


# Accesses the item, which is possible since the ID of the item is passed in
# Returns an embed that displays the caller's name and three news articles that
# pertains to the user's preference.

class getFirstThree():
  async def firstThree(self, ctx, idList, BASE_URL, type, topic):
    curr_res = 0
    limit = 3

    async with aiohttp.ClientSession() as session:
      embed = self.colorPicker(type)
      embed.set_author(name=type + ' about ' + topic + ' for ' + str(ctx.message.author)) # X about Y for author

      for id in idList:
        async with session.get(
          BASE_URL + 'item/' + str(id) + '.json?print=pretty') as curr_id:

          curr_data = await curr_id.json()

          if (curr_data.get('url')) and (curr_res < limit):
            curr_res += 1
            embed.add_field(name=curr_data.get('title'), value=curr_data.get('url', 'no url'), inline=False)
            
      await ctx.send(embed=embed)

  # jobstories, newstories, topstories, beststories, showstories
  def colorPicker(self, type):
    if type == 'jobstories':
      return discord.Embed(colour=0x1F8B4C) # dark green
    elif type == 'newstories':
      return discord.Embed(colour=0xFD0061) # luminous vivid pink
    elif type == 'topstories':
      return discord.Embed(colour=0x1ABC9C) # aqua
    elif type == 'beststories':
      return discord.Embed(colour=0xF1C40F) # gold
    elif type == 'showstories':
      return discord.Embed(colour=0x34495E) # navy


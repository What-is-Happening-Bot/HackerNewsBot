import aiohttp
import discord
import re

# Accesses the item, which is possible since the ID of the item is passed in
# Returns a color-coded embed that displays the caller's name and up to three stories that
# pertains to the user's preference.

class getFirstThree():
  async def firstThree(self, ctx, idList, BASE_URL, type, topic):
    curr_res = 0
    limit = 3

    async with aiohttp.ClientSession() as session:
      embed = self.colorPicker(type)
      embed.set_author(name=type + ' about ' + topic + ' for ' + str(ctx.message.author))

      for id in idList:

        async with session.get(
          BASE_URL + 'item/' + str(id) + '.json?print=pretty') as curr_id:

          curr_data = await curr_id.json()

          if not curr_data: 
            continue

          curr_title = re.search('\\b'+topic+'\\b', curr_data.get('title').lower())

          if (curr_res < limit) and curr_title:
            curr_res += 1
            embed.add_field(name=curr_data.get('title'), value=curr_data.get('url', 'no url'), inline=False)
            
      if not embed.fields:
        embed.add_field(name='No Results!', value='We were unable to find any matching stories...')

      await ctx.send(embed=embed)

  def colorPicker(self, type):
    if type == 'job':
      return discord.Embed(colour=0x1F8B4C) # dark green
    elif type == 'new':
      return discord.Embed(colour=0xFD0061) # luminous vivid pink
    elif type == 'top':
      return discord.Embed(colour=0x1ABC9C) # aqua
    elif type == 'best':
      return discord.Embed(colour=0xF1C40F) # gold
    elif type == 'show':
      return discord.Embed(colour=0x34495E) # navy
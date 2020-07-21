import aiohttp

# Returns the top 100 IDs for the following types:
# [Jobs,
#  Stories (New, Top, Best),
#  Ask]

class getType:
    BASE_URL = 'https://hacker-news.firebaseio.com/v0/'
    JOBS = 'jobstories'
    NEW_STORIES = 'newstories'
    TOP_STORIES = 'topstories'
    BEST_STORIES = 'beststories'
    ASK = 'askstories'
    
    ITEM = 'item'
    ITEM_ID = []

    async def get_top_stories(self):
      async with aiohttp.ClientSession() as session:
        async with session.get(
          self.BASE_URL + self.TOP_STORIES + '.json?print=pretty') as top_ids:

          data = await top_ids.json()

          count = 0
          while count < 100:
            self.ITEM_ID.append(data[count])
            count += 1

      return self.ITEM_ID
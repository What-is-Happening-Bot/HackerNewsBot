# Hackernews Hawker Bot

**Created by:** [Phil Kim](https://github.com/socolorphil), [Ricardo Rodriguez](https://github.com/RicardoR22), [Xiangmin Mo](https://github.com/mxmsunny)

Collaborating to build a Discord bot that makes news recommendations from HackerNews **(working description)**  
We are using [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) and the [HackerNews API](https://github.com/HackerNews/API) to achieve this goal.
Because of this:

### Please have [Python 3.5.3 or higher](https://www.python.org/downloads/) installed on your machine  
  
*You can also use [nodemon](https://nodemon.io/) for development, which requires [node.js](https://nodejs.org/en/).  
Please follow the installation instructions on their respective websites.*

## Installation
**1. Download discord.py**  

  * You can get the library directly from PyPI:
```
  python3 -m pip install -U discord.py
```
  * If you are using Windows, then the following should be used instead:
```
  py -3 -m pip install -U discord.py
```  

**2. Download python-dotenv**
```
  pip install -U python-dotenv
```

**3. Create a .env file (named ".env") and include your bot token**

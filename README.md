# Hackernews Hawker Bot

**Created by:** [Phil Kim](https://github.com/socolorphil), [Ricardo Rodriguez](https://github.com/RicardoR22), [Xiangmin Mo](https://github.com/mxmsunny)

This program allows a Discord bot to communicate with the Hacker News API. Users have the ability to send commands with specification parameters to narrow search results.

We are using [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) and the [HackerNews API](https://github.com/HackerNews/API) to achieve this goal.
Because of this:

### Please have [Python 3.5.3 or higher](https://www.python.org/downloads/) installed on your machine

_You can also use [nodemon](https://nodemon.io/) for development, which requires [node.js](https://nodejs.org/en/).  
Please follow the installation instructions on their respective websites._

## Installation

**1. Download discord.py**

- You can get the library directly from PyPI:

```
  python3 -m pip install -U discord.py
```

- If you are using Windows, then the following should be used instead:

```
  py -3 -m pip install -U discord.py
```

**2. Download python-dotenv**

```
  pip install -U python-dotenv
```

**3. Create a .env file (named ".env") and include your bot token**

## Commands

**1. !help news**

- Assists users use the !news command

```
  !help news
```

**2. !storytypes**

- Displays the available story types from Hacker News API

```
  !storytypes
```

**3. !topics**

- Displays currently available search keywords

```
  !topics
```

## Screenshots

**1. Bot running on Discord**
![](/screenshots/bot.png)

**2. Running a storytype + topics search**
![](/screenshots/command.png)

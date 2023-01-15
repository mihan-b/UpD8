# UpD8

Upd8 is a discord bot that keeps you updated on the latest news and information. You can set up the bot with your preferences such as your name, location, NBA team, and stocks to follow. You can also use it to check for the current stock prices, weather, and sports scores by simply sending a command. It also sends you a daily update of your preferences. Upd8 uses OpenAI's DaVinci 3 to output responses in a natural language with randomized tones. Upd8 keeps you informed and saves you time in finding the latest updates on the things that matter to you.

<img width="870" alt="Screen Shot 2023-01-15 at 3 19 01 PM" src="https://user-images.githubusercontent.com/97782125/212564858-88033382-f027-4efb-a758-9c2b3b89dae8.png">

## Built With
- [Python](https://www.python.org/)
- [Discord API](https://discord.com/developers/docs/intro)
- [OpenAI API](https://openai.com/api/)
- [Figma](https://www.figma.com/)

## Commands
- `setup` - setup user info
- `upd8` - receive daily update
- `stock`, `sports`, `weather` - receive on-demand info

## Discord
We use Discord's API to pull the user's ID and match/create a JSON file that stores their info, we also read and write messages with our bot in Discord. This is managed in `main.py`

## Davinci 3
We use OpenAI's Davinci 3 to turn our data responses into natural-sounding text that varies in tone and sounds like it came from a person. This also means that responses will not always be the same. This is managed in `ai.py`

## APIs
We created our own APIs in the `get.py` file by web scraping. Web scraping is tedious and can sometimes be unreliable but we made sure that we correctly scrape our data. 

## Replit
We used Replit to run our code and collaborate.

## Unexpected Challenges
The biggest challenge we faced was trying to get APIs to work properly. This is why we ended up using web scraping to create our own. 

## What's Next
Adding features like other sports leagues, news, personal calendar reminders and more

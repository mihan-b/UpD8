import os
import discord
import json
import requests
import schedule
import time
from discord.ext import commands
from get import get_stock
from get import get_weather
from get import get_score

TOKEN = os.environ['token']
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
  print('bot ready')

@client.event
async def on_message(message):
  print(message.author, message.content, message.channel.id)
  user_id = message.author.id
  # Filename
  filename = str(user_id) + ".json"
  # Testing if bot is responsive
  if message.content == "ping":
    await message.channel.send("pong")
  # Setup user info
  if message.content == "setup" or message.content == "Setup":
    # Continue with the setup process
    await message.channel.send("What is your name?")
    name = await client.wait_for('message')
    await message.channel.send("Where are you located?")
    location = await client.wait_for('message')
    await message.channel.send("What NBA team would you like to follow?")
    team = await client.wait_for('message')
    await message.channel.send("What 3 stocks would you like to follow?")
    stock1 = await client.wait_for('message')
    await message.channel.send(f"Followed {stock1.content}")
    stock2 = await client.wait_for('message')
    await message.channel.send(f"Followed {stock2.content}")
    stock3 = await client.wait_for('message')
    await message.channel.send(f"Followed {stock3.content}")

    # Info for json
    user_data = {
      "discord_id": user_id,
      "name": name.content,
      "location": location.content,
      "sports": team.content,
      "tag1": stock1.content,
      "tag2": stock2.content,
      "tag3": stock3.content,
    }

    # Append to json
    with open(filename, "w") as outfile:
      json.dump(user_data, outfile)

    # Confirmation message
    await message.channel.send(
      f"Thank you, {name.content}! Your information has been saved.")

  if message.content == "stock" or message.content == "Stock":
    await message.channel.send("Enter the stock tag")
    tag = await client.wait_for('message')
    price = get_stock(tag.content)
    await message.channel.send(price)

  if message.content == "weather" or message.content == "Weather":
    await message.channel.send("Enter the city")
    city = await client.wait_for('message')
    temp = get_weather(city.content)
    await message.channel.send(temp)

  if message.content == "sports" or message.content == "Sports":
    await message.channel.send("Enter the leauge")
    leauge = await client.wait_for('message')
    await message.channel.send("Enter the team")
    team = await client.wait_for('message')
    text = get_score(leauge.content, team.content)
    await message.channel.send(text)

  if message.content == "upd8" or message.content == "Upd8" or message.content == "UpD8":
    with open(filename, "r") as json_file:
      # Load the contents of the file into a Python object
      data = json.load(json_file)
    await message.channel.send("Here is your daily UpD8!")
    stock1 = get_stock(data["tag1"])
    stock2 = get_stock(data["tag2"])
    stock3 = get_stock(data["tag3"])
    score = get_score("NBA", data["sports"])
    weather = get_weather(data["location"])
    text = weather + "\n" +  stock1 + "\n" + stock2 + "\n" + stock3 + "\n" + score
    await message.channel.send(text)
   
    
@client.command()
async def hello(ctx):
  channel = client.get_channel(1033759192596619386)
  await channel.send(f'hello there {ctx.author.mention}')

client.run(TOKEN) 
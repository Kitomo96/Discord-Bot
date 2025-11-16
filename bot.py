import dotenv
import discord
import os
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

dotenv.load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print (f'Logged on as {self.user}')
    async def on_message(self, message):
        if message.author != self.user and message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        else:
            return 
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN) # Replace with your own token.
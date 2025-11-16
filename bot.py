import dotenv
import discord
import os
import requests
import json
from google import genai

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

dotenv.load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY') 

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

def gemini_response(prompt):
    response = gemini_client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = prompt,
)
    return response.text
    

class MyClient(discord.Client):
    async def on_ready(self):
        print (f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
            
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
            return

        if self.user.mentioned_in(message):
            prompt = message.content.replace(f'<@!{self.user.id}>', '').replace(f'<@{self.user.id}>', '').strip()

            async with message.channel.typing():
                try:
                    await message.reply(gemini_response(message.content))
                except Exception as e:
                    print(f"Error generating response: {e}")
                    await message.reply("Sorry, I ran into an error trying to respond.")
            return
        
        else:
            return 
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
import discord
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


llm = ChatOpenAI(temperature=0.7)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        try:
            #await message.channel.send(message.content)
            msg = [HumanMessage(content = message.content)]
            result = llm(msg)
            await message.channel.send(result.content)
        except Exception as e:
            print(f"Error occurred: {e}")
            await message.channel.send("Sorry, I was unable to process your question.")

client.run(os.environ.get('DISCORD_TOKEN'))
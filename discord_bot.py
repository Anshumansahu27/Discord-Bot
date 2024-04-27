
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

chat = ChatOpenAI(temperature=0)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def question(ctx, *, question):
    try:

        messages = [HumanMessage(content=question)]
        result = chat(messages)
        await ctx.send(result.content)
    except Exception as e:
        print(f"Error occurred: {e}")
        await ctx.send("Sorry, I was unable to process your question.")


bot.run(os.environ.get("DISCORD_TOKEN"))
# src/bot/main.py
import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}!")

# TODO: Register your slash commands here

if __name__ == "__main__":
    bot.run(TOKEN)

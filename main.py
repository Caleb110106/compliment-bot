import os
import discord
import random
import time
from keep_alive import keep_alive

keep_alive()

# Securely get the token and user ID from environment variables
TOKEN = os.getenv("TOKEN")
SECRET_USER_ID = int(os.getenv("SECRET_USER_ID"))

compliments = [
    "You're amazing!",
    "God loves you!",
    "You're beautiful.",
    "You're talented.",
    "You make a difference.",
    "There is someone out there that loves you.",
]

secret_message = (
    "I love you, señora! 💖 Keep being the beautiful and amazing woman that you are. "
    "I'm very happy and lucky to have such an incredible woman and friend in my life."
)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
         msg = message.content.lower()

    if msg.startswith("!compliment"):
        parts = message.content.split()

        # Check if someone was mentioned
        if len(parts) > 1 and message.mentions:
            mentioned_user = message.mentions[0]
            compliment = random.choice(compliments)
            await message.channel.send(f"{mentioned_user.mention}, {compliment} (from {message.author.mention})")
        else:
            compliment = random.choice(compliments)
            await message.channel.send(f"{message.author.mention}, {compliment}")

    elif message.author.id == SECRET_USER_ID and msg == "!secret":
        try:
            await message.author.send(secret_message)
        except discord.Forbidden:
            await message.channel.send(
                f"{message.author.mention}, I tried to DM you but couldn’t!"
            )

# Auto-restart loop
while True:
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"⚠️ Bot crashed! Restarting in 5 seconds...\nError: {e}")
        time.sleep(5)


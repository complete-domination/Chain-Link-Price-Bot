# ping.py
import os, discord, logging
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise SystemExit("Missing TOKEN")

intents = discord.Intents.none()  # minimal
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"READY: {client.user} in {len(client.guilds)} guild(s)")
    await client.change_presence(activity=discord.Game(name="online ✅"))

client.run(TOKEN)

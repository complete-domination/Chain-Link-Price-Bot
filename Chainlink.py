import os, logging, discord
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise SystemExit("Missing TOKEN")

client = discord.Client(intents=discord.Intents.none())

@client.event
async def on_ready():
    print(f"READY: {client.user} in {len(client.guilds)} guild(s)")
    try:
        await client.change_presence(activity=discord.Game(name="online ✅"))
    except Exception as e:
        print(f"Presence set failed: {e}")

client.run(TOKEN)

from telethon import TelegramClient
import asyncio

api_id = 20834477
api_hash = "08fe734379555d72c42399e1ba89ca68"

client = TelegramClient("session", api_id, api_hash)

async def main():
    print("Bot ishladi")
    await client.start()
    me = await client.get_me()
    print(me.first_name)

with client:
    client.loop.run_until_complete(main())

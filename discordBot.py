import asyncio
import discord
import importlib
import os
import socket
from dotenv import load_dotenv
import Constants.constantsDiscord as constants

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
DEBUG_CHANNEL_ID = int(os.getenv("DEBUG_CHANNEL_ID"))

HOST = "127.0.0.1"
PORT = 12345

class MyClient(discord.Client):
    async def setup_hook(self):
        self.bg_task = asyncio.create_task(self.listenForMessages())

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def listenForMessages(self):
        await self.wait_until_ready()
        
        channel = self.get_channel(CHANNEL_ID)
        debugChannel = self.get_channel(DEBUG_CHANNEL_ID)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        server.setblocking(False)
        
        print(f"Listening for messages on {HOST}:{PORT}")
        loop = asyncio.get_running_loop()
        
        while True:
            try:
                client_sock, _ = await loop.sock_accept(server)
                data = await loop.sock_recv(client_sock, 1024)
                msg = data.decode("utf-8").strip()
                if msg:
                    importlib.reload(constants)
                    await debugChannel.send(msg)

                    for item in constants.itemsWorthNotifying:
                        if item in msg:
                            await channel.send(f"<@523671068452585508> **{constants.itemsWorthNotifying[item]}** is in stock hei gui")
                            print(f"Sent notification for {item}")

                client_sock.close()
            
            except Exception as e:
                print(f"Socket error: {e}")
            
            await asyncio.sleep(0.1)

client = MyClient(intents=discord.Intents.default())

async def main():
    await client.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
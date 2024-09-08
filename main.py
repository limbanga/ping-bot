import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

print(TOKEN)
# Khởi tạo client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Sự kiện khi bot sẵn sàng
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Sự kiện khi bot nhận tin nhắn
@client.event
async def on_message(message):
    print("message")
    print(message.content)
    print(message.author)

    # Không phản hồi tin nhắn của bot
    if message.author == client.user:
        return

    # Lệnh kiểm tra ping
    print(message)
    if message.content == '!ping':
        await message.channel.send('Pong!')

# Đăng nhập bot
client.run(TOKEN)


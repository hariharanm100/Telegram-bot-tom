from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
# Replace with your actual API credentials
api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'
users_to_add = ["akilthangavel100"]
user_id_add = 6330745427
group_entity = -1001917437122
user_id = "1213145088"
# 4022079554
# Create a Telethon client instance with the API credentials
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# Define command handlers as shown in the previous example...
# Define a command handler using the events.NewMessage pattern
@client.on(events.NewMessage(pattern='/start'))  # Change the command as needed
async def start_command(event):
    # This function will be called when the /start command is received
    my_user  = await client.get_entity(PeerUser(6330745427))
    print(my_user)
    my_channel = await client.get_entity(PeerChannel(-1001917437122))
    print(my_channel)
    # await client(InviteToChannelRequest(-1001917437122, [6330745427]))
    # await client(AddChatUserRequest(-1001917437122, 6558470586, fwd_limit=10 ))
    await event.respond('Hello! Welcome to the bot.')

    
# Run the client
client.run_until_disconnected()

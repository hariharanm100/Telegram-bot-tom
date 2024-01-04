from telethon import TelegramClient, events

api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

# 4022079554
# Create a Telethon client instance with the API credentials
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# Define command handlers as shown in the previous example...
# Define a command handler using the events.NewMessage pattern
@client.on(events.NewMessage(pattern='/start'))  # Change the command as needed
async def start_command(event):
    # This function will be called when the /start command is received
    await event.respond('Hello! Welcome to the bot.')

    
# Run the client
client.run_until_disconnected()
chat_id = "mychatid"
users = ['UserName']

response = client.invoke(ResolveUsernameRequest(chat_id))

target_group_entity = InputPeerChannel(response.chats[0].id, response.chats[0].access_hash)

try:
    res = client(InviteToChannelRequest(channel=target_group_entity, users=users ))
except Exception as e:
    print("spam protection: " + e.message + ": " + str(e))
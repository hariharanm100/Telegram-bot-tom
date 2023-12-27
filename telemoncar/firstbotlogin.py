from telethon import TelegramClient, events

# Replace with your actual API credentials
api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'


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

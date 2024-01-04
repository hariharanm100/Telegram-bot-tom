from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest

api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'


client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start')) 
async def start_command(event):
    updates = await client(ImportChatInviteRequest('+nPmonJDl21w4YTk9'))
    print(updates)
    await event.respond('Hello! Welcome to the bot.')

    
# Run the client
client.run_until_disconnected()

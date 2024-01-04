from telethon.sync import TelegramClient
from telethon import functions, types

api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
with TelegramClient("akilthangavel1", api_id, api_hash) as client:
    result = client(functions.messages.AddChatUserRequest(
        chat_id=-12398745604826,
        user_id='username',
        fwd_limit=42
    ))
    print(result.stringify())
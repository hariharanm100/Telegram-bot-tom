from telethon import TelegramClient, sync
client = TelegramClient(SESSION_FILE_NAME, API_ID, 'API_HASH')
client.start()

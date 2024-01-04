from telethon.sync import TelegramClient, events

# Bot credentials
bot_api_id = 27824897
bot_api_hash = "c7360424c507d2fb40196bbd6cd5c648"
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

# User credentials
user_api_id = 27824897
user_api_hash = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaekt'

async def main():
    # Create bot client
    bot_client = TelegramClient('bot_session', bot_api_id, bot_api_hash).start(bot_token=bot_token)

    # Create user client
    user_client = TelegramClient('user_session', user_api_id, user_api_hash)
    await user_client.start()

    @bot_client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('Hello! This is the bot.')

    @user_client.on(events.NewMessage)
    async def echo(event):
        if not event.message.out:
            await event.respond(event.text)

    print("Bot is running!")
    await bot_client.run_until_disconnected()

if __name__ == "__main__":
    with bot_client, user_client:
        bot_client.loop.run_until_complete(main())

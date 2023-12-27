from telethon.sync import TelegramClient, events
from telethon.tl.types import InputPeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest

# Bot credentials
bot_api_id = 27824897
bot_api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'


# User credentials
user_api_id = 27824897
user_api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
phone = '+918489798100'
user_client = TelegramClient(phone, user_api_id, user_api_hash)
user_client.connect()
if not user_client.is_user_authorized():
    user_client.send_code_request(phone)
    user_client.sign_in(phone, input('Enter the code: '))
async def main():
    
    # Create bot client
    bot_client = TelegramClient('bot_session', bot_api_id, bot_api_hash)
    await bot_client.start(bot_token=bot_token)

    @bot_client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('Hello! This is the bot.')

    # @bot_client.on(events.NewMessage(pattern='/sart1'))
    # async def start1(event):
    #     targetGroupId = 2096266635 
    #     targetGroupAccessHash = -198665311552621838
    #     target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
    #     # user_to_add = InputPeerUser(user['id'], user['access_hash'])
    #     user_to_add =await user_client.get_input_entity('akilthangavel100')
    #     print(user_to_add)
    #     print(target_group_entity)
    #     print("##################################")
    #     await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    #     await event.respond('User added')

    print("Bot is running!")
    await bot_client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest

# Your API credentials from https://my.telegram.org
api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

group_id = -1001917437122
# Your phone number associated with your Telegram account
phone_number = '+918489798100'

# ID of your private group
# group_id = YOUR_GROUP_ID

# ID of the user you want to add
# user_id_to_add = USER_ID_TO_ADD

async def add_user_to_group():
    async with TelegramClient(phone_number, api_id, api_hash) as client:
        # Ensure you're logged in
        await client.start()

        # Add the user to the group
        try:
            # return await client.get_entity(6558470586)
            print("######################################")
            # await client.get_messages("tesaddmem")
            # await client(AddChatUserRequest(-1001917437122, 6558470586, fwd_limit= 10))

            print("User added to the group successfully!")
        except Exception as e:
            print(f"Error: {e}")

# Run the script
if __name__ == "__main__":
    import asyncio
    asyncio.run(add_user_to_group())

import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def add_members_to_group(chat_id, members):
    for member_id in members:
        try:
            await bot.add_chat_members(chat_id=chat_id, user_ids=member_id)
            print(f"Added user with ID {member_id} to the group!")
        except Exception as e:
            print(f"Failed to add user with ID {member_id}: {e}")

async def start_adding_members():
    # Replace this with your actual group ID
    group_chat_id = 123456789  # Replace with your group chat ID
    # Replace these IDs with the user IDs you want to add to the group
    members_to_add = [987654321, 111111111]

    await add_members_to_group(group_chat_id, members_to_add)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.get_me())
    loop.run_until_complete(start_adding_members())

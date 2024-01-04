API_TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'
group_chat_id = -1001917437122 
#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

# import logging
# from telegram import LabeledPrice, Bot
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# # set higher logging level for httpx to avoid all GET and POST requests being logged
# logging.getLogger("httpx").setLevel(logging.WARNING)

# logger = logging.getLogger(__name__)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     chat_id = "-1004022205092"

#     # chat_id = update.message.chat_id
#     await context.bot.send_message(chat_id=chat_id, text=f"Your Chat ID is: {chat_id}")


# def main() -> None:
#     """Run the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token(API_TOKEN).build()

#     application.add_handler(CommandHandler("start", start))

#     # Run the bot until the user presses Ctrl-C
#     application.run_polling(allowed_updates=Update.ALL_TYPES)


# if __name__ == "__main__":
#     main()




################################################# 



# from telegram import Bot

# # Bot token received from BotFather
# bot_token = API_TOKEN

# # Group ID where you want to add members
# group_id = '-1001917437122'

# # Initialize the bot
# bot = Bot(token=bot_token)

# # Function to add member to the group
# def add_member_to_group(member_id):
#     bot.add_chat_member(chat_id=group_id, user_id=member_id)

# # Example: Adding a member (replace '123456789' with the actual user ID)
# user_id_to_add = 123456789
# add_member_to_group(user_id_to_add)


##########################################################################################


# import requests

# bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'
# group_id = -1001917437122
# user_id = 6330745427

# add_member_url = f'https://api.telegram.org/bot{bot_token}/addChatMember?chat_id={group_id}&user_id={user_id}'

# response = requests.get(add_member_url)
# print(response)
# print(response.json())


#########################################################################################################################

from telegram import Bot
import asyncio
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = Bot(token='6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA')

# Replace 'GROUP_CHAT_ID' with your group's chat ID
group_chat_id = -1004022205092  # Example ID, replace this with your group's chat ID


async def get_invite_link():
    invite_link = await bot.export_chat_invite_link(chat_id=group_chat_id)
    return invite_link

async def main():
    invite_link = await get_invite_link()
    print("Invite Link:", invite_link)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
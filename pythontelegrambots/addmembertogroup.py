# from telegram import Bot, ChatAction
# bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'
# group_id = -1004022205092  # Replace with your group ID

# # List of user IDs to be added to the group
# users_to_add = [6330745427, 987654321]  # Replace with user IDs

# # Initialize the bot
# bot = Bot(token=bot_token)

# # Add users to the group
# for user_id in users_to_add:
#     try:
#         #bot.add_chat_members(chat_id=group_id, user_id=user_id)
#         # bot.promote_chat_member(chat_id=group_id, user_id=user_id, can_change_info=False)
#         # print(f"User {user_id} added to the group successfully!")
#         bot.send_chat_action(chat_id=group_id, action=ChatAction.TYPING)
#         bot.chat_member(chat_id=group_id, user_id=user_id, action='add')
#         print(f"User {user_id} added to the group successfully!")
#     except Exception as e:
#         print(f"Failed to add user {user_id}: {e}")




#########################################



# import telethon 
# def get_users(): 
#    # Get a list of user IDs or usernames. 
#     return ["123456789", "username"] 
# def add_member(user): 
#     # Get the Telegram client. 
#     client = telethon.TelegramClient(None, api_id, api_hash) 
#     # Get the group ID. 
#     group_id = "-123456789" 
#     # Add the user to the group. 
#     client.get_entity(group_id).add_user(user) 
# if __name__ == "__main__": 
#     # Get the list of users. 
#     users = get_users() 
#     # Add the users to the group. 
#     for user in users: 
#         add_member(user) 


############################################################


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram Bot Token
TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

# Function to handle the /add command
def add_members(update: Update, context: CallbackContext):
    # Get the chat ID of the group
    chat_id = update.message.chat_id
    
    # List of users to add to the group
    users_to_add = ['username1', 'username2', 'username3']  # Add usernames here
    
    for user in users_to_add:
        try:
            # Add users to the group
            context.bot.add_chat_members(chat_id=chat_id, user_ids=user)
        except Exception as e:
            print(f"Failed to add user {user}: {e}")

# Set up the bot and dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handler for the /add command
dispatcher.add_handler(CommandHandler("add", add_members))


def main() -> None:
    application = Application.builder().token(API_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(football_subscription, pattern="Football"))
    application.add_handler(CallbackQueryHandler(basketball_subscription, pattern="Basketball"))
    application.add_handler(CallbackQueryHandler(nba_props_subscription, pattern="NBA Props"))
    application.add_handler(CallbackQueryHandler(all_in_one_subscription, pattern="ALL IN ONE"))
    application.add_handler(CallbackQueryHandler(pay_callback, pattern="1"))
    application.add_handler(CommandHandler("help", help_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

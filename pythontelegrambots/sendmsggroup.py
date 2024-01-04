from telegram import Bot

# Your bot token
TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

# Your group chat ID
group_chat_id = -100123456789  # Replace with your actual group chat ID


bot = Bot(TOKEN)
bot.send_message(chat_id=group_chat_id, text="message")


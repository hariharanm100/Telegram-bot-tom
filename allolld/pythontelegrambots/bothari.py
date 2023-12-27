API_TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'
#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import LabeledPrice, Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = "-1004022205092"

    group_chat_id = -1001917437122  # Replace with your actual group chat ID


    bot = Bot(API_TOKEN)
    await bot.send_message(chat_id=group_chat_id, text="message")
    await bot.export_chat_invite_link(chat_id=group_chat_id)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Get the list of user IDs to add to the group
    user_ids = [123456789, 987654321]  # Replace these with the actual user IDs

    # Get the chat ID of the group where you want to add users
    chat_id = update.message.chat_id
    # print("##################################")
    for user_id in user_ids:
        try:
            # Add the user to the group
            context.bot.add_chat_members(chat_id, user_id)
            # Send a message indicating the user has been added
            context.bot.send_message(chat_id, f"User {user_id} has been added to the group.")
        except Exception as e:
            print(f"Error adding user {user_id}: {e}")
    # query = update.callback_query

    # # CallbackQueries need to be answered, even if no notification to the user is needed
    # # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    # # Send the first message asking the user to accept terms of service
    # message_1 = "terms of service."
    # await context.bot.send_message(chat_id=query.message.chat_id, text=message_1)

    # if query.data == "Football (€29,99)":
    #     import uuid

    #     # Generating a unique ID
    #     unique_transaction_id = str(uuid.uuid4())
    #     message_1 = "Football (€29,99)"
    #     await context.bot.send_message(chat_id=query.message.chat_id, text=message_1)
    #     await context.bot.send_invoice(
    #     chat_id=query.message.chat_id,
    #     title="test p1",
    #     description="Description of the service",
    #     payload=test,
    #     provider_token="sk_test_51OPcsbSBmq5mkuubu7FGoHEUcWnxx8AjFbdO5HEI2GIwgXYN6Nf0hRjprbGCPxy6GKsEoaKXPIwJhGYFtqvfuYn600q5CTWPzn",  # Your payment provider's token
    #     start_parameter="start_parameter",
    #     currency="EUR",
    #     prices=[LabeledPrice(label="Service", amount=2999)],  # Prices in smallest units of the currency (e.g., cents)
    #     need_name=True,
    #     need_phone_number=True,
    #     need_email=True,
    #     need_shipping_address=True,
    #     is_flexible=False,
    # )

    # await query.edit_message_text(text=f"Selected option: {query.data}")

 


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
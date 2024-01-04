import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, LabeledPrice
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


API_TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    welcome_message = (
        f"Welcome, {user.first_name}! \U0001F44B\n\n"  # Waving hand emoji
        "We are currently running 3 services:\n\n"
        "\U000026BD️ Football (10.75% ROI after 1561 Bets)\n"
        "\U0001F3C0 Basketball (8% ROI after 1450 Bets)\n"
        "\U0001F3C6 NBA Props (10% ROI after 1020 Bets)\n\n"
        "\u25A0 Within each group you can expect 150-200 bets a month. All groups offer +EV bets, "
        "with a focus on beating the closing line resulting in long-term profitability.\n"
        "\u25A0 Each subscription lasts 30 days, and after buying your subscription will be active immediately. Subscriptions are recurring, unless you cancel."
    )
    await update.message.reply_text(welcome_message)
    keyboard = [
        [
            InlineKeyboardButton("Football (€29,99)", callback_data="Football (€29,99)"),
            InlineKeyboardButton("Basketball (€29,99)", callback_data="Basketball (€29,99)"),
        ],
        [
            InlineKeyboardButton("NBA Props (€29,99)", callback_data="NBA Props (€29,99)"),
            InlineKeyboardButton("ALL IN ONE", callback_data="ALL IN ONE"),],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

async def football_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await update.callback_query.answer("You've chosen the Football subscription!")
    logger.error(query.data, exc_info=context.error)
    footballOption = (
        "By purchasing this service, you get access to: \n"
        "\t - Toms Tips Premium Football Group \U000026BD \n"
        "\u25A0 In this group, we will be posting 1x2, Asian Handicap and Over/Under bets. Over 75% of the bets in this group will be on the ‘big’ leagues, this way even people with restricted accounts can follow our bets. \n"
        "\u25A0 Most of the bets will be posted soon after the odds are released, which could be a week or even longer before the game actually takes place because this is the moment we can extract the most value. \n"
        "\u25A0 The main focus of this group is beating the closing line. This is our key indicator for performance and will also be tracked in the spreadsheet. \n You can expect 100-150 bets per month, and we expect an average ROI% of around 10%\n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter. By purchasing this service, you agree to the Terms and Conditions \n"
        "\u2023 By purchasing this service, you get access to: \n"
    )
    await context.bot.send_message(chat_id=query.message.chat_id, text=footballOption)
    keyboard = [
        [InlineKeyboardButton("Pay", callback_data="1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    football_option = "Pay now to get access to the respected groups"
    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text=football_option,
        reply_markup=reply_markup
    )


async def basketball_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await update.callback_query.answer("You've chosen the Basketball subscription!")
    basketballOption = (
        "By purchasing this service, you get access to: \n"
        "\t - Toms Tips Premium Basketball Group \U0001F3C0 \n"
        "\u25A0 In this group, we will be posting bets on the lower leagues of Basketball (No NBA). \n"
        "\u25A0 Most bets are placed within 48 hours of the match start, sometimes even minutes before. This way the turnover will be fast, and thus you can compound your bank quickly. \n"
        "\u25A0 When available, we will be tracking the closing lines of our bets in the spreadsheet. \n This remains a key indicator for our long term success, even on lower limit leagues. You can expect 150-200 bets a month in this group, and we expect an average ROI% of 10% \n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter. \n" 
        "\u2023 By purchasing this service, you agree to the Terms and Conditions. \n"
    )
    await context.bot.send_message(chat_id=query.message.chat_id, text=basketballOption)

async def nba_props_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await update.callback_query.answer("You've chosen the NBA Props subscription!")
    nbaOption = (
        "By purchasing this service, you get access to: \n"
        "\t - Toms Tips Premium NBA Props Group \U0001F3C6 \n"
        "\u25A0 In this group we will be posting NBA Player Prop bets. \n"
        "\u25A0 Most of the bets will be placed close to tip-off (start of the match), but we also take earlier lines when available. Because of this, even people from EU that don’t want to stay up late can still enjoy a part of our bets. Because the bets are posted close to tip-off, the turnover will be fast and thus you can compound your bank quickly. \n"
        "\u25A0 When available, we will be tracking the closing lines of our bets in the spreadsheet. This remains a key indicator for our long term success. You can expect 150-200 bets a month in this group, and we expect an average ROI% of 10%. \n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter." 
        "\u2023 By purchasing this service, you agree to the Terms and Conditions \n"
    )
    await context.bot.send_message(chat_id=query.message.chat_id, text=nbaOption)

async def all_in_one_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await update.callback_query.answer("You've chosen the All-in-One subscription!")
    allOption = (
        "By purchasing this service, you get access to all three groups: \n"
        "\u2022 Toms Tips Premium Football Group \n"
        "\u2022 Toms Tips Premium NBA Props Group \n"
        "\u2022 Toms Tips Premium Basketball Group \n"
        "\u25A0 By choosing the all in one deal you get the full potential of our services and a nice discount! The football group is focused on higher limits, but bets will often be taken early. The lower league basketball group and the NBA props group have a higher volume and a quick turnover time, but lower limits. \n"
        "\u25A0This unique combination of all three services will bring your betting game to the next level. We use closing line value as a key indicator in all our services, and this will bring us long term success. \n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter. \n"
        "\u2023 By purchasing this service, you agree to the Terms and Conditions. \n"
        )
    await context.bot.send_message(chat_id=query.message.chat_id, text=allOption)

async def pay_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uery = update.callback_query
    await query.answer()
    bot_token = 'YOUR_BOT_TOKEN'
    group_id = -100123456789  # Replace with your group ID

    # List of user IDs to be added to the group
    users_to_add = [123456789, 987654321]  # Replace with user IDs

    # Initialize t123456789he bot
    bot = Bot(token=bot_token)

    # Add users to the group
    for user_id in users_to_add:
        try:
            bot.add_chat_members(chat_id=group_id, user_id=user_id)
            print(f"User {user_id} added to the group successfully!")
        except Exception as e:
            print(f"Failed to add user {user_id}: {e}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to test this bot.")


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
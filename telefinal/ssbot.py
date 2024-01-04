from telethon.sync import TelegramClient, events, Button, types, functions
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
import schedule
from datetime import datetime, timedelta, date
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Bot credentials
bot_api_id = 26689721
bot_api_hash = "41120962662844279ab6a08a0f60774f"
bot_token = '6321748774:AAFOXyERQa333nNIc3GBxcjM0s_uEL4LZi4'
provider_token = '284685063:TEST:ZDZhZjlhMjczMjdm'
bot_client = TelegramClient('bot_session', bot_api_id, bot_api_hash)


# That event is handled when customer enters his card/etc, on final pre-checkout
# If we don't `SetBotPrecheckoutResultsRequest`, money won't be charged from buyer, and nothing will happen next.
@bot_client.on(events.Raw(types.UpdateBotPrecheckoutQuery))
async def payment_pre_checkout_handler(event: types.UpdateBotPrecheckoutQuery):
    if event.payload.decode('UTF-8') == 'Football':
        # so we have to confirm payment
        await bot_client(
            functions.messages.SetBotPrecheckoutResultsRequest(
                query_id=event.query_id,
                success=True,
                error=None
            )
        )
    elif event.payload.decode('UTF-8') == 'Basketball':
        # same for another
        await bot_client(
            functions.messages.SetBotPrecheckoutResultsRequest(
                query_id=event.query_id,
                success=True,
                error=None
            )
        )
    elif event.payload.decode('UTF-8') == 'nbaOption':
        await bot_client(
            functions.messages.SetBotPrecheckoutResultsRequest(
                query_id=event.query_id,
                success=True,
                error=None
            )
        )
    elif event.payload.decode('UTF-8') == 'allOption':
        # same for another
        await bot_client(
            functions.messages.SetBotPrecheckoutResultsRequest(
                query_id=event.query_id,
                success=True,
                error=None
            )
        )
    else:
        # for example, something went wrong (whatever reason). We can tell customer about that:
        await bot(
            functions.messages.SetBotPrecheckoutResultsRequest(
                query_id=event.query_id,
                success=False,
                error='Something went wrong'
            )
        )

    raise events.StopPropagation


@bot_client.on(events.Raw(types.UpdateNewMessage))
async def payment_received_handler(event):
    if isinstance(event.message.action, types.MessageActionPaymentSentMe):
        payment: types.MessageActionPaymentSentMe = event.message.action
        # do something after payment was received
        if payment.payload.decode('UTF-8') == 'Football':
            await bot_client.send_message(
                    event.message.peer_id.user_id,
                    "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>",
                    parse_mode='html',
                    buttons=[
                        Button.inline("Accept", b'add_members_service_1'),
                        Button.inline("Decline", b'decline_service_1'),
                    ]
                )
        elif payment.payload.decode('UTF-8') == 'Basketball':
            await bot_client.send_message(
                    event.message.peer_id.user_id,
                    "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>",
                    parse_mode='html',
                    buttons=[
                        Button.inline("Accept", b'add_members_service_2'),
                        Button.inline("Decline", b'decline_service_2'),
                    ]
                )
        elif payment.payload.decode('UTF-8') == 'nbaOption':
            await bot_client.send_message(
                    event.message.peer_id.user_id,
                    "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>",
                    parse_mode='html',
                    buttons=[
                        Button.inline("Accept", b'add_members_service_3'),
                        Button.inline("Decline", b'decline_service_3'),
                    ]
                )
        elif payment.payload.decode('UTF-8') == 'allOption':
            await bot_client.send_message(
                    event.message.peer_id.user_id,
                    "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>",
                    parse_mode='html',
                    buttons=[
                        Button.inline("Accept", b'add_members_service_4'),
                        Button.inline("Decline", b'decline_service_4'),
                    ]
                )
        raise events.StopPropagation


# let's put it in one function for more easier way
def generate_invoice(price_label: str, price_amount: int, currency: str, title: str,
                     description: str, payload: str, start_param: str) -> types.InputMediaInvoice:
    price = types.LabeledPrice(label=price_label, amount=price_amount)  # label - just a text, amount=10000 means 100.00
    invoice = types.Invoice(
        currency=currency,  # currency like USD
        prices=[price],  # there could be a couple of prices.
        test=True,  # if you're working with test token, else set test=False.
        # More info at https://core.telegram.org/bots/payments

        # params for requesting specific fields
        name_requested=False,
        phone_requested=False,
        email_requested=False,
        shipping_address_requested=False,

        # if price changes depending on shipping
        flexible=False,

        # send data to provider
        phone_to_provider=False,
        email_to_provider=False
    )
    return types.InputMediaInvoice(
        title=title,
        description=description,
        invoice=invoice,
        payload=payload.encode('UTF-8'),  # payload, which will be sent to next 2 handlers
        provider=provider_token,

        provider_data=types.DataJSON('{}'),
        # data about the invoice, which will be shared with the payment provider. A detailed description of
        # required fields should be provided by the payment provider.

        start_param=start_param,
        # Unique deep-linking parameter. May also be used in UpdateBotPrecheckoutQuery
        # see: https://core.telegram.org/bots#deep-linking
        # it may be the empty string if not needed

    )


async def send_message():
    print("send message")
    #data = worksheet.get_all_records()
    # Date comparison
    # today = datetime.now()
    # if data:
    #     insertLineCount = 1
    #     for row in data:
    #         insertLineCount += 1
    #         user_date = datetime.strptime(row['subdate'], "%Y-%m-%d")  # Adjust the date format
    #         if today - user_date > timedelta(days=30):
    #             await kick_user_from_group(row["service"], row["Userid"], row['userhash'], row['Userstatus'], insertLineCount)
    # else:
    #     pass
            # Remove user from Telegram group
            # bot = Bot('YOUR_TELEGRAM_API_TOKEN')
            # chat_id = 'YOUR_TELEGRAM_CHAT_ID'
            # user_id = row['UserID']
            # bot.kick_chat_member(chat_id, user_id)

@bot_client.on(events.NewMessage(pattern='/start'))
async def start(event):
    welcome_message = (
        f"Welcome, ! \U0001F44B\n\n"  # Waving hand emoji
        "We are currently running 3 services:\n\n"
        "\U000026BD️ Football (10.75% ROI after 1561 Bets)\n"
        "\U0001F3C0 Basketball (8% ROI after 1450 Bets)\n"
        "\U0001F3C6 NBA Props (10% ROI after 1020 Bets)\n\n"
        "\u25A0 Within each group you can expect 150-200 bets a month. All groups offer +EV bets, "
        "with a focus on beating the closing line resulting in long-term profitability.\n"
        "\u25A0 Each subscription lasts 30 days, and after buying your subscription will be active immediately. Subscriptions are recurring, unless you cancel. \n"
        "\u2023 NOTE: Spaces in each group are limited to protect the odds. First come, first served. \n"
    )
    buttons = [
        [
            Button.inline("Football (€29,99)", b'service_1'),
            Button.inline("Basketball (€29,99)", b'service_2'),
            
        ],
        [
            Button.inline("NBA Props (€29,99)", b'service_3'),
            Button.inline("ALL IN ONE(€74,99)", b'service_4'),
        ]
    ]
    await event.respond(welcome_message, buttons=buttons)


@bot_client.on(events.CallbackQuery(pattern=b'service_1'))
async def service_1(event):
    footballOption = (
        "By purchasing this service(Football €29,99), you get access to: \n"
        "\t - Toms Tips Premium Football Group \U000026BD \n"
        "\u25A0 In this group, we will be posting 1x2, Asian Handicap and Over/Under bets. Over 75% of the bets in this group will be on the ‘big’ leagues, this way even people with restricted accounts can follow our bets. \n"
        "\u25A0 Most of the bets will be posted soon after the odds are released, which could be a week or even longer before the game actually takes place because this is the moment we can extract the most value. \n"
        "\u25A0 The main focus of this group is beating the closing line. This is our key indicator for performance and will also be tracked in the spreadsheet. \n You can expect 100-150 bets per month, and we expect an average ROI% of around 10%\n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter. \n"
        
    )
    await event.respond(footballOption)
    await bot_client.send_message(
        event.chat_id, 'Sending invoice for Football',
        file=generate_invoice(
            price_label='Pay', price_amount=2999, currency='EUR', title='Football', description= "",
            payload='Football', start_param='abc'
        )
    )
    # payment_message = "To proceed with Football, please make the payment."
    # buttons = [
    #     [
    #         Button.inline("Pay Now", b'pay_service_1'),
    #     ],
        
    # ]
    # await event.respond(payment_message, buttons=buttons)

@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_1'))
async def add_members_service_1(event):
    targetGroupId = 2096266635 
    targetGroupAccessHash = -198665311552621838
    target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
    sender = await event.get_sender()
    user_to_add = InputPeerUser(sender.id, sender.access_hash)
    # await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    accept_message = "You have successfully added to Foolball group" 
    await event.edit(accept_message)


@bot_client.on(events.CallbackQuery(pattern=b'decline_service_1'))
async def decline_service_1(event):
    decline_message = "Kindly, contact the admin" 
    await event.edit(decline_message)


@bot_client.on(events.CallbackQuery(pattern=b'service_2'))
async def service_2(event):
    basketballOption = (
        "By purchasing this service, you get access to: \n"
        "\t - Toms Tips Premium Basketball Group \U0001F3C0 \n"
        "\u25A0 In this group, we will be posting bets on the lower leagues of Basketball (No NBA). \n"
        "\u25A0 Most bets are placed within 48 hours of the match start, sometimes even minutes before. This way the turnover will be fast, and thus you can compound your bank quickly. \n"
        "\u25A0 When available, we will be tracking the closing lines of our bets in the spreadsheet. \n This remains a key indicator for our long term success, even on lower limit leagues. You can expect 150-200 bets a month in this group, and we expect an average ROI% of 10% \n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter. \n" 
    )
    await event.respond(basketballOption)
    await bot_client.send_message(
        event.chat_id, 'Sending invoice for Basketball',
        file=generate_invoice(
            price_label='Pay', price_amount=2999, currency='EUR', title='Basketball', description= "",
            payload='Basketball', start_param='abc'
        )
    )
    # payment_message = "To proceed with Basketball, please make the payment."
    # buttons = [
    #     [
    #         Button.inline("Pay Now", b'pay_service_2'),
    #     ],
        
    # ]
    # await event.respond(payment_message, buttons=buttons)


@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_2'))
async def add_members_service_2(event):
    targetGroupId = 2096266635 
    targetGroupAccessHash = -198665311552621838
    target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
    sender = await event.get_sender()
    user_to_add = InputPeerUser(sender.id, sender.access_hash)
    # await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    accept_message = "You have successfully added to Basketball group" 
    await event.edit(accept_message)


@bot_client.on(events.CallbackQuery(pattern=b'decline_service_2'))
async def decline_service_2(event):
    decline_message = "Kindly, contact the admin" 
    await event.edit(decline_message)


@bot_client.on(events.CallbackQuery(pattern=b'service_3'))
async def service_3(event):
    nbaOption = (
        "By purchasing this service, you get access to: \n"
        "\t - Toms Tips Premium NBA Props Group \U0001F3C6 \n"
        "\u25A0 In this group we will be posting NBA Player Prop bets. \n"
        "\u25A0 Most of the bets will be placed close to tip-off (start of the match), but we also take earlier lines when available. Because of this, even people from EU that don’t want to stay up late can still enjoy a part of our bets. Because the bets are posted close to tip-off, the turnover will be fast and thus you can compound your bank quickly. \n"
        "\u25A0 When available, we will be tracking the closing lines of our bets in the spreadsheet. This remains a key indicator for our long term success. You can expect 150-200 bets a month in this group, and we expect an average ROI% of 10%. \n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter." 
    )
    await event.respond(nbaOption)
    await bot_client.send_message(
        event.chat_id, 'Sending invoice for NBA Option',
        file=generate_invoice(
            price_label='Pay', price_amount=2999, currency='EUR', title='NBA Option', description= "",
            payload='nbaOption', start_param='abc'
        )
    )
    # payment_message = "To proceed with NBA option, please make the payment."
    # buttons = [
    #     [
    #         Button.inline("Pay Now", b'pay_service_3'),
    #     ],
        
    # ]
    # await event.respond(payment_message, buttons=buttons)


@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_3'))
async def add_members_service_3(event):
    targetGroupId = 2096266635 
    targetGroupAccessHash = -198665311552621838
    target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
    sender = await event.get_sender()
    user_to_add = InputPeerUser(sender.id, sender.access_hash)
    # await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    accept_message = "You have successfully added to NBA Props Group group" 
    await event.edit(accept_message)


@bot_client.on(events.CallbackQuery(pattern=b'decline_service_3'))
async def decline_service_3(event):
    decline_message = "Kindly, contact the admin" 
    await event.edit(decline_message)


@bot_client.on(events.CallbackQuery(pattern=b'service_4'))
async def service_4(event):
    allOption = (
        "By purchasing this service, you get access to all three groups: \n"
        "\u2022 Toms Tips Premium Football Group \n"
        "\u2022 Toms Tips Premium NBA Props Group \n"
        "\u2022 Toms Tips Premium Basketball Group \n"
        "\u25A0 By choosing the all in one deal you get the full potential of our services and a nice discount! The football group is focused on higher limits, but bets will often be taken early. The lower league basketball group and the NBA props group have a higher volume and a quick turnover time, but lower limits. \n"
        "\u25A0This unique combination of all three services will bring your betting game to the next level. We use closing line value as a key indicator in all our services, and this will bring us long term success. \n"
        "\u25A0 If you have any questions, feel free to reach out to @THKTipsNBA on twitter. \n"
    )
    await event.respond(allOption)
    await bot_client.send_message(
        event.chat_id, 'Sending invoice for All three groups',
        file=generate_invoice(
            price_label='Pay', price_amount=7999, currency='EUR', title='All three groups', description= "",
            payload='allOption', start_param='abc'
        )
    )
    # await bot_client.send_message(
    #     event.chat_id, 'Sending invoice for All the groups',
    #     file=generate_invoice(
    #         price_label='Pay', price_amount=2999, currency='RUB', title='All the groups', description= "",
    #         payload='allOption', start_param='abc'
    #     )
    # )
    # payment_message = "To proceed with all three groups, please make the payment."
    # buttons = [
    #     [
    #         Button.inline("Pay Now", b'pay_service_4'),
    #     ],
        
    # ]
    # await event.respond(payment_message, buttons=buttons)


@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_4'))
async def add_members_service_4(event):
    targetGroupId = 2096266635 
    targetGroupAccessHash = -198665311552621838
    target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
    sender = await event.get_sender()
    user_to_add = InputPeerUser(sender.id, sender.access_hash)
    # await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    accept_message = "You have successfully added to all three groups" 
    await event.edit(accept_message)


@bot_client.on(events.CallbackQuery(pattern=b'decline_service_4'))
async def decline_service_4(event):
    decline_message = "Kindly, contact the admin" 
    await event.edit(decline_message)

async def main():
    # await user_client.start(user_phone_number)
    while True:
        await send_message()
        # Sleep for 1 hour (3600 seconds)
        await asyncio.sleep(3600)  

async def start_bot():
    print("Bot is running!")
    await bot_client.start(bot_token=bot_token)
    await bot_client.run_until_disconnected()


# Start both clients
async def run_clients():
    user_task = asyncio.create_task(main())
    bot_task = asyncio.create_task(start_bot())
    await asyncio.gather(user_task, bot_task)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_clients())

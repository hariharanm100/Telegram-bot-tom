from telethon.sync import TelegramClient, events, Button, types, functions
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
import schedule
from datetime import datetime, timedelta, date
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import stripe
from telethon.tl.types import MessageEntityTextUrl
from telethon.tl import types
from telethon.tl.functions.messages import ExportChatInviteRequest


# Bot credentials
bot_api_id = 26689721
bot_api_hash = "41120962662844279ab6a08a0f60774f"
bot_token = '6321748774:AAFOXyERQa333nNIc3GBxcjM0s_uEL4LZi4'
provider_token = '284685063:TEST:ZDZhZjlhMjczMjdm'
bot_client = TelegramClient('bot_session', bot_api_id, bot_api_hash)


# User credentials
user_api_id = 26689721
user_api_hash = '41120962662844279ab6a08a0f60774f'
phone = '+31640436234'
user_client = TelegramClient(phone, user_api_id, user_api_hash)
user_client.connect()
if not user_client.is_user_authorized():
    try:
        user_client.send_code_request(phone)
        user_client.sign_in(phone, input('Enter the code: '))
    except:
        password = input("Enter password: ")
        me =  user_client.sign_in(password=password)

if  user_client.is_user_authorized():
    print("Authorized")

# Gsheet credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('lofty-fragment-409309-dc159bba07fc.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('usedet')
worksheet = sheet.sheet1
data = worksheet.get_all_values()
num_rows_filled = len(data)


stripe.api_key = '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'
# stripe.api_key =  "sk_test_51O88vNAptBIIWmpkbGayF2o2fe9JnrHlm9Jc3AWvokWtnonabDIs9crY6duhX2VKBxQuXku6mlkR8ssDUMPIzInt00UkHdmYb8"

async def check_payment_status1(session_id):
    count = 0
    while count < 90:
        count += 1
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            return True 
        await asyncio.sleep(20)


async def check_payment_status2(session_id):
    count = 0
    while count < 90:
        count += 1
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            return True 
        await asyncio.sleep(20)


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
    buttons = [
        [Button.text('Plans', resize=True) , Button.text('Cancel', resize=True)]
        
    ]
    entity = await client.get_entity('YOUR_CHANNEL_USERNAME')
    result = await client.export_chat_invite_link(entity)
    print(f"One-time use invite link: {result.link}")
    # Send the message with the keyboard
    await event.respond('Choose an option:', buttons=buttons)


@bot_client.on(events.NewMessage(pattern='^Plans$'))
async def handle_button1(event):
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


@bot_client.on(events.NewMessage(pattern='^Cancel$'))
async def handle_button2(event):
    sender = await event.get_sender()
    noOption = True
    if num_rows_filled >= 2:
        for i in range(2, num_rows_filled+1):
            print(i)
            row_values = worksheet.row_values(i)
            if int((row_values[0])) == int(sender.id) and row_values[3] == "complete" :
                noOption = False
                cancel_message = ("Do you like to cancel " + row_values[2] + " subscription")
                buttons = [
                    [
                        Button.inline("Yes", b'cancel_yes'),
                        Button.inline("No", b'cancel_no'),
                        
                    ],
                ]
                await event.respond(cancel_message, buttons=buttons)
                
                break
    if noOption:
        await event.respond("No Plans to cancel!")

    # data = worksheet.get_all_values()

    # # data = data[1:]
    # num_rows_filled = len(data)
    # if num_rows_filled >= 1:
    #     for row in data:
    #         print(sender.id)
    #         # print(row['Userid'])
    #         if int(sender.id) == int(row[0]) and row[3] == "complete" :
    #             cancel_message = ("Do you like to cancel " + row['service'] + " subscription")
    #             buttons = [
    #                 [
    #                     Button.inline("Yes", b'cancel_yes'),
    #                     Button.inline("No", b'cancel_no'),
                        
    #                 ],
    #             ]
    #             await event.respond(cancel_message, buttons=buttons)
    #             break
    # else:
        # await event.respond("No Plans to cancel!")


@bot_client.on(events.CallbackQuery(data=b'cancel_yes'))
async def cancel_yes(event):
    await event.respond('Plan has been cancelled successfully!')


@bot_client.on(events.CallbackQuery(data=b'cancel_no'))
async def cancel_yes(event):
    # Handle button press
    await event.respond('Continue enjoying our services!')


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
    session = stripe.checkout.Session.create(
            payment_method_types= ['card', 'paypal'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Subscribe to Football',
                        },
                        'recurring': {
                            'interval': 'month',  # Billing interval
                            'interval_count': 1,  # Number of intervals
                        },
                        'unit_amount': 2999,  # Amount in cents (e.g., $29.99)
                        },
                    'quantity': 1,
                },
            ],
            mode='subscription',
            
            allow_promotion_codes=True,
            success_url='https://www.google.com/',  # Redirect after successful payment
            cancel_url='https://yourdomain.com/cancel',  # Redirect if payment is canceled
            expires_at=int(datetime.now().timestamp()) + 1800  # Link expires after 1 hour (in seconds),  
        )
    checkout_session = stripe.checkout.Session.retrieve(session.id)
    payment_link = checkout_session.url
    # Creating buttons with URLs
    buttons = [
        Button.url('subscribe', payment_link)
    ]
    
    await event.respond("Click here to pay", buttons=buttons)
    payment_completed = await check_payment_status1(session.id)
    if payment_completed:
        await event.respond("Payment completed for Football. Thank you for subscribing!")
        
        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_1'),
                Button.inline("Decline", b'decline_service_1'),
            ],
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    else: 
        await event.respond("Timeout! Try again")

@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_1'))
async def add_members_service_1(event):
    global num_rows_filled
    footballTargetGroupId = 2133069468 
    footballTargetGroupAccessHash = 6572793378551583437
    footballtarget_group_entity = InputPeerChannel(footballTargetGroupId,footballTargetGroupAccessHash)
    # result = await user_client(ExportChatInviteRequest(footballtarget_group_entity))
    # print(result)
    sender = await event.get_sender()
    print(f"Sender Username: {sender.username}")
    if sender.username:
        print(f"Sender Username: {sender.username}")
        user_to_add =await user_client.get_input_entity(sender.username)
        print(user_to_add)
        print(footballtarget_group_entity)
        print(await user_client(InviteToChannelRequest(footballtarget_group_entity,[user_to_add])))
        insertRow = [sender.id, sender.access_hash, "Football", "complete", str(date.today()), "added"]
        num_rows_filled += 1
        worksheet.insert_row(insertRow, num_rows_filled)
        accept_message = "You have successfully added to Foolball group" 
        await event.respond(accept_message)
    else:
        add_usr_name =  ("Add username to your Telegram account \n"
                        "# Setting => Username \n"
                        "# Set the username if not there or Update the username \n"
                        "Trying clicking on accept"
                        )
        await event.respond(add_usr_name)


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
        "\u2023 By purchasing this service, you agree to the Terms and Conditions. \n"
    )
    await event.respond(basketballOption)
    session = stripe.checkout.Session.create(
            payment_method_types= ['card', 'paypal'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Subscribe to Lower League Basketballl',
                        },
                        'recurring': {
                            'interval': 'month',  # Billing interval
                            'interval_count': 1,  # Number of intervals
                        },
                        'unit_amount': 2999,  # Amount in cents (e.g., $29.99), RevokeChatInviteRequest
                        },
                    'quantity': 1,
                },
            ],
            mode='subscription',
            
            allow_promotion_codes=True,
            success_url='https://www.google.com/',  # Redirect after successful payment
            cancel_url='https://yourdomain.com/cancel',  # Redirect if payment is canceled
            expires_at=int(datetime.now().timestamp()) + 1800  # Link expires after 1 hour (in seconds),  
        )
    checkout_session = stripe.checkout.Session.retrieve(session.id)
    payment_link = checkout_session.url
    # Creating buttons with URLs
    buttons = [
        Button.url('subscribe', payment_link)
    ]
    
    await event.respond("Click here to pay", buttons=buttons)
    payment_completed = await check_payment_status2(session.id)
    if payment_completed:
        await event.respond("Payment completed for Basketball. Thank you for subscribing!")

        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_2'),
                Button.inline("Decline", b'decline_service_2'),
            ],
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    else: 
        await event.respond("Timeout! Try again")



@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_2'))
async def add_members_service_2(event):
    global num_rows_filled
    basketballTargetGroupId = 2078978318 
    basketballTargetGroupAccessHash = 3066502175714683773
    baskettarget_group_entity = InputPeerChannel(basketballTargetGroupId,basketballTargetGroupAccessHash)
    sender = await event.get_sender()
    print(f"Sender Username: {sender.username}")
    if sender.username:
        print(f"Sender Username: {sender.username}")
        user_to_add =await user_client.get_input_entity(sender.username)
        print(user_to_add)
        print(baskettarget_group_entity)
        print(await user_client(InviteToChannelRequest(baskettarget_group_entity,[user_to_add])))
        insertRow = [sender.id, sender.access_hash, "Basketball", "complete", str(date.today()), "added"]
        num_rows_filled += 1
        worksheet.insert_row(insertRow, num_rows_filled)
        accept_message = "You have successfully added to Basketball group" 
        await event.respond(accept_message)
    else:
        add_usr_name =  ("Add username to your Telegram account \n"
                        "# Setting => Username \n"
                        "# Set the username if not there or Update the username \n"
                        "Trying clicking on accept"
                        )
        await event.respond(add_usr_name)


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
        "\u2023 By purchasing this service, you agree to the Terms and Conditions \n"
    )
    await event.respond(nbaOption)
    session = stripe.checkout.Session.create(
            payment_method_types= ['card', 'paypal'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Subscribe to NBA Props',
                        },
                        'recurring': {
                            'interval': 'month',  # Billing interval
                            'interval_count': 1,  # Number of intervals
                        },
                        'unit_amount': 2999,  # Amount in cents (e.g., $29.99)
                        },
                    'quantity': 1,
                },
            ],
            mode='subscription',
            
            allow_promotion_codes=True,
            success_url='https://www.google.com/',  # Redirect after successful payment
            cancel_url='https://yourdomain.com/cancel',  # Redirect if payment is canceled
            expires_at=int(datetime.now().timestamp()) + 1800  # Link expires after 1 hour (in seconds),  
        )

    checkout_session = stripe.checkout.Session.retrieve(session.id)
    payment_link = checkout_session.url
    # Creating buttons with URLs
    buttons = [
        Button.url('subscribe', payment_link)
    ]
    
    await event.respond("Click here to pay", buttons=buttons)
    payment_completed = await check_payment_status2(session.id)
    if payment_completed:
        await event.respond("Payment completed for NBA Option. Thank you for subscribing!")

        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_3'),
                Button.inline("Decline", b'decline_service_3'),
            ],
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    else: 
        await event.respond("Timeout! Try again")


@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_3'))
async def add_members_service_3(event):
    global num_rows_filled
    nbaTargetGroupId = 1929741813 
    nbaTargetGroupAccessHash = -4821731871629234815
    target_group_entity = InputPeerChannel(nbaTargetGroupId,nbaTargetGroupAccessHash)
    sender = await event.get_sender()
    print(f"Sender Username: {sender.username}")
    if sender.username:
        print(f"Sender Username: {sender.username}")
        user_to_add =await user_client.get_input_entity(sender.username)
        print(user_to_add)
        print(target_group_entity)
        print(await user_client(InviteToChannelRequest(target_group_entity,[user_to_add])))
        insertRow = [sender.id, sender.access_hash, "NBA Option", "complete", str(date.today()), "added"]
        num_rows_filled += 1
        worksheet.insert_row(insertRow, num_rows_filled)
        accept_message = "You have successfully added to NBA Option group" 
        await event.respond(accept_message)
    else:
        add_usr_name =  ("Add username to your Telegram account \n"
                        "# Setting => Username \n"
                        "# Set the username if not there or Update the username \n"
                        "Trying clicking on accept"
                        )
        await event.respond(add_usr_name)


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
    "\u2023 By purchasing this service, you agree to the Terms and Conditions. \n"
    )
    await event.respond(allOption)
    session = stripe.checkout.Session.create(
            payment_method_types= ['card', 'paypal'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Subscribe to Combo Deal (Football + Basketball + NBA)',
                        },
                        'recurring': {
                            'interval': 'month',  # Billing interval
                            'interval_count': 1,  # Number of intervals
                        },
                        'unit_amount': 7499,  # Amount in cents (e.g., $29.99)
                        },
                    'quantity': 1,
                },
            ],
            mode='subscription',
            
            allow_promotion_codes=True,
            success_url='https://www.google.com/',  # Redirect after successful payment
            cancel_url='https://yourdomain.com/cancel',  # Redirect if payment is canceled
            expires_at=int(datetime.now().timestamp()) + 1800  # Link expires after 1 hour (in seconds),  
        )
    
    checkout_session = stripe.checkout.Session.retrieve(session.id)
    payment_link = checkout_session.url
    # Creating buttons with URLs
    buttons = [
        Button.url('subscribe', payment_link)
    ]
    
    await event.respond("Click here to pay", buttons=buttons)
    payment_completed = await check_payment_status2(session.id)
    if payment_completed:
        await event.respond("Payment completed for ALL Options. Thank you for subscribing!")


        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_4'),
                Button.inline("Decline", b'decline_service_4'),
            ],
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    else: 
        await event.respond("Timeout! Try again")


@bot_client.on(events.CallbackQuery(pattern=b'add_members_service_4'))
async def add_members_service_4(event):
    global num_rows_filled
    nbaTargetGroupId = 1929741813 
    nbaTargetGroupAccessHash = -4821731871629234815
    target_group_entity = InputPeerChannel(nbaTargetGroupId,nbaTargetGroupAccessHash)
    basketballTargetGroupId = 2078978318 
    basketballTargetGroupAccessHash = 3066502175714683773
    baskettarget_group_entity = InputPeerChannel(basketballTargetGroupId,basketballTargetGroupAccessHash)
    footballTargetGroupId = 2133069468 
    footballTargetGroupAccessHash = 6572793378551583437
    footballtarget_group_entity = InputPeerChannel(footballTargetGroupId,footballTargetGroupAccessHash)
    sender = await event.get_sender()
    print(f"Sender Username: {sender.username}")
    if sender.username:
        print(f"Sender Username: {sender.username}")
        user_to_add =await user_client.get_input_entity(sender.username)
        print(user_to_add)
        print(target_group_entity)
        print(await user_client(InviteToChannelRequest(footballtarget_group_entity,[user_to_add])))
        print(await user_client(InviteToChannelRequest(baskettarget_group_entity,[user_to_add])))
        print(await user_client(InviteToChannelRequest(target_group_entity,[user_to_add])))
        insertRow = [sender.id, sender.access_hash, "All Option", "complete", str(date.today()), "added"]
        num_rows_filled += 1
        worksheet.insert_row(insertRow, num_rows_filled)
        accept_message = "You have successfully added to All Option group" 
        await event.respond(accept_message)
    else:
        add_usr_name =  ("Add username to your Telegram account \n"
                        "# Setting => Username \n"
                        "# Set the username if not there or Update the username \n"
                        "Trying clicking on accept"
                        )
        await event.respond(add_usr_name)


@bot_client.on(events.CallbackQuery(pattern=b'decline_service_4'))
async def decline_service_4(event):
    decline_message = "Kindly, contact the admin" 
    await event.edit(decline_message)


async def send_message():
    data = worksheet.get_all_records()
    # Date comparison
    today = datetime.now()
    if data:
        insertLineCount = 1
        for row in data:
            insertLineCount += 1
            user_date = datetime.strptime(row['subdate'], "%Y-%m-%d")  # Adjust the date format
            if today - user_date > timedelta(days=30):
                await kick_user_from_group(row["service"], row["Userid"], row['userhash'], row['Userstatus'], insertLineCount)
    else:
        pass


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

from telethon.sync import TelegramClient, events, Button
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest

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
        welcome_message = (
            f"Welcome, ! \U0001F44B\n\n"  # Waving hand emoji
            "We are currently running 3 services:\n\n"
            "\U000026BD️ Football (10.75% ROI after 1561 Bets)\n"
            "\U0001F3C0 Basketball (8% ROI after 1450 Bets)\n"
            "\U0001F3C6 NBA Props (10% ROI after 1020 Bets)\n\n"
            "\u25A0 Within each group you can expect 150-200 bets a month. All groups offer +EV bets, "
            "with a focus on beating the closing line resulting in long-term profitability.\n"
            "\u25A0 Each subscription lasts 30 days, and after buying your subscription will be active immediately. Subscriptions are recurring, unless you cancel."
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
            "\u2023 NOTE: Spaces in each group are limited to protect the odds. First come, first served. \n"
        )
        await event.respond(footballOption)
        payment_message = "To proceed with Football, please make the payment."
        buttons = [
            [
                Button.inline("Pay Now", b'pay_service_1'),
            ],
           
        ]
        await event.respond(payment_message, buttons=buttons)

    @bot_client.on(events.CallbackQuery(pattern=b'pay_service_1'))
    async def pay_service_1(event):
        confirmation_message = "Payment for Football confirmed! Thank you." 
        await event.edit(confirmation_message)
        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_1'),
                Button.inline("Decline", b'decline_service_1'),
            ],
           
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    
    @bot_client.on(events.CallbackQuery(pattern=b'add_members_service_1'))
    async def add_members_service_1(event):
        targetGroupId = 2096266635 
        targetGroupAccessHash = -198665311552621838
        target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
        sender = await event.get_sender()
        user_to_add = InputPeerUser(sender.id, sender.access_hash)
        await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
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
            "\u2023 By purchasing this service, you agree to the Terms and Conditions. \n"
        )
        await event.respond(basketballOption)
        payment_message = "To proceed with Basketball, please make the payment."
        buttons = [
            [
                Button.inline("Pay Now", b'pay_service_2'),
            ],
           
        ]
        await event.respond(payment_message, buttons=buttons)

    @bot_client.on(events.CallbackQuery(pattern=b'pay_service_2'))
    async def pay_service_2(event):
        confirmation_message = "Payment for Basketball confirmed! Thank you." 
        await event.edit(confirmation_message)
        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_2'),
                Button.inline("Decline", b'decline_service_2'),
            ],
           
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    
    @bot_client.on(events.CallbackQuery(pattern=b'add_members_service_2'))
    async def add_members_service_2(event):
        targetGroupId = 2096266635 
        targetGroupAccessHash = -198665311552621838
        target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
        sender = await event.get_sender()
        user_to_add = InputPeerUser(sender.id, sender.access_hash)
        await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
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
            "\u2023 By purchasing this service, you agree to the Terms and Conditions \n"
        )
        await event.respond(nbaOption)
        payment_message = "To proceed with NBA option, please make the payment."
        buttons = [
            [
                Button.inline("Pay Now", b'pay_service_3'),
            ],
           
        ]
        await event.respond(payment_message, buttons=buttons)
        
    @bot_client.on(events.CallbackQuery(pattern=b'pay_service_3'))
    async def pay_service_3(event):
        confirmation_message = "Payment for NBA Props Group confirmed! Thank you." 
        await event.edit(confirmation_message)
        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_3'),
                Button.inline("Decline", b'decline_service_3'),
            ],
           
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    
    @bot_client.on(events.CallbackQuery(pattern=b'add_members_service_3'))
    async def add_members_service_3(event):
        targetGroupId = 2096266635 
        targetGroupAccessHash = -198665311552621838
        target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
        sender = await event.get_sender()
        user_to_add = InputPeerUser(sender.id, sender.access_hash)
        await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
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
        "\u2023 By purchasing this service, you agree to the Terms and Conditions. \n"
        )
        await event.respond(allOption)
        payment_message = "To proceed with all three groups, please make the payment."
        buttons = [
            [
                Button.inline("Pay Now", b'pay_service_4'),
            ],
           
        ]
        await event.respond(payment_message, buttons=buttons)

    @bot_client.on(events.CallbackQuery(pattern=b'pay_service_4'))
    async def pay_service_4(event):
        confirmation_message = "Payment for all three groups confirmed! Thank you." 
        await event.edit(confirmation_message)
        acceptOrDeclineMessage = "<a href='https://docs.google.com/document/d/e/2PACX-1vTvzil-qCjU2kUQ2NWDGiOcRNVzMPV7_fWK_bJLUAQOurmEZ3D4R712xJ5ayz0vYaEaycMDcmmOCM3S/pub'>Terms and Conditions</a>"
        buttons = [
            [
                Button.inline("Accept", b'add_members_service_4'),
                Button.inline("Decline", b'decline_service_4'),
            ],
           
        ]
        await event.respond(acceptOrDeclineMessage, buttons=buttons, parse_mode='html')
    
    @bot_client.on(events.CallbackQuery(pattern=b'add_members_service_4'))
    async def add_members_service_4(event):
        targetGroupId = 2096266635 
        targetGroupAccessHash = -198665311552621838
        target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
        sender = await event.get_sender()
        user_to_add = InputPeerUser(sender.id, sender.access_hash)
        await user_client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        accept_message = "You have successfully added to all three groups" 
        await event.edit(accept_message)


    @bot_client.on(events.CallbackQuery(pattern=b'decline_service_4'))
    async def decline_service_4(event):
        decline_message = "Kindly, contact the admin" 
        await event.edit(decline_message)

    
    
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
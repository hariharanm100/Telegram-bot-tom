# import requests
# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'


# # Replace 'GROUP_NAME' with your group name (case-sensitive)
# group_name = 'Tes UP hari'

# # Get updates from the bot
# response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
# data = response.json()

# # Loop through updates to find the group
# for result in data['result']:
#     chat = result.get('message', {}).get('chat', {})
#     chat_type = chat.get('type', '')
#     chat_title = chat.get('title', '')
#     print(chat)
#     print("###################")
#     if chat_type == 'supergroup' and chat_title == group_name:
#         group_id = chat.get('id', '')
#         print(f"Group ID for {group_name}: {group_id}")
#         break


import requests

# Your bot token
TOKEN = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

# Request URL
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

# Get recent updates
response = requests.get(url)
data = response.json()

print(data['result'])
# Print chat ID of the first group the bot encountered
chat_id = data['result'][0]['message']['chat']['id']
print("Chat ID:", chat_id)

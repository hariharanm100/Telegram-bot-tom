from telethon import TelegramClient

# Your user account's API credentials
api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
bot_token = '6551842711:AAHr6NidbwxcByMNb5ZiswX-Jrv8RYaektA'

# Group entity (replace 'group_username' with your group's username or ID)
group_entity = -1001917437122  # You can get this from the invite link or by using methods to resolve usernames

# List of users' usernames or phone numbers you want to add to the group
users_to_add = ["akilthangavel100"]  # Replace with actual usernames or phone numbers

# Create a client instance
client = TelegramClient('session_name', api_id, api_hash)

async def add_users_to_group():
    # Connect to the Telegram servers
    await client.connect()

    if not await client.is_user_authorized():
        # Log in if not already logged in
        await client.start()

    # Iterate through the list of users to add
     # Iterate through the list of users to add
    for user in users_to_add:
        try:
            # Add the user to the group
            await client.invoke(
                await client.get_input_entity(group_entity),
                await client.get_input_entity(user),
                version=2
            )
            print(f"Added {user} to the group!")
        except Exception as e:
            print(f"Failed to add {user}: {e}")


    # Disconnect the client
    await client.disconnect()

# Run the function to add users to the group
with client:
    client.loop.run_until_complete(add_users_to_group())

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
# You can be more explicit about the type for said ID by wrapping
# it inside a Peer instance. This is recommended but not necessary.
from telethon.tl.types import PeerUser, PeerChat, PeerChannel



# my_user    = await client.get_entity(PeerUser("+918489798100"))
# my_chat    = await client.get_entity(PeerChat(some_id))
# my_channel = await client.get_entity(PeerChannel(some_id))

api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'

# Your phone number and the group username where you want to add members
phone_number = '+918489798100'
group_username = 'tesaddmem'

# List of phone numbers of users you want to add to the group
members = ['USER1_PHONE_NUMBER', 'USER2_PHONE_NUMBER']  # Add more phone numbers as needed

with TelegramClient('session_name', api_id, api_hash) as client:
    client.connect()
    
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the code: '))
    
    # Get the group entity
    target_group = client.get_entity(group_username)
    
    # Add members to the group
    for member in members:
        try:
            my_user  = await client.get_entity(PeerUser("+918489798100"))
            print(my_user)
            user_to_add = client.get_input_entity(member)
            client(InviteToChannelRequest(target_group, [user_to_add]))
            print(f"Added {member} to the group!")
        except Exception as e:
            print(f"Failed to add {member}: {e}")

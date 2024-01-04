from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
import telethon
 

api_id =  26689721
api_hash = '41120962662844279ab6a08a0f60774f'
phone = '+31640436234'

chats = []
last_date = None
chunk_size = 200
groups=[]


client = TelegramClient(phone, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    try:
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    except telethon.errors.SessionPasswordNeededError:
        password = input("Enter password: ")
        me =  client.sign_in(password=password)

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
# print(chats)

for chat in chats:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(chat)
    print("#############################################")


footballTargetGroupId = 2133069468 
footballTargetGroupAccessHash = 6572793378551583437
target_group_entity = InputPeerChannel(footballTargetGroupId,footballTargetGroupAccessHash)
user_to_add = InputPeerUser(6558470586, 201207036318365083)
me = client.get_me()

# Print user ID and access hash
print("User ID:", me.id)
print("Access Hash:", me.access_hash)
user_to_add = client.get_input_entity('akilthangavel1')
print(user_to_add)
print(target_group_entity)
print(client(InviteToChannelRequest(target_group_entity,[user_to_add])))
# # print(client.kick_participant(target_group_entity, user_to_add))

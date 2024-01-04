from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
 

api_id = 27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
phone = '+918489798100'


chats = []
last_date = None
chunk_size = 200
groups=[]


client = TelegramClient(phone, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
print(chats)

targetGroupId = 2096266635 
targetGroupAccessHash = -198665311552621838
target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
# user_to_add = InputPeerUser(user['id'], user['access_hash'])
user_to_add = client.get_input_entity('akilthangavel100')
# print(user_to_add)
# print(target_group_entity)
# print(client(InviteToChannelRequest(target_group_entity,[user_to_add])))
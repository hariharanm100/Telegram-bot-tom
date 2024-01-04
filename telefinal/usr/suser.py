from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
import telethon
 

api_id =  27824897
api_hash = 'c7360424c507d2fb40196bbd6cd5c648'

user_api_id = 27824897
user_api_hash = 'c7360424c507d2fb40196bbd6cd5c648'
phone = '+918489798100'

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
    # try:
    #     if chat.megagroup == True:
    #         groups.append(chat)
    #         print("#############################################")
    #         print(chat)
    #         print("#############################################")
    #     else:
    #         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #         print(chat)
    #         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # except:
    #     continue
# print(chat)
# print('Choose a group to add members:')
# i=0
# for group in groups:
#     print(str(i) + '- ' + group.title)
#     i+=1


# g_index = input("Enter a Number: ")
# target_group=groups[int(g_index)]
# print(target_group)
# print(target_group.id, target_group.access_hash)

# footballChannelId=2014821675
# footballAccessHash=-8678746501267230078
targetGroupId = 1995731758 
targetGroupAccessHash = 5424220485967556720
target_group_entity = InputPeerChannel(targetGroupId,targetGroupAccessHash)
# user_to_add = InputPeerUser(user['id'], user['access_hash'])
user_to_add = client.get_input_entity('akilthangavel100')
print(user_to_add)
print(target_group_entity)
print(client(InviteToChannelRequest(target_group_entity,[user_to_add])))
# # print(client.kick_participant(target_group_entity, user_to_add))

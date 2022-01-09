# -*- coding: utf8 -*-
import os
import time
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
def main_handler(event,context):
    api_id = os.environ.get("APP_ID").split(";")  #输入api_id，一个账号一项，以分号隔开
    api_hash = os.environ.get("API_HASH").split(";")  #输入api_hash，一个账号一项，和上面的 api_id要一一对应，以分号隔开
    auth_string = os.environ.get("AUTH_KEY").split(";") #以分号隔开
    # print("api_id: " + str(api_id))
    # print("api_hash: " + str(api_hash))
    # print("auth_string: " + str(auth_string))
    for num in range(len(api_id)):
        client = TelegramClient(StringSession(auth_string[num]), api_id[num], api_hash[num])
        client.start()
        
        getfree_cloud_chat_entity = client.get_entity('t.me/GetfreeCloud')

        client.send_message(getfree_cloud_chat_entity, '/checkin@GetfreeCloud_Bot')  #第一项是机器人ID，第二项是发送的文字
        client.send_message("@ecyjcbot", '/checkin')  #第一项是机器人ID，第二项是发送的文字

        if(event["TriggerName"] == 'getfree_upgrade'):
            client.send_message(getfree_cloud_chat_entity, '/upgrade@GetfreeCloud')  #第一项是机器人ID，第二项是发送的文字
            print("Getfree Upgrade")

        time.sleep(5)  #延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        client.send_read_acknowledge("@jcbot")     #将机器人回应设为已读
        print("Done! App name:", api_id[num])
        # print(client.session.save())
    return
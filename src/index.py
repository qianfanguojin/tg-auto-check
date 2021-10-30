# -*- coding: utf8 -*-
import os
import time
from TGAutoSign.src.telethon.tl.types import User
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
def main_handler(event,context):
    api_id = os.environ.get("APP_ID").split(";")  #输入api_id，一个账号一项，以分号隔开
    api_hash = os.environ.get("API_HASH").split(";")  #输入api_hash，一个账号一项，和上面的 api_id要一一对应，以分号隔开
    auth_string = os.environ.get("AUTH_KEY").split(";") #以分号隔开
    print("api_id: " + str(api_id))
    print("api_hash: " + str(api_hash))
    print("auth_string: " + str(auth_string))
    for num in range(len(api_id)):
        client = TelegramClient(StringSession(auth_string[num]), api_id[num], api_hash[num])
        client.start()
        client.send_message("@BaigeiMe_Bot", '/checkin')  #第一项是机器人ID，第二项是发送的文字
        client.send_message("@ecyjcbot", '/checkin')  #第一项是机器人ID，第二项是发送的文字
        if(event["TriggerName"] == 'getfree_upgrade'):
            client.send_message("@BaigeiMe_Bot", '/upgrade')  #第一项是机器人ID，第二项是发送的文字
            print("Getfree Upgrade")
        time.sleep(5)  #延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        client.send_read_acknowledge("@BaigeiMe_Bot")     #将机器人回应设为已读
        client.send_read_acknowledge("@ecyjcbot")
        print("Done! App name:", api_id[num])
        # print(client.session.save())
    os._exit(0)
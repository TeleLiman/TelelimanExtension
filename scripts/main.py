import requests
import time
import GetJSON
import Helper
import socket

liste = GetJSON.getJSON()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

offset = open("/liman/extensions/teleliman/scripts/offset.txt","r").read()

while True:
    telegramData = Helper.getUpdates(int(offset)+1,)
    for message in telegramData["result"]:
        message_text = message["message"]["text"]
        offset =  message["update_id"]
        chat_id = message["message"]["from"]["id"]
        print(str(chat_id) + ":" + message_text)

        # Offset Kaydet
        offsetfile = open("/liman/extensions/teleliman/scripts/offset.txt","w")
        offsetfile.write(str(offset))
        offsetfile.close()
    
        if str(chat_id) == str(liste["userid"]):
            if "/shutdown" in message_text:
                Helper.sendShutdown()
                Helper.sendMessage("Sunucu başarıyla kapatıldı.")
            if "/reboot" in message_text:
                Helper.sendReboot()
                Helper.sendMessage("Sunucu başarıyla yeniden başlatıldı.")
            if "/update" in message_text:
                Helper.sendUpdate()
                Helper.sendMessage("Sunucu başarıyla güncellendi.")
            if "/ps" in message_text:
                Helper.sendPs()
            if "/startservice" in message_text:
                service_name = message_text.replace("/startservice","")
                service_name = service_name.strip()
                Helper.startService(service_name)
            if "/stopservice" in message_text:
                service_name = message_text.replace("/stopservice","")
                service_name = service_name.strip()
                Helper.stopService(service_name)
            if "/statusservice" in message_text:
                service_name = message_text.replace("/statusservice","")
                service_name = service_name.strip()
                response = Helper.statusService(service_name)
                Helper.sendMessage(response)
            if "/uname" in message_text:
                response = Helper.sendUname()
                Helper.sendMessage(response)
            if "/usage" in message_text:
                response = Helper.usage()
                Helper.sendMessage(response)
        else:
            print("Yetkisiz Erişim")
            Helper.sendMessage("Bu sunucuda yetkiniz bulunmamaktadır")
    # if sock.connect_ex(liste["serverip"]) != 0:
    #     Helper.sendMessage("Sunucu çöktü.")
    time.sleep(1)
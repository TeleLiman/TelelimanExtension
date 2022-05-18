import requests
import json
import paramiko
import GetJSON

json_list = GetJSON.getJSON()
token = json_list["telegramtoken"]
chat_id = json_list["userid"]
serverip = json_list["serverip"]
username = json_list["sshusername"]
password = json_list["sshpassword"]

path = "/liman/extensions/teleliman/"

# Telegram Methods
def sendMessage(text):
    url = "https://api.telegram.org/bot"+token+"/sendMessage"
    send_data = {"text": text, "chat_id": chat_id}
    response = requests.post(url, data=send_data)
    return response.text

def getUpdates(offset):
    url = "https://api.telegram.org/bot"+token+"/getUpdates"
    send_data = {"offset": offset}
    response = requests.post(url, data=send_data)
    data = json.loads(response.text)
    return data

def sendDocument():
    url = "https://api.telegram.org/bot"+token+"/sendDocument"
    send_data = {"chat_id": chat_id}
    files = {'document': open("temp.txt","r")}
    response = requests.post(url, data=send_data, files=files)

# Commands

def sendCommandServer(command):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(serverip, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    veri = stdout.read().decode()
    client.close()
    return veri

def sendShutdown():
    return sendCommandServer("shutdown now")

def sendReboot():
    return sendCommandServer("reboot")

def sendUpdate():
    return sendCommandServer("apt update & apt upgrade -y")

def startService(service_name):
    return sendCommandServer("systemctl start "+service_name+".service")

def stopService(service_name):
    return sendCommandServer("systemctl stop "+service_name+".service")

def statusService(service_name):
    return sendCommandServer("systemctl status "+service_name+".service")

def sendUname():
    return sendCommandServer("uname -a")

# Temp File
def tempfile(text):
    filee = open("/liman/extensions/teleliman/scripts/temp.txt","w")
    filee.write(text)
    filee.close()
    return True
import json

# Settings
def getJSON():
    settings = open("/liman/extensions/teleliman/scripts/settings.json","r")
    liste = json.loads(settings.read())
    return liste
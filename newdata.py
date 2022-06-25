import time
import json
import os
def data():
 if os.name == 'nt':
    pass
 if os.name == 'linux':
    import simplejson as json
 else:
    try:
        import json
    except:
        import simplejson as json
 file = open("settings.json", "r")
 data = json.load(file)
 file.close()
 data['token'] = input("Please Enter Your Account Token: ")
 data['channel'] = input("Please Enter Your Channel ID: ")
 data['sm'] = input("Toggle Sleep Mode (YES/NO): ")
 data['webhook'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
 if data['webhook'] != "None":
  data['webhookping'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')

import requests
import Server

ServerIP = "CHANGE THIS"
clipboard = requests.get('http://'+ServerIP+':8000/?type=get')
clipboard = clipboard.json()['clipboard']
Server.set_clipboard(clipboard)

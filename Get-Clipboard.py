import win32clipboard
import requests
import Server

clipboard = requests.get('http://'+Server.ServerIP+':8000/?type=get')
clipboard = clipboard.json()['clipboard']
Server.set_clipboard(clipboard)

import win32clipboard
import requests
import Server

requests.get('http://'+Server.ServerIP +
             ':8000/?type=set&clip='+Server.get_clipboard())

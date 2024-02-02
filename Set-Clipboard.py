import requests
import Server

ServerIP = "CHANGE THIS"
requests.get('http://'+ServerIP +
             ':8000/?type=set&clip='+Server.get_clipboard())

# ClipPy
Local shared clipboard using HTTP server. This allows you to easily share your clipboard cross devices

## Supported OS
- Windows
- iOS

## Setup
After installing the [required packages](#requirements), double click on `Server.py` or run it using the command line:
```powershell
#Installing packages:
> python -m pip install -r requirements.txt

#Running the server
> python server.py
Available network interfaces:
1. ['vEthernet (WSL)'] -> 172.19.160.1
2. ['Ethernet'] -> 192.168.1.123
5. ['VMware Network Adapter VMnet1'] -> 192.168.10.1
6. ['WiFi'] -> 192.168.126.17
7. ['(unknown)'] -> 127.0.0.1
Choose the interface (enter the number): 2
Server started at http://192.168.1.123:8000
```

## Client: Windows"
Update the `ServerIP` variable in each file and set it to the server IP. Then run the files as described below:
- `Set-Clipboard.py`: To share your current clipboard with the server.
- `Get-Clipboard.py`: To get the current shared clipboard from the server and set it as yours.

## Client: iOS - Using Shortcuts
To apply this shared clipboard in iOS using Shortcuts app, just create 2 shortcuts. One to share the iOS devices clipboard, the second is to apply the current shared clipboard.

### Share iOS clipboard
Download it from here: 
https://www.icloud.com/shortcuts/da32be38195a4628820d45690c388dad
![Image](https://imgur.com/tSlQNZF.png)

### Get the current shared clipboard
Download it from here: 
https://www.icloud.com/shortcuts/7e62e35bf85c48b58604579138eed878
![Image](https://imgur.com/QPoTuts.png)

This way it's easy to get or set the shared clipboard:
![Image](https://i.imgur.com/L5DqKv0.png)


# Contribute
If you would like to help improve this repo, you can help support other systems like Android.

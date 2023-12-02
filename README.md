# ClipPy
Local shared clipboard using HTTP server. This allows you to easily share your clipboard cross devices

## Requirements
`pip install -r requirements.txt`

## Supported OS
- Windows
- iOS

# How To Setup?
## Modify This Line in Server.py
```python
ServerIP = "CHANGE THIS"
```

## Run The Server
After installing the [required packages](#requirements), double click on `Server.py` or run it using the command line:
```powershell
python Server.py
```

## Client: Windows"
Download the same package, change "ServerIP" in "Server.py" to the server IP, then run the files as described below:
- `Set-Clipboard.py`: To share your current clipboard with the server.
- `Get-Clipboard.py`: To get the current shared clipboard from the server and set it as yours.

## Client: iOS - Using Shortcuts
To apply this shared clipboard in iOS using Shortcuts app, just create 2 shortcuts. One to share the iOS devices clipboard, the second is to apply the current shared clipboard.

### Share iOS clipboard
![Image](https://i.imgur.com/FbmItfM.png)

### Get the current shared clipboard
![Image](https://i.imgur.com/BUBVxgt.png)

This way it's easy to get or set the shared clipboard:
![Image](https://i.imgur.com/L5DqKv0.png)


# Contribute
If you would like to help improve this repo, you can help support other systems like Android.

# ClipPy
Local shared clipboard using HTTP server. This allows for easy application on different systems.

## Requirements
`pip install -r requirements.txt`

## Limitation
The Server must be running on windows environment. Just because it helps me :)

# How does it works?
<p align="center">
  <img src="https://i.imgur.com/axKGfBC.jpg">
</p>

Start by running "Server.py" on you windows machine. Just double click if you want. (After modifying the "CHANGE THIS")
then follow the below for each system you have.

## Windows - using the files "Set/Get-Clipboard.py"
From the host:
Just download and run. Set and Get clipboard files must work without any changes.

From another windows computer:
Download the same package, change "ServerIP" in "Server.py" to the host IP, then just by clicking Set or Get clipboard files it should work :)

## iOS - Using Shortcuts
To apply this shared clipboard in iOS using Shortcuts app, just create 2 shortcuts. One to share the iOS devices clipboard, the second is to apply the current shared clipboard.

### Share iOS clipboard
![Image](https://i.imgur.com/FbmItfM.png)

### Get the current shared clipboard
![Image](https://i.imgur.com/BUBVxgt.png)

This way it's easy to get or set the shared clipboard:
![Image](https://i.imgur.com/L5DqKv0.png)


## Upcoming (Propably not)
Android widget version :-)

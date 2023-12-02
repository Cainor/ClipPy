#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import win32clipboard
import json
import socket

ServerIP = "CHANGE THIS"


def set_clipboard(clip):
    global clipboard
    clipboard = clip
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(clip, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return True


def get_clipboard():
    win32clipboard.OpenClipboard()
    # If the clipboard was empty
    try:
        data = win32clipboard.GetClipboardData()
    except:
        data = "ClipPy"
    win32clipboard.CloseClipboard()
    return data


# Initial value is the Windows clipboard.
clipboard = get_clipboard()


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        querystring = parse_qs(parsed_path.query)
        global clipboard
        if('type' in querystring):
            type = querystring['type'][0]
            if(type == 'set'):
                clipboard = querystring['clip'][0]
                set_clipboard(clipboard)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({
                    'clipboard': str(clipboard),
                }).encode())
                return
            elif(type == 'get'):
                clipboard = get_clipboard()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({
                    'clipboard': clipboard,
                }).encode())
                return
        else:
            self.send_response(500)
            self.end_headers()
            return


if __name__ == '__main__':
    server = HTTPServer((ServerIP, 8000), RequestHandler)
    print('Server started at http://'+ServerIP+':8000')
    server.serve_forever()

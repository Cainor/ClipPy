#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import win32clipboard
import json
import netifaces as ni
import winreg as wr
from pprint import pprint


def get_connection_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    return iface_names
    
    
def get_network_interfaces():
    interfaces = ni.interfaces()
    print("Available network interfaces:")
    for i, interface in enumerate(interfaces, start=1):
        interface_ip = get_interface_ip(interface)
        if(interface_ip):
            print(f"{i}. {get_connection_name_from_guid([interface])} -> {interface_ip}")
    return interfaces

def choose_interface(interfaces):
    while True:
        try:
            choice = int(input("Choose the interface (enter the number): "))
            if 1 <= choice <= len(interfaces):
                return interfaces[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_interface_ip(interface):
    try:
        ip_address = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        return ip_address
    except KeyError:
        #print("Unable to retrieve IP address for the selected interface.")
        return None


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
    interfaces = get_network_interfaces()
    selected_interface = choose_interface(interfaces)
    ServerIP = get_interface_ip(selected_interface)

    server = HTTPServer((ServerIP, 8000), RequestHandler)
    print('Server started at http://'+ServerIP+':8000')
    server.serve_forever()

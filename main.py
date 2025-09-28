#current version: 1.2.2 (Final, until stated)
'''
- QR Generator can now accept entry text, or text files.
- Fixed issue where full QR Image doesn't show properly.

1.2.2:
- Organization for code readability.
- Project ends here, unless stated in README.
'''

# Script uses these following libraries, please install.
import qrcode # Most important.
import os # To open folder in different operating systems.
from PIL import ImageTk # Image view.
from tkinter import *
from tkinter import filedialog
from datetime import datetime

data = None #variable is used for holding data in qr generation

#---FUNCTIONS---
def clear_entry():
    entry.delete(0, END)

def open_folder():
    if os.name == 'posix': #macOS or Linux
        os.system(f'open "{os.getcwd()}"')
    else:
        os.startfile(os.getcwd())

def set_data(): # Preparing the data variable, placing user input into data var.
    global data
    data = entry.get()

def generate_qr(): # QR Code Generation process.
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Gets current date and time, for unique filename.

    qr = qrcode.QRCode(version=3, box_size=3, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill="Black", back_color="White")
    image.save(f"qr_code{date}.png") # Saves with unique filename.

def browse_file(): # Function to browse and read text file content
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path: # File selected becomes entry data.
        with open(file_path, 'r') as file:
            file_to_Text = file.read()
        entry.delete(0, END)
        entry.insert(0, file_to_Text)

def view_qr(): # Window used for QR Code view.
    # SETUP FOR VIEW
    top = Toplevel()
    top.title("Generated QR Code")

    labelset = Label(top, text="QR CODE GENERATED:")
    labelset.pack(pady=10)
    qr_image = ImageTk.PhotoImage(file=f"qr_code{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    label = Label(top, image=qr_image)
    label.image = qr_image  # keep a reference!
    label.pack()

    top.after(10000, lambda: top.destroy())  # auto-close after 10 seconds

#---GUI SETUP---
#main window
main = Tk()
main.title("QR Code Generator")

frame1 = Frame(main)
frame2 = Frame(main)

frame1.grid(row=0, column=0, padx=20, pady=20)
frame2.grid(row=0, column=1, padx=20, pady=20)

#frame1 contents
label_title = Label(frame1, text="QR Code Generator", font=('Arial', 20))
label_desc = Label(frame1, text="Enter anything to generate QR Code")
entry = Entry(frame1, width=30, font=('Arial', 17))
buttonGenerate = Button(frame1, text="Generate QR Code", command=lambda: [set_data(), generate_qr(), view_qr()], font=('Arial', 15))

#pack for frame1
label_title.pack()
label_desc.pack(pady=20)
entry.pack(pady=10)
buttonGenerate.pack(pady=20, fill='x', expand=True)

#frame2 contents
label_file = Label(frame2, text="Or, you can enter a text file path to generate QR code from its content.", wraplength=250, justify="center", font=('Helvetica', 15))
label_file.pack(pady=10)
for textIn, btnCommand in [
    ("Browse File", browse_file),
    ("Clear Entry", clear_entry),
    ("Open Storage Folder", open_folder)
]:
    Button(
        frame2, 
        text=textIn, 
        command=btnCommand, 
        width=25,
        font=('Helvetica', 15)
    ).pack(pady=10, fill='x', expand=True)
    
main.mainloop()
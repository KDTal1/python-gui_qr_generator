#current version: 1.3
'''
- Added error catching in functions.

1.3:
- Binary code feature: Convert your text into Binary.
'''

# Script uses these following libraries, please install.
import qrcode # Most important.
import os # To open folder in different operating systems.
from PIL import ImageTk # Image view.
from tkinter import *
from tkinter import filedialog, messagebox
from datetime import datetime

data = None #variable is used for holding data in qr generation
color = ["White", "Green"] # variable used to store color
qrCode_folder = "qrcodes" #folder that will be created

#---FUNCTIONS---
def clear_entry():
    entry.delete(0, END)

def make_folder(): # Block is added for function purposes.
    try:
        os.mkdir(qrCode_folder)
    except FileExistsError:
        pass
    except Exception as e:
        print(f"Debug Error: {e}")


def open_folder():
    if os.name == 'posix': #macOS or Linux
        os.system(f'open "{qrCode_folder}"')
    else:
        os.startfile(qrCode_folder)

def set_data(): # Preparing the data variable, placing user input into data var.
    global data
    data = entry.get()

def generate_qr(): # QR Code Generation process.
    global data #test
    colVar = 0

    #following is for testing purposes
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Gets current date and time, for unique filename.
    fileName = f"qrcode_{date}.png" #name for every qr code
    link = f"{qrCode_folder}/{fileName}"

    if testBinary.get() == "1": #testBinary test
        colVar = 1
        data = ' '.join(format(ord(char), 'b') for char in data)

    make_folder()

    try:
        qr = qrcode.QRCode(version=5, box_size=3, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill="Black", back_color=color[colVar])
        image.save(link) # Saves with unique filename.

    except Exception as e: #catch error if cap
        messagebox.showerror("Error", f"Failed to create QR Code: {e}\n\nActually, what did you do to get here?") # Shows error.


def browse_file(): # Function to browse and read text file content
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path: # File selected becomes entry data.
        with open(file_path, 'r') as file:
            file_to_Text = file.read()
        entry.delete(0, END)
        entry.insert(0, file_to_Text)

def view_qr(): # Window used for QR Code view.
    #following is for testing purposes
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Gets current date and time, for unique filename.
    fileName = f"qrcode_{date}.png" #name for every qr code
    link = f"{qrCode_folder}/{fileName}"

    # SETUP FOR VIEW
    top = Toplevel()
    top.title("Generated QR Code")

    labelset = Label(top, text="QR CODE GENERATED:", font=("Helvetica", 12))
    labelset.pack(pady=10)

    try: #this is to try code if it shows picture error.
        qr_image = ImageTk.PhotoImage(file=link) # test for link variable
        label = Label(top, image=qr_image)
        label.image = qr_image  # keep a reference!
        label.pack(pady=15, padx=15)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to show QR Code: {e}\n\nMight need to deal with that.")
        labelset.config(text="ERROR, NO QR CODE FOUND.")

    top.after(10000, lambda: top.destroy())  # auto-close after 10 seconds

#---GUI SETUP---
#main window
main = Tk()
main.title("QR Code Generator")
main.resizable(False, False)

frame1 = Frame(main)
frame2 = Frame(main)
subframe1 = Frame(frame1) #for features selection

frame1.grid(row=0, column=0, padx=20, pady=20)
frame2.grid(row=0, column=1, padx=20, pady=20)

#frame1 contents
label_title = Label(frame1, text="QR Code Generator", font=('Arial', 20))
label_desc = Label(frame1, text="Enter anything to generate QR Code")
entry = Entry(frame1, width=30, font=('Arial', 17))
label_features = Label(frame1, text="Features")
buttonGenerate = Button(frame1, text="Generate QR Code", command=lambda: [set_data(), generate_qr(), view_qr()], font=('Arial', 15))

#subframe1 contents
testBinary = StringVar(value="0")

binaryCheck = Checkbutton(subframe1, variable=testBinary, text="Binary").grid(row=0, column=0)

#pack for frame1
label_title.pack()
label_desc.pack(pady=20)
entry.pack(pady=10)
buttonGenerate.pack(pady=20, fill='x', expand=True)
label_features.pack(pady=5)
subframe1.pack(pady=5, fill="x", expand=True)

#pack for subframe1

#frame2 contents
label_file = Label(frame2, text="Or, you can enter a text file to generate QR code from its content.", wraplength=250, justify="center", font=('Helvetica', 10))
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
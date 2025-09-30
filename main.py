#current version: 1.3.1
#made in Python 3.13
'''
1.3.1:
- Optimizations in code
- Comments spread evenly.
'''

# Script uses these following imports.
import qrcode
import os 
from PIL import ImageTk
from tkinter import * 
from tkinter import filedialog, messagebox
from datetime import datetime

color = ["White", "Green"] # Used for color selection.
qrCode_folder = "qrcodes"

# Variables that will be used for returning value
date = ""
fileName = ""
link = ""

# --- FUNCTIONS ---
def clear_entry():
    entry.delete(0, END)

def open_folder():
    if os.name == 'posix': # used for other OS
        os.system(f'open "{qrCode_folder}"')
    else:
        os.startfile(qrCode_folder)

def generate_qr(): # Main process of generating QR Code
    global data, date, fileName, link
    colVar = 0 

    data = entry.get()
    date = datetime.now().strftime("%y%m%d-%H%M%S") # Gets current date and time, for unique filename.
    fileName = f"qrcode_{date}.png"
    link = f"{qrCode_folder}/{fileName}"

    if choice_Feature.get() == "1": # Will change if there are new variants.
        colVar = 1
        data = ' '.join(format(ord(char), 'b') for char in data)

    try: # What if there is no folder yet?
        os.mkdir(qrCode_folder)
    except FileExistsError: # Checks to see if folder is already produced.
        pass
    except Exception as e: # Checks other errors, basically.
        print(f"Debug Error: {e}")

    try: # The QR code is being created.
        qr = qrcode.QRCode(version=5, box_size=3, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill="Black", back_color=color[colVar])
        image.save(link) # Saves with unique filename.

    except Exception as e: # Uh oh, QR Code isn't made properly, we want user to see.
        messagebox.showerror("Error", f"Failed to create QR Code: {e}\n\nActually, what did you do to get here?") # Shows error.
    
    return date, fileName, link # QR Code is finished! We transfer it back to starting variables

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]) # What if user wants to add in text file instead?

    if file_path:
        with open(file_path, 'r') as file:
            file_to_Text = file.read() # It turns the text file into string
        entry.delete(0, END) # Deletes what's inside of entry first.
        entry.insert(0, file_to_Text) 

def view_qr(): # Pops up a window for user to see QR Code.
    global date, fileName, link

    # SETUP FOR VIEW
    top = Toplevel()
    top.title("Generated QR Code")
    top.resizable(False, False)

    labelset = Label(top, text="QR CODE GENERATED:", font=("Helvetica", 12))
    labelset.pack(pady=10)

    try: # User wants to see QR Code.
        qr_image = ImageTk.PhotoImage(file=link) # Checks if QR Code is in folder.
        label = Label(top, image=qr_image)
        label.image = qr_image  # For safekeeping purposes.
        label.pack(pady=15, padx=15)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to show QR Code: {e}\n\nMight need to deal with that.")
        labelset.config(text="ERROR, NO QR CODE FOUND.")

    top.after(10000, lambda: top.destroy())  # QR Code doesn't need to be there for long, so user has 10 seconds to screenshot the QR Code before it dies.

#  ---  GUI SETUP  ---
main = Tk()
main.title("QR Code Generator")
main.resizable(False, False)

frame1 = Frame(main)
frame2 = Frame(main)
subframe1 = Frame(frame1) # To add in a separate features area.

frame1.grid(row=0, column=0, padx=20, pady=20)
frame2.grid(row=0, column=1, padx=20, pady=20)

#frame1 contents
label_title = Label(frame1, text="QR Code Generator", font=('Arial', 20))
label_desc = Label(frame1, text="Enter anything to generate QR Code")
entry = Entry(frame1, width=30, font=('Arial', 17))
label_features = Label(frame1, text="Features")
buttonGenerate = Button(frame1, text="Generate QR Code", command=lambda: [generate_qr(), view_qr()], font=('Arial', 15))

#subframe1 contents
choice_Feature = StringVar(value="0")
for featTxt, val, rowNum, colNum in [ # In loop to optimize, and it looks good in readability.
    ("Normal", "0", "0", "0"),
    ("Binary", "1", "0", "1"),
]:
    Radiobutton(
        subframe1, 
        variable=choice_Feature, 
        text=featTxt, 
        value=val
    ).grid(
        row=rowNum,
        column=colNum,
        padx=2,
        pady=2
    )

#pack for frame1
label_title.pack()
label_desc.pack(pady=20)
entry.pack(pady=10)
buttonGenerate.pack(pady=20, fill='x', expand=True)
label_features.pack(pady=5)
subframe1.pack(pady=5, fill="x", expand=True)

#pack for subframe1
#nothing.

#frame2 contents
label_file = Label(frame2, text="Or, you can enter a text file to generate QR code from its content.", wraplength=250, justify="center", font=('Helvetica', 10))
label_file.pack(pady=10)

for textIn, btnCommand in [ # In loop to optimize, and it looks good in readability.
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
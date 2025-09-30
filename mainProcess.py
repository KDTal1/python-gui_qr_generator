import qrcode, os, random
from PIL import ImageTk 
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Main Process file is the main commands making the program functional.

color = ["White", "Green"] # Used for color selection.

# Variables that will be used for returning value
date = ""
fileName = ""
link = ""

# -- FUNCTIONS --
def generate_qr(folder, error_messages, choice_Feature, entry): # Main process of generating QR Code
    global data, date, fileName, link
    colVar = 0 

    data = entry.get()
    date = datetime.now().strftime("%y%m%d-%H%M%S") # Gets current date and time, for unique filename.
    fileName = f"qrcode_{date}.png"
    link = f"{folder}/{fileName}"

    if choice_Feature.get() == "1": # Will change if there are new variants.
        colVar = 1
        data = ' '.join(format(ord(char), 'b') for char in data)
    elif choice_Feature.get() == "2":
        messagebox.showinfo("Coming soon.", "Coming soon.")
    elif choice_Feature.get() == "3":
        messagebox.showinfo("Coming soon.", "Coming soon.")

    try: # What if there is no folder yet?
        os.mkdir(folder)
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
        messagebox.showerror("Error", f"Failed to create QR Code: {e}\n\n{error_messages[random.randint(0, 10)]}") # Shows error.
    
    return date, fileName, link # QR Code is finished! We transfer it back to starting variables

def view_qr(error_messages): # Pops up a window for user to see QR Code.
    global date, fileName, link

    # SETUP FOR VIEW
    top = Toplevel()
    top.title("Generated QR Code")
    top.resizable(False, False)

    labelset = Label(top, text="TEXT QR CODE GENERATED:", font=("Helvetica", 12))
    labelset.pack(pady=10)

    try: # User wants to see QR Code.
        qr_image = ImageTk.PhotoImage(file=link) # Checks if QR Code is in folder.
        label = Label(top, image=qr_image)
        label.image = qr_image  # For safekeeping purposes.
        label.pack(pady=15, padx=15)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to show QR Code: {e}\n\n{error_messages[random.randint(0, 10)]}")
        labelset.config(text="ERROR, NO QR CODE FOUND.")

    top.after(10000, lambda: top.destroy())  # QR Code doesn't need to be there for long, so user has 10 seconds to screenshot the QR Code before it dies.
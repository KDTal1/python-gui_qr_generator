#gonna try and make a practice project for qr code generation

#current version: 1.1
'''
- can now handle small text files.
- future versions will try to handle larger text files.
'''
import qrcode
from PIL import Image, ImageTk
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

    #show QR code in main GUI
    qr_canvas.qr_image_ref = ImageTk.PhotoImage(file=f"qr_code{date}.png")
    qr_canvas.create_image(100, 100, image=qr_canvas.qr_image_ref)
    qr_canvas.image = qr_canvas.qr_image_ref

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

#
main = Tk()
main.title("QR Code Generator")
main.geometry("500x650")

label = Label(main, text="Enter anything to generate QR Code")
label.pack(pady=20)
entry = Entry(main, width=30, font=('Arial', 17))
entry.pack(pady=10)
label_file = Label(main, text="Or, you can enter a text file path to generate QR code from its content.")
label_file.pack(pady=10)
button2 = Button(main, text="Browse File", command=browse_file)
button2.pack(pady=10)
button = Button(main, text="Generate QR Code", command=lambda: [set_data(), generate_qr()])
button.pack(pady=20)

#add canvas for QR code display
frame = Frame(main, width=400, height=400)
frame.pack(pady=20)
qr_canvas = Canvas(frame, width=200, height=200)
qr_canvas.pack(pady=45, anchor="center")

main.mainloop()
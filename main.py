#gonna try and make a practice project for qr code generation

#current version: 1.0
'''
- can only generate qr codes from text input
- will end project once program can generate qr codes from text files.
'''
import qrcode
from PIL import Image
from tkinter import *
from datetime import datetime

data = None #global variable to hold data for qr code generation

def generate_qr(): #process of generating qr code
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # get current date and time for unique filename
    qr = qrcode.QRCode(version=3, box_size=5.5, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill="Black", back_color="Red")

    image.save(f"qr_code{date}.png") #saves qr code with filename

    #show QR code in main GUI
    qr_image = PhotoImage(file=f"qr_code{date}.png")
    qr_canvas.create_image(100, 100, image=qr_image)
    qr_canvas.image = qr_image


def set_data(): #sets the data variable, putting the data got from entry box.
    global data
    data = entry.get()

#
main = Tk()
main.title("QR Code Generator")
main.geometry("500x500")

label = Label(main, text="Enter anything to generate QR Code")

label.pack(pady=20)
entry = Entry(main, width=30)
entry.pack(pady=10)
button = Button(main, text="Generate QR Code", command=lambda: [set_data(), generate_qr()])
button.pack(pady=20)

#add canvas for QR code display
frame = Frame(main, width=400, height=400)
frame.pack(pady=20)
qr_canvas = Canvas(frame, width=200, height=200)
qr_canvas.pack(pady=20)

main.mainloop()
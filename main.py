#current version: 1.3.3
#made in Python 3.13
'''
1.3.3:
- Optimization efforts
'''

# Script uses these following imports.
import commands, mainProcess
from tkinter import *

# -- To load before the whole thing runs.

commands.jsonTurned_variable() # Loaded before the main setup, to plug error_messaegs.json into the error_message variable 

#  ---  GUI SETUP  ---
main = Tk()
main.title("Text QR Code Generator")
main.resizable(False, False)

frame1 = Frame(main)
frame2 = Frame(main)
subframe1 = Frame(frame1) # To add in a separate features area.

frame1.grid(row=0, column=0, padx=20, pady=20)
frame2.grid(row=0, column=1, padx=20, pady=20)

#frame1 contents
label_title = Label(frame1, text="Text QR Code Generator", font=('Arial', 20))
label_desc = Label(frame1, text="Enter anything to generate QR Code")
entry = Entry(frame1, width=30, font=('Arial', 17))
label_features = Label(frame1, text="Features")
buttonGenerate = Button(frame1, text="Generate QR Code", command=lambda: [mainProcess.generate_qr(commands.qrCode_folder, commands.error_messages, choice_Feature, entry), mainProcess.view_qr(commands.error_messages)], font=('Arial', 15))

#subframe1 contents
choice_Feature = StringVar(value="0")
for featTxt, val, rowNum, colNum in [ # In loop to optimize, and it looks good in readability.
    ("Normal", "0", "0", "0"),
    ("Binary", "1", "0", "1"),
    ("Secret", "2", "0", "2"),
    ("Secret", "3", "0", "3")
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
    ("Browse File", lambda: commands.browse_file(entry)),
    ("Clear Entry", lambda: commands.clear_entry(entry)),
    ("Open Storage Folder", lambda: commands.open_folder())
]:
    Button(
        frame2, 
        text=textIn, 
        command=btnCommand, 
        width=25,
        font=('Helvetica', 15)
    ).pack(pady=10, fill='x', expand=True)
    
main.mainloop()
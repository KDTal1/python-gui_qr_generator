#current version: 1.5
#made in Python 3.13

# Script uses these following imports.
import commands, mainProcess
from tkinter import *

# -- To load before the whole thing runs.

commands.jsonTurned_variable() # Loaded before the main setup, to plug error_messaegs.json into the error_message variable 

#  ---  GUI SETUP  ---
main = Tk()
main.title("Text QR Code Generator - 1.5 - KDTal1")
main.resizable(False, False)

frame1 = Frame(main)
frame2 = Frame(main)
subframe1 = Frame(frame1) # To add in a separate features area.

frame1.grid(row=0, column=0, padx=20, pady=20)
frame2.grid(row=0, column=1, padx=20, pady=20)

#frame1 contents
label_title = Label(frame1, text="Text QR Code Generator", font=('Arial', 20))
label_desc = Label(frame1, text="Enter anything in the textbox", font=("Arial", 11, "italic"))
entry = Entry(frame1, width=30, font=('Arial', 17))
label_features = Label(frame1, text="- - - - - - - - - - - - MODES - - - - - - - - - - - -", font=('Helvetica', 15))
label_desc2 = Label(frame1, text="Then, press the button to generate QR Code", font=("Arial", 11, "italic"))
buttonGenerate = Button(frame1, text="GENERATE", command=lambda: [mainProcess.generate_qr(commands.qrCode_folder, commands.error_messages, choice_Feature, entry), mainProcess.view_qr(commands.error_messages)], font=('Arial', 15))

#subframe1 contents
choice_Feature = StringVar(value="0")
for featTxt, val, rowNum, colNum in [ # In loop to optimize, and it looks good in readability.
    ("Normal", "0", "0", "0"),
    ("Binary", "1", "0", "1"),
    ("Consochain", "2", "0", "2"),
    ("Reverse", "3", "0", "3"),
    ("Effigy", "4", "0", "4")
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
for variables in [label_title, label_desc, entry, label_desc2, buttonGenerate, label_features, subframe1]:
    variables.pack(pady=7, fill='x', expand=True)

#frame2 contents
label_file = Label(frame2, text="Or, you can browse a file you can turn into a QR Code.", wraplength=250, justify="center", font=('Helvetica', 10))
label_file.pack(pady=10)

for textIn, btnCommand, colorBtn in [ # In loop to optimize, and it looks good in readability.
    ("BROWSE FILE", lambda: commands.browse_file(entry), "#67B174"),
    ("CLEAR", lambda: commands.clear_entry(entry), "powder blue"),
    ("OPEN STORAGE", lambda: commands.open_folder(), "powder blue"),
    ("ABOUT", lambda: commands.about(), "powder blue")
]:
    Button(
        frame2, 
        text=textIn, 
        command=btnCommand, 
        width=25,
        font=('Helvetica', 15),
        bg=colorBtn
    ).pack(pady=10, fill='x', expand=True)
    
main.mainloop()
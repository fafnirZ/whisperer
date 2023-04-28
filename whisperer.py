from tkinter import *

from cryptidy import symmetric_encryption
import base64, os

root= Tk()

canvas1 = Canvas(root, width = 300, height = 500)
canvas1.pack()

def decrypt():  
    inputt = input_text.get()
    key = decrypt_key.get()
    result = ""
    if(len(key) % 16 != 0):
        result = "error key is incorrect length"
    else:
        _, res = symmetric_encryption.decrypt_message(inputt.encode("ascii"), key.encode())
        result = res

    global result_box
    result_box.delete(1.0, END)
    result_box.insert(INSERT, result)
    # canvas1.create_window(150, 400, window=text_label)

def encrypt():
    inputt = input_text.get()
    key = decrypt_key.get()
    result = ""
    if(len(key) % 16 != 0):
        result = "error key is incorrect length"
    else:
        res = symmetric_encryption.encrypt_message(inputt.encode(), key.encode())
        result = res

    global result_box
    result_box.delete(1.0, END)
    result_box.insert(INSERT, result)
    # canvas1.create_window(150, 400, window=text_label)


def toggle_mode(static=False):
    global MODE
    if MODE == "decrypt":
        MODE = "encrypt"
        update_mode_label(MODE)
    else:
        MODE = "decrypt"
        update_mode_label(MODE)


def add_mode_labels():
    global mode_label
    global key_label
    mode_label = Label(root, text= f'{MODE}', fg='blue', font=('helvetica', 12, 'bold'))
    key_label = Label(root, text="input your decryption key here", font=('helvetica', 12, 'bold'))
    # mode_label.pack()

def update_mode_label(new_mode):
    global mode_label
    global key_label
    mode_label["text"] = new_mode
    key_label["text"] = f"input your {new_mode} key here"

def toggle_trigger():
    global MODE
    if MODE == "decrypt":
        decrypt()
    else:
        encrypt()

MODE = "decrypt"
add_mode_labels()
toggle = Button(text='Toggle Mode', command=toggle_mode, bg='brown',fg='white')

submit = Button(text=f"submit", command=toggle_trigger, bg='brown',fg='white')
text_label = Label(root, text="input your text here", font=('helvetica', 12, 'bold'))
input_text = Entry(root)

decrypt_key = Entry(root)
result_box = Text(root, wrap=WORD, bd=0)

canvas1.create_window(150, 50, window=mode_label)
canvas1.create_window(150, 80, window=toggle)

canvas1.create_window(150, 120, window=text_label)
canvas1.create_window(150, 150, window=input_text)
canvas1.create_window(150, 170, window=key_label)
canvas1.create_window(150, 200, window=decrypt_key)

canvas1.create_window(150, 250, window=submit)
result_box.pack()

root.mainloop()
from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

# Encoding Function
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decoding Function
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        dec.append(list_dec)
    return "".join(dec)

# Function that executes on clicking Show Message
def Result():
    msg = Message.get()
    k = key.get()
    i = mode.get()
    
    if i == 1:
        Output.set(encode(k, msg))
    elif i == 2:
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo("Error", "Please choose either Encryption or Decryption. Try again.")

# Function that executes on clicking Reset
def Reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")

# Creating main window
wn = Tk()
wn.geometry("700x600")  
wn.configure(bg='dim grey')  
wn.title("Encrypt and Decrypt your Messages")
wn.state("zoomed")  

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

# Header Frame (Orange Background)
headingFrame1 = Frame(wn, bg="orange", bd=5)
headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.15)

headingLabel = Label(headingFrame1, text="Welcome to Encryption and \nDecryption",
                     fg='black', bg='orange', font=('Courier', 22, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Labels & Entry Fields inside Orange Frame
labelFrame = Frame(wn, bg="orange", bd=5)
labelFrame.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.5)

Label(labelFrame, text='Enter the Message:', font=('Courier', 16, 'bold'), bg='orange', fg='black').place(x=30, y=20)
msg = Entry(labelFrame, textvariable=Message, width=40, font=('calibre', 14, 'normal'))
msg.place(x=280, y=20)

Label(labelFrame, text='Enter the Key:', font=('Courier', 16, 'bold'), bg='orange', fg='black').place(x=30, y=80)
InpKey = Entry(labelFrame, textvariable=key, width=40, font=('calibre', 14, 'normal'))
InpKey.place(x=280, y=80)

Label(labelFrame, text='Select Mode:', font=('Courier', 16, 'bold'), bg='orange', fg='black').place(x=30, y=140)
Radiobutton(labelFrame, text='Encrypt', variable=mode, value=1, font=('Courier', 14), bg='orange', fg='black').place(x=280, y=140)
Radiobutton(labelFrame, text='Decrypt', variable=mode, value=2, font=('Courier', 14), bg='orange', fg='black').place(x=400, y=140)

Label(labelFrame, text='Result:', font=('Courier', 16, 'bold'), bg='orange', fg='black').place(x=30, y=200)
res = Entry(labelFrame, textvariable=Output, width=40, font=('calibre', 14, 'normal'))
res.place(x=280, y=200)

# Buttons with Proper Spacing
ShowBtn = Button(wn, text="Show Message", bg='SpringGreen2', fg='black', width=15, height=2, command=Result)
ShowBtn['font'] = font.Font(size=14, weight="bold")
ShowBtn.place(relx=0.2, rely=0.8)  # Positioned separately

ResetBtn = Button(wn, text='Reset', bg='blue2', fg='black', width=15, height=2, command=Reset)
ResetBtn['font'] = font.Font(size=14, weight="bold")
ResetBtn.place(relx=0.45, rely=0.8)  # Positioned separately

QuitBtn = Button(wn, text='Exit', bg='red2', fg='black', width=15, height=2, command=wn.destroy)
QuitBtn['font'] = font.Font(size=14, weight="bold")
QuitBtn.place(relx=0.7, rely=0.8)  # Positioned separately

wn.mainloop()

from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk()

root = Tk()
root.title("Denomination Counter")
root.configure("Light Blue")
root.geometry("650x400")

upload = Image.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0C04mSQer5MURkHpU3y3khpZeaObc1pPqCwbZSykmKg&s=10")
upload = upload.resize("300, 300")
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg ="Light Blue")
label.place(x=180, y=20)

label1 = Label(root, text="Hey user!, Welcome to denomination counter Application", bg="Light Blue")

label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msgbox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count")

    if Msgbox == "ok":
        topwin()


button1 = Button(root, text = "Let's get started!", command=msg, bg = "brown", fg="white")

button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination calculator")
    top.configure(bg="light grey")
    

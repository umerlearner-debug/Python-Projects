from tkinter import*
window = Tk()
window.title("Event Handlerr")
window.geometry('100x100')

def handle_keypress(event):
    """print the chracter associated to the keypress."""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\n The button was clicked")


button = Button(text="Click me")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()
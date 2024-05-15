from tkinter import*

#Created a window and set a background colour
window = Tk()
window.geometry("300x300")
window.title("My App")
window['bg']='#2C2A64'

#Added my logo image and edited the appearance
img = PhotoImage(file="applogo.png")
label = Label(window,image=img, borderwidth=0, highlightthickness=0 )
label.pack()


window.mainloop()


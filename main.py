from tkinter import*

#Created a window and set a background colour
window = Tk()
window.geometry("300x300")
window.title("My App")
window['bg']='#2C2A64'

#Added my logo image and edited the appearance
img = PhotoImage(file="applogo.png")
#This resizes the orginial picture by a factor of 6
img = img.subsample(6) 
#This allows the gray border of the picture is disappear
label = Label(window,image=img,borderwidth=0, highlightthickness=0)
#This allows the picture to be found on the left and north west of the page
label.pack(side=LEFT, anchor=NW)





window.mainloop()


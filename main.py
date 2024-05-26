from tkinter import*
import quiz_window #This imports the quiz window program

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

#This allows for a new window to open when the button is clicked
def open_quiz_window():
    quiz_window.create_quiz_window(window)

#Created a button to take quiz 
quiz_button = Button(window,text= "Take the Quiz",command=open_quiz_window) 
quiz_button.pack(pady=20)



window.mainloop()


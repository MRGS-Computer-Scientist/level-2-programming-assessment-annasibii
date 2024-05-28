from tkinter import*
import quiz_window #This imports the quiz window program

#Created a window and set a background colour
window = Tk()
window.geometry("300x300")
window.title("My App")
window['bg']='#2C2A64'

#Added my logo image and edited the appearance
img = PhotoImage(file="applogo.png")
#This resizes the original picture by a factor of 6
img = img.subsample(6) 
#This allows the gray border of the picture to disappear
label = Label(window,image=img,borderwidth=0, highlightthickness=0)
#This allows the picture to be found on the left and north west of the page
label.pack(side=LEFT, anchor=NW)

text_label = Label(window, text="My Goalie", font=("Arial", 80), fg="#98D8DD", bg="#2C2A64")
text_label.place(relx=0.5, rely=0.5, anchor=CENTER)

#This allows for a new window to open when the button is clicked
def open_quiz_window():
    quiz_window.create_quiz_window(window)

#Created a button to take quiz + designed the appearance
quiz_button = Button(window,text= "Take the Quiz",command=open_quiz_window, font=("Arial", 40), bg='#A20202', fg='white', borderwidth=7,)
quiz_button.place(relx=0.5, rely=0.8, anchor='s')


window.mainloop()


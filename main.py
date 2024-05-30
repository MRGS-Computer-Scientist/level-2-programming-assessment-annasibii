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

#Text displaying app name
text_label = Label(window, text="My Goalie", font=("Georgia", 48), fg="#98D8DD", bg="#2C2A64")
#Positioning of this text
text_label.place(relx=0.09, rely=0.01, anchor=NW)

#Text displaying the yellow text
text_label2 = Label(window, text="Are you curious to discover and work towards a personalised goal?", font =("Verdana", 25),
fg="#FBFF37", bg="#2C2A64")
#Positioning of this text
text_label2.place(relx=0.5, rely=0.3, anchor=CENTER)

#Text displaying the green text
text_label3 = Label(window, text="Take the quiz below to begin your journey towards success!" , font =("Verdana", 20),
fg="#A6DF05", bg="#2C2A64")
#Positioning of this text 
text_label3.place(relx=0.5, rely=0.5, anchor=CENTER)

#Created a button to take quiz + designed the appearance
quiz_button = Button(window,text= "Take the Quiz",command=open_quiz_window, font=("Arial", 37), bg='#A20202', fg='white', borderwidth=7,)
quiz_button.place(relx=0.5, rely=0.8, anchor='s')


window.mainloop()


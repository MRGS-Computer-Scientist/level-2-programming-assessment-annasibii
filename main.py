from tkinter import*

def go_to_quiz_frame():
  start_frame.pack_forget()
  quiz_frame.pack()
  #Hide the start frame 


#Created a window and set a background colour
window = Tk()
window.geometry("1280x800")
window.title("My App")
window['bg']='#2C2A64'

top_frame = Frame(window, width=1280, height=85, bg='#2C2A64')
#Keeping the same width and height of the frame. By default, frames only take up as much space as they need.
top_frame.pack_propagate(False)
top_frame.pack()

#Creating a frame that holds all the widgets
start_frame = Frame(window, width=1280, height=700, background='#2C2A64')
start_frame.pack()
#Maintains frame size with specified width and height
start_frame.pack_propagate(0)

#Added my logo image and edited the appearance
img = PhotoImage(file="applogo.png")
#This resizes the original picture by a factor of 6
img = img.subsample(6) 
#This allows the gray border of the picture to disappear
label = Label(top_frame,image=img,borderwidth=0, highlightthickness=0)
#This allows the picture to be found on the left and north west of the page
label.pack(side=LEFT, anchor=NW)

#Text displaying app name
text_label = Label(top_frame, text="My Goalie", font=("Georgia", 48), fg="#98D8DD", bg="#2C2A64")
#Positioning of this text
text_label.place(relx=0.09, rely=0.01, anchor=NW)

#Text displaying the yellow text
text_label2 = Label(start_frame, text="Are you curious to discover and work towards a personalised goal?", font =("Verdana", 25),
fg="#FBFF37", bg="#2C2A64")
#Positioning of this text
text_label2.place(relx=0.5, rely=0.25, anchor=CENTER)

#Text displaying the green text
text_label3 = Label(start_frame, text="Take the quiz below to begin your journey towards success!" , font =("Verdana", 20),
fg="#A6DF05", bg="#2C2A64")
#Positioning of this text 
text_label3.place(relx=0.5, rely=0.45, anchor=CENTER)

#Created a button to take quiz + designed the appearance
quiz_button = Button(start_frame,text= "Take the Quiz", font=("Arial", 37), bg='#A20202', fg='white', borderwidth=7,command=go_to_quiz_frame)
quiz_button.place(relx=0.5, rely=0.75, anchor=S)


######## Quiz Frame ########

quiz_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label2 = Label(quiz_frame, text="What area would you like your goal to focus on?", font =("Verdana", 30),
fg="#FBFF37", bg="#2C2A64")
#Positioning of this text
text_label2.place(relx=0.5, rely=0.15, anchor=CENTER)

# Define an IntVar variable to store the selected radio button
selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
productivity_radio = Radiobutton(quiz_frame, text="Productivity", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=selected_var, value=1, padx=20, pady=10,borderwidth=0, highlightthickness=0)

health_radio = Radiobutton(quiz_frame, text="Health", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=selected_var, value=2, padx=20, pady=10,borderwidth=0, highlightthickness=0)

# Positioning the radio buttons
productivity_radio.place(relx=0.2, rely=0.4, anchor=W)
health_radio.place(relx=0.2, rely=0.6, anchor=W)

quiz_button = Button(quiz_frame,text= "Next", font=("Arial", 30), bg='#A20202', fg='white', borderwidth=7,)
quiz_button.place(relx=0.8, rely=0.75, anchor=S)



window.mainloop()


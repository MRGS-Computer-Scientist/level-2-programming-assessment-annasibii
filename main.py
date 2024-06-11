from tkinter import*

def go_to_quiz_frame():
  start_frame.pack_forget()
  quiz_frame.pack()
  #Hide the start frame 

def go_to_next_frame():
  #Get the user's choice from the radio buttons
  choice = selected_var.get()
  #Hide the quiz frame
  quiz_frame.pack_forget()
  #show the frame selected by the user's choice 
  if choice ==1: #Productivity
    productivity_frame.pack()
  elif choice ==2: #Health
    health_frame.pack()

#Takes users into frame based of their productivity goal choice
def go_to_productivity_subgoal_frame():
  subgoal_choice = productivity_selected_var.get()
  productivity_frame.pack_forget()
  if subgoal_choice == 1:
      studying_frame.pack()
  elif subgoal_choice == 2:
      reading_frame.pack()
  elif subgoal_choice == 3:
      money_frame.pack()
    
#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_color():
  if selected_var.get()== 1:
    productivity_radio.config(bg="gray", fg="black")
    health_radio.config(bg='#2C2A64', fg="#A6DF05")
  elif selected_var.get()== 2:
    health_radio.config(bg="gray", fg="black")
    productivity_radio.config(bg='#2C2A64', fg="#A6DF05")
    
#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_productivity_color():
  if productivity_selected_var.get() == 1:
      studying_radio.config(bg="gray", fg="black")
      reading_radio.config(bg='#2C2A64', fg="#A6DF05")
      money_radio.config(bg='#2C2A64', fg="#A6DF05")
  elif productivity_selected_var.get() == 2:
      reading_radio.config(bg="gray", fg="black")
      studying_radio.config(bg='#2C2A64', fg="#A6DF05")
      money_radio.config(bg='#2C2A64', fg="#A6DF05")
  elif productivity_selected_var.get() == 3:
      money_radio.config(bg="gray", fg="black")
      studying_radio.config(bg='#2C2A64', fg="#A6DF05")
      reading_radio.config(bg='#2C2A64', fg="#A6DF05")

#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_studying_color():
  if studying_selected_var.get() == 1:
      study_radio1.config(bg="gray", fg="black")
      study_radio2.config(bg='#2C2A64', fg="#A6DF05")
  elif studying_selected_var.get() == 2:
      study_radio2.config(bg="gray", fg="black")
      study_radio1.config(bg='#2C2A64', fg="#A6DF05")


# Created button that takes users to the next frame (based of their previous choice)
def go_to_time_frame():
    studying_frame.pack_forget()
    time_frame.pack()
  

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

# Defined IntVar variable which stores the selected radio buttons
selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
productivity_radio = Radiobutton(quiz_frame, text="Productivity", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=selected_var, value=1, padx=20, pady=10,borderwidth=0, highlightthickness=0, selectcolor="#2C2A64",command=change_color)

#This is the health radio button 
health_radio = Radiobutton(quiz_frame, text="Health", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=selected_var, value=2, padx=20, pady=10,borderwidth=0, highlightthickness=0, selectcolor="#2C2A64", command=change_color)

#Positioning the radio buttons
productivity_radio.place(relx=0.2, rely=0.4, anchor=W)
health_radio.place(relx=0.2, rely=0.6, anchor=W)

#Created a next button -> takes users to the next frame (based of their choice)
quiz_button2 = Button(quiz_frame,text= "Next", font=("Arial", 30), bg='#A20202', fg='white', borderwidth=7,command=go_to_next_frame)
quiz_button2.place(relx=0.8, rely=0.75, anchor=S)

######## Productivity Frame ########
productivity_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label3 = Label(productivity_frame, text="What area in productivity would you like to have a goal for?", font =("Verdana", 30),
fg="#FBFF37", bg="#2C2A64")
#Positioning of this text
text_label3.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label = Label(productivity_frame, text="My goal is focused on...", font =("Verdana", 20),
fg="white", bg="#2C2A64")
#Positioning of this text
help_label.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
productivity_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
studying_radio = Radiobutton(productivity_frame, text="Studying", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=productivity_selected_var, value=1, padx=20, pady=10,borderwidth=0, highlightthickness=0, selectcolor="#2C2A64",command=change_productivity_color)
#positioning of studying button
studying_radio.place(relx=0.2, rely=0.4, anchor=W)

reading_radio = Radiobutton(productivity_frame, text="Reading", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=productivity_selected_var, value=2, padx=20, pady=10,borderwidth=0, highlightthickness=0, selectcolor="#2C2A64",command=change_productivity_color)
#positioning of reading button
reading_radio.place(relx=0.2, rely=0.5, anchor=W)

money_radio = Radiobutton(productivity_frame, text="Money", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=productivity_selected_var, value=3, padx=20, pady=10,borderwidth=0, highlightthickness=0, selectcolor="#2C2A64",command=change_productivity_color)
#positioning of money button
money_radio.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
quiz_button3 = Button(productivity_frame,text= "Next", font=("Arial", 30), bg='#A20202', fg='white', borderwidth=7,command=go_to_productivity_subgoal_frame)
quiz_button3.place(relx=0.8, rely=0.75, anchor=S)


######### The diff types of Productivity subgoals#####

#### Studying frame ####
studying_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label4 = Label(studying_frame, text="What Studying goal would you like to focus on", font =("Verdana", 30),
fg="#FBFF37", bg="#2C2A64")
#Positioning of this text
text_label4.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label2 = Label(studying_frame, text="I want to...", font =("Verdana", 20),
fg="white", bg="#2C2A64")
#Positioning of this text
help_label2.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined studying IntVar variable which stores the selected radio buttons
studying_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
study_radio1 = Radiobutton(studying_frame, text="Study 2 hours each day", font=("Verdana", 25),fg="#A6DF05", bg="#2C2A64", variable=studying_selected_var, value=1, padx=20, pady=10,borderwidth=0, highlightthickness=0, selectcolor="#2C2A64", command=change_studying_color)
#positioning of reading button
study_radio1.place(relx=0.2, rely=0.5, anchor=W)

#Radio button for studying option 2
study_radio2 = Radiobutton(studying_frame, text="Finish my homework", font=("Verdana", 25), fg="#A6DF05",bg="#2C2A64", variable=studying_selected_var, value=2, padx=20, pady=10, borderwidth=0, highlightthickness=0, selectcolor="#2C2A64",command=change_studying_color)
#positioning of this button 
study_radio2.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
quiz_button4 = Button(studying_frame,text= "Next", font=("Arial", 30), bg='#A20202', fg='white', borderwidth=7,command=go_to_time_frame)
quiz_button4.place(relx=0.8, rely=0.75, anchor=S)

#########

#### Reading frame ####
reading_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label5 = Label(reading_frame, text="What Reading goal would you like to focus on", font =("Verdana", 30),
fg="#FBFF37", bg="#2C2A64")
#Positioning of this text
text_label5.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label3 = Label(reading_frame, text="I want to...", font =("Verdana", 20),
fg="white", bg="#2C2A64")
#Positioning of this text
help_label3.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined reading IntVar variable which stores the selected radio buttons
reading_selected_var = IntVar()






#### Money frame ####
money_frame = Frame(window, width=1280, height=800, background='#2C2A64')


####### Health Frame ########
health_frame = Frame(window, width=1280, height=800, background='#2C2A64')



######(the button will have 2 commands?)


window.mainloop()


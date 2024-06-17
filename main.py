from tkinter import *

current_frame = "start_frame"

#Name of some variables
selected_catagory = ""
selected_timeframe = ""
selected_goal = ""

# Colour Palette
radio_button_bg_color = '#2C2A64'
radio_button_fg_color = '#A6DF05'


##### where each frame leads to ######
def go_to_quiz_frame():
    global current_frame
    current_frame = "quiz_frame"
    start_frame.pack_forget()
    quiz_frame.pack()
    #Hide the start frame

def go_to_start_frame():
    #Goes through all the child frames of the main window
    for frame in window.winfo_children():
        if frame != start_frame and frame != top_frame:
            frame.pack_forget()
    start_frame.pack()
    top_frame.pack()

def go_to_aboutus_frame():
    for frame in window.winfo_children():
        if frame != aboutus_frame and frame != top_frame:
            frame.pack_forget()
    aboutus_frame.pack()
    top_frame.pack()

def go_to_next_frame():
    global current_frame
    #Get the user's choice from the radio buttons
    choice = selected_var.get()
    print(choice)
    #Hide the quiz frame
    quiz_frame.pack_forget()
    if current_frame == "quiz_frame":
        #show the frame selected by the user's choice
        if choice == 1:  #Productivity
            current_frame = "productivity_frame"
            productivity_frame.pack()
        elif choice == 2:  #Health
            current_frame = "health_frame"
            health_frame.pack()


#Takes users into frame based of their productivity goal choice
def go_to_productivity_subgoal_frame():
    global current_frame
    subgoal_choice = productivity_selected_var.get()
    productivity_frame.pack_forget()
    if subgoal_choice == 1:
        current_frame = "studying_frame"
        studying_frame.pack()
    elif subgoal_choice == 2:
        current_frame = "reading_frame"
        reading_frame.pack()
    elif subgoal_choice == 3:
        current_frame = "money_frame"
        money_frame.pack()


#Takes users into frame based of their health goal choice
def go_to_health_subgoal_frame():
    global current_frame
    subgoal_choice = health_selected_var.get()
    health_frame.pack_forget()
    if subgoal_choice == 1:
        current_frame = "food_frame"
        food_frame.pack()
    elif subgoal_choice == 2:
        current_frame = "gym_frame"
        gym_frame.pack()
    elif subgoal_choice == 3:
        current_frame = "sport_frame"
        sport_frame.pack()
    elif subgoal_choice == 4:
        current_frame = "running_frame"
        running_frame.pack()


# Created button that takes users to the next frame (based of their previous choice, and forgets the previous frame)


def go_to_time_frame():
    global current_frame
    print(current_frame)
    if current_frame == "studying_frame":
        studying_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()
    elif current_frame == "reading_frame":
        reading_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()
    elif current_frame == "money_frame":
        money_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()
    elif current_frame == "food_frame":
        food_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()
    elif current_frame == "gym_frame":
        gym_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()
    elif current_frame == "sport_frame":
        sport_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()
    elif current_frame == "running_frame":
        running_frame.pack_forget()
        current_frame = "time_frame"
        time_frame.pack()


def go_to_result_frame():
    global current_frame
    time_frame.pack_forget()
    current_frame = "result_frame"
    result_frame.pack()

    #The goal message (displayed at end)
    goal_message = f"My goal is focused on {selected_catagory}. I want to {selected_goal} and I will achieve this goal by the {selected_timeframe}."

    #Replaces blank goal message with the correct goal message but only until user has played quiz
    goal_message_label.config(text=goal_message)


'''
def go_to_time_frame():
    studying_frame.pack_forget()
    time_frame.pack()

def go_to_time_frame():
    reading_frame.pack_forget()
    time_frame.pack()

def go_to_time_frame():
    money_frame.pack_forget()
    time_frame.pack()

def go_to_time_frame():
    food_frame.pack_forget()
    time_frame.pack()

def go_to_time_frame():
    gym_frame.pack_forget()
    time_frame.pack()

def go_to_time_frame():
    sport_frame.pack_forget()
    time_frame.pack()

def go_to_time_frame():
    running_frame.pack_forget()
    time_frame.pack()
'''

#############Colour of highlighted options##############


#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_color():
    if selected_var.get() == 1:
        productivity_radio.config(bg="gray", fg="black")
        health_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
    elif selected_var.get() == 2:
        health_radio.config(bg="gray", fg="black")
        productivity_radio.config(bg=radio_button_bg_color, fg="#A6DF05")


#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_productivity_color():
    global selected_catagory
    if productivity_selected_var.get() == 1:
        studying_radio.config(bg="gray", fg="black")
        reading_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        money_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Studying"
    elif productivity_selected_var.get() == 2:
        reading_radio.config(bg="gray", fg="black")
        studying_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        money_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Reading"
    elif productivity_selected_var.get() == 3:
        money_radio.config(bg="gray", fg="black")
        studying_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        reading_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Money"


#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_studying_color():
    global selected_catagory, selected_goal
    if studying_selected_var.get() == 1:
        study_radio1.config(bg="gray", fg="black")
        study_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "studying"
        selected_goal = "study 2 hours each day"
    elif studying_selected_var.get() == 2:
        study_radio2.config(bg="gray", fg="black")
        study_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Studying"
        selected_goal = "finish my homework"


def change_reading_color():
    global selected_catagory, selected_goal
    if reading_selected_var.get() == 1:
        reading_radio1.config(bg="gray", fg="black")
        reading_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        reading_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Reading"
        selected_goal = "Read 1 book"
    elif reading_selected_var.get() == 2:
        reading_radio2.config(bg="gray", fg="black")
        reading_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        reading_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Reading"
        selected_goal = "Read 5 books"
    elif reading_selected_var.get() == 3:
        reading_radio3.config(bg="gray", fg="black")
        reading_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        reading_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Reading"
        selected_goal = "Read 10 books"


def change_money_color():
    global selected_catagory, selected_goal
    if money_selected_var.get() == 1:
        money_radio1.config(bg="gray", fg="black")
        money_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Money"
        selected_goal = "Make more money"
    elif money_selected_var.get() == 2:
        money_radio2.config(bg="gray", fg="black")
        money_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Money"
        selected_goal = "Get a job"


#Gives different highlight colours to the buttons depending on which ones are selected/not selected
def change_health_color():
    global selected_catagory
    if health_selected_var.get() == 1:
        food_radio.config(bg="gray", fg="black")
        gym_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        sport_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        running_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Food"
    elif health_selected_var.get() == 2:
        gym_radio.config(bg="gray", fg="black")
        sport_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        running_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        food_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Gym"
    elif health_selected_var.get() == 3:
        sport_radio.config(bg="gray", fg="black")
        running_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        food_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        gym_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Sport"
    elif health_selected_var.get() == 4:
        running_radio.config(bg="gray", fg="black")
        sport_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        food_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        gym_radio.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Running"


def change_food_color():
    global selected_catagory, selected_goal
    if food_selected_var.get() == 1:
        food_radio1.config(bg="gray", fg="black")
        food_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        food_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Food"
        selected_goal = "have a more healthier diet"
    elif food_selected_var.get() == 2:
        food_radio2.config(bg="gray", fg="black")
        food_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        food_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Food"
        selected_goal = "increase my intake of protein "
    elif food_selected_var.get() == 3:
        food_radio3.config(bg="gray", fg="black")
        food_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        food_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Food"
        selected_goal = "increase my intake of fruits and veggies"


def change_gym_color():
    global selected_catagory, selected_goal
    if gym_selected_var.get() == 1:
        gym_radio1.config(bg="gray", fg="black")
        gym_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        gym_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Gym"
        selected_goal = "begin going gym"
    elif gym_selected_var.get() == 2:
        gym_radio2.config(bg="gray", fg="black")
        gym_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        gym_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Gym"
        selected_goal = "hit a new Pr (personal record)"
    elif gym_selected_var.get() == 3:
        gym_radio3.config(bg="gray", fg="black")
        gym_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        gym_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_catagory = "Gym"
        selected_goal = "go more consistently"


def change_sport_color():
    global selected_catagory, selected_goal
    if sport_selected_var.get() == 1:
        sport_radio1.config(bg="gray", fg="black")
        sport_radio2.config(bg=radio_button_bg_color, 
         fg="#A6DF05")
        sport_radio3.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        selected_catagory = "Sport"
        selected_goal = "learn a new sport"
    elif sport_selected_var.get() == 2:
        sport_radio2.config(bg="gray", fg="black")
        sport_radio1.config(bg=radio_button_bg_color, 
         fg="#A6DF05")
        sport_radio3.config(bg=radio_button_bg_color, 
         fg="#A6DF05")
        selected_catagory = "Sport"
        selected_goal = "master a sport skill"
    elif sport_selected_var.get() == 3:
        sport_radio3.config(bg="gray", fg="black")
        sport_radio1.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        sport_radio2.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        selected_catagory = "Sport"
        selected_goal = "consistently play sport"


def change_running_color():
    global selected_catagory, selected_goal
    if running_selected_var.get() == 1:
        running_radio1.config(bg="gray", fg="black")
        running_radio2.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        running_radio3.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        selected_catagory = "Running"
        selected_goal = "get into running"
    elif running_selected_var.get() == 2:
        running_radio2.config(bg="gray", fg="black")
        running_radio1.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        running_radio3.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        selected_catagory = "Running"
        selected_goal = "be more consistent with running"
    elif running_selected_var.get() == 3:
        running_radio3.config(bg="gray", fg="black")
        running_radio1.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        running_radio2.config(bg=radio_button_bg_color, 
        fg="#A6DF05")
        selected_catagory = "Running"
        selected_goal = "Run 2 laps at the park"


def change_time_color():
    global current_frame, selected_timeframe
    if time_selected_var.get() == 1:
        time_radio1.config(bg="gray", fg="black")
        time_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        time_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_timeframe = "end of this week"
    elif time_selected_var.get() == 2:
        time_radio2.config(bg="gray", fg="black")
        time_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        time_radio3.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_timeframe = "end of this month"
    elif time_selected_var.get() == 3:
        time_radio3.config(bg="gray", fg="black")
        time_radio1.config(bg=radio_button_bg_color, fg="#A6DF05")
        time_radio2.config(bg=radio_button_bg_color, fg="#A6DF05")
        selected_timeframe = "end of this year"


#Created a window and set a background colour
window = Tk()
window.geometry("1280x800")
window.title("My Goalie")
window['bg'] = radio_button_bg_color

top_frame = Frame(window, width=1280, height=85, bg='#2C2A64')
#Keeping the same width and height of the frame. By default, frames only take up as much space as they need.
top_frame.pack_propagate(False)
top_frame.pack()

#Added my logo image and edited the appearance
img = PhotoImage(file="applogo.png")
#This resizes the original picture by a factor of 6
img = img.subsample(6)
#This allows the gray border of the picture to disappear
label = Label(top_frame, image=img, borderwidth=0, highlightthickness=0)
#This allows the picture to be found on the left and north west of the page
label.pack(side=LEFT, anchor=NW)

#Text displaying app name
text_label = Label(top_frame,
                   text="My Goalie",
                   font=("Georgia", 48),
                   fg="#98D8DD",
                   bg="#2C2A64")
#Positioning of this text
text_label.place(relx=0.09, rely=0.01, anchor=NW)

home_button = Button(top_frame,
                     text="Home",
                     font=("Arial", 15),
                     bg='white',
                     fg='black',
                     borderwidth=2,
                     command=go_to_start_frame)
home_button.place(relx=0.8, rely=0.75, anchor=S)

aboutus_button = Button(top_frame,
                     text="About us",
                     font=("Arial", 15),
                     bg='white',
                     fg='black',
                     borderwidth=2,
                     command=go_to_aboutus_frame)
aboutus_button.place(relx=0.9, rely=0.75, anchor=S)

aboutus_frame = Frame(window, 
                      width=1280, 
                      height=700,
                      background='#2C2A64')

aboutus_label = Label(aboutus_frame,
                     text="About Us",
                     font=("Verdana", 30),
                     fg="#FBFF37",
                     bg="#2C2A64")
#Positioning of this text
aboutus_label.place(relx=0.5, rely=0.15, anchor=CENTER)

##### Start Frame #####

#Creating a frame that holds all the widgets
start_frame = Frame(window, width=1280, height=700, background='#2C2A64')
start_frame.pack()
#Maintains frame size with specified width and height
start_frame.pack_propagate(0)

#Text displaying the yellow text
text_label2 = Label(
    start_frame,
    text="Are you curious to discover and work towards a personalised goal?",
    font=("Verdana", 25),
    fg="#FBFF37",
    bg="#2C2A64")
#Positioning of this text
text_label2.place(relx=0.5, rely=0.25, anchor=CENTER)

#Text displaying the green text
text_label3 = Label(
    start_frame,
    text="Take the quiz below to begin your journey towards success!",
    font=("Verdana", 20),
    fg="#A6DF05",
    bg="#2C2A64")
#Positioning of this text
text_label3.place(relx=0.5, rely=0.45, anchor=CENTER)

#Created a button to take quiz + designed the appearance
quiz_button = Button(start_frame,
                     text="Take the Quiz",
                     font=("Arial", 37),
                     bg='#A20202',
                     fg='white',
                     borderwidth=7,
                     command=go_to_quiz_frame)
quiz_button.place(relx=0.5, rely=0.75, anchor=S)

######## Quiz Frame ########

quiz_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label2 = Label(quiz_frame,
                    text="What area would you like your goal to focus on?",
                    font=("Verdana", 30),
                    fg="#FBFF37",
                    bg="#2C2A64")
#Positioning of this text
text_label2.place(relx=0.5, rely=0.15, anchor=CENTER)

# Defined IntVar variable which stores the selected radio buttons
selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
productivity_radio = Radiobutton(quiz_frame,
                                 text="Productivity",
                                 font=("Verdana", 25),
                                 fg="#A6DF05",
                                 bg="#2C2A64",
                                 variable=selected_var,
                                 value=1,
                                 padx=20,
                                 pady=10,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 selectcolor="#2C2A64",
                                 command=change_color)

#This is the health radio button
health_radio = Radiobutton(quiz_frame,
                           text="Health",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=selected_var,
                           value=2,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_color)

#Positioning the radio buttons
productivity_radio.place(relx=0.2, rely=0.4, anchor=W)
health_radio.place(relx=0.2, rely=0.6, anchor=W)

#Created a next button -> takes users to the next frame (based of their choice)
next_button = Button(quiz_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_next_frame)
next_button.place(relx=0.8, rely=0.75, anchor=S)

######## Productivity Frame ########
productivity_frame = Frame(window,
                           width=1280,
                           height=800,
                           background='#2C2A64')

#Text displaying the yellow text
text_label3 = Label(
    productivity_frame,
    text="What area in productivity would you like to have a goal for?",
    font=("Verdana", 30),
    fg="#FBFF37",
    bg="#2C2A64")
#Positioning of this text
text_label3.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label = Label(productivity_frame,
                   text="My goal is focused on...",
                   font=("Verdana", 20),
                   fg="white",
                   bg="#2C2A64")
#Positioning of this text
help_label.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
productivity_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
studying_radio = Radiobutton(productivity_frame,
                             text="Studying",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=productivity_selected_var,
                             value=1,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_productivity_color)
#positioning of studying button
studying_radio.place(relx=0.2, rely=0.4, anchor=W)

reading_radio = Radiobutton(productivity_frame,
                            text="Reading",
                            font=("Verdana", 25),
                            fg="#A6DF05",
                            bg="#2C2A64",
                            variable=productivity_selected_var,
                            value=2,
                            padx=20,
                            pady=10,
                            borderwidth=0,
                            highlightthickness=0,
                            selectcolor="#2C2A64",
                            command=change_productivity_color)
#positioning of reading button
reading_radio.place(relx=0.2, rely=0.5, anchor=W)

money_radio = Radiobutton(productivity_frame,
                          text="Money",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=productivity_selected_var,
                          value=3,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_productivity_color)
#positioning of money button
money_radio.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button2 = Button(productivity_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_productivity_subgoal_frame)
next_button2.place(relx=0.8, rely=0.75, anchor=S)

######### The diff types of Productivity subgoals#####

#### Studying frame ####
studying_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label4 = Label(studying_frame,
                    text="What Studying goal would you like to focus on",
                    font=("Verdana", 30),
                    fg="#FBFF37",
                    bg="#2C2A64")
#Positioning of this text
text_label4.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label2 = Label(studying_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label2.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined studying IntVar variable which stores the selected radio buttons
studying_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
study_radio1 = Radiobutton(studying_frame,
                           text="Study 2 hours each day",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=studying_selected_var,
                           value=1,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_studying_color)
#positioning of reading button
study_radio1.place(relx=0.2, rely=0.5, anchor=W)

#Radio button for studying option 2
study_radio2 = Radiobutton(studying_frame,
                           text="Finish my homework",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=studying_selected_var,
                           value=2,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_studying_color)
#positioning of this button
study_radio2.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button3 = Button(studying_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_time_frame)
next_button3.place(relx=0.8, rely=0.75, anchor=S)

#########

#### Reading frame ####
reading_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label5 = Label(reading_frame,
                    text="What Reading goal would you like to focus on",
                    font=("Verdana", 30),
                    fg="#FBFF37",
                    bg="#2C2A64")
#Positioning of this text
text_label5.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label3 = Label(reading_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label3.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined reading IntVar variable which stores the selected radio buttons
reading_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
reading_radio1 = Radiobutton(reading_frame,
                             text="Read 1 book",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=reading_selected_var,
                             value=1,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_reading_color)
#positioning of reading button
reading_radio1.place(relx=0.2, rely=0.5, anchor=W)

#Radio button for reading option 2
reading_radio2 = Radiobutton(reading_frame,
                             text="Read 5 books",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=reading_selected_var,
                             value=2,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_reading_color)
#positioning of this button
reading_radio2.place(relx=0.2, rely=0.6, anchor=W)

#Radio button for reading option 3
reading_radio3 = Radiobutton(reading_frame,
                             text="Read 10 books",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=reading_selected_var,
                             value=3,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_reading_color)
#positioning of this button
reading_radio3.place(relx=0.2, rely=0.7, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button4 = Button(reading_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_time_frame)
next_button4.place(relx=0.8, rely=0.75, anchor=S)

#### Money frame ####
money_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label6 = Label(money_frame,
                    text="What Money goal would you like to focus on",
                    font=("Verdana", 30),
                    fg="#FBFF37",
                    bg="#2C2A64")
#Positioning of this text
text_label6.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label4 = Label(money_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label4.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined money IntVar variable which stores the selected radio buttons
money_selected_var = IntVar()

#Radio button for money option 1
money_radio1 = Radiobutton(money_frame,
                           text="Make more money",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=money_selected_var,
                           value=1,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_money_color)
#positioning of this button
money_radio1.place(relx=0.2, rely=0.5, anchor=W)

#Radio button for money option 2
money_radio2 = Radiobutton(money_frame,
                           text="Get a job",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=money_selected_var,
                           value=2,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_money_color)
#positioning of this button
money_radio2.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button5 = Button(money_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_time_frame)
next_button5.place(relx=0.8, rely=0.75, anchor=S)

##########

####### Health Frame ########
health_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label7 = Label(
    health_frame,
    text="What area in health would you like to have a goal for?",
    font=("Verdana", 30),
    fg="#FBFF37",
    bg="#2C2A64")
#Positioning of this text
text_label7.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label5 = Label(health_frame,
                    text="My goal is focused on...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label5.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
health_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
food_radio = Radiobutton(health_frame,
                         text="Food",
                         font=("Verdana", 25),
                         fg="#A6DF05",
                         bg="#2C2A64",
                         variable=health_selected_var,
                         value=1,
                         padx=20,
                         pady=10,
                         borderwidth=0,
                         highlightthickness=0,
                         selectcolor="#2C2A64",
                         command=change_health_color)
#positioning of food button
food_radio.place(relx=0.2, rely=0.4, anchor=W)

#Radio button for gym on health frame
gym_radio = Radiobutton(health_frame,
                        text="Gym",
                        font=("Verdana", 25),
                        fg="#A6DF05",
                        bg="#2C2A64",
                        variable=health_selected_var,
                        value=2,
                        padx=20,
                        pady=10,
                        borderwidth=0,
                        highlightthickness=0,
                        selectcolor="#2C2A64",
                        command=change_health_color)
#positioning of gym button
gym_radio.place(relx=0.2, rely=0.5, anchor=W)

#Radio button for sport on health frame
sport_radio = Radiobutton(health_frame,
                          text="Sport",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=health_selected_var,
                          value=3,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_health_color)
#positioning of sport button
sport_radio.place(relx=0.2, rely=0.6, anchor=W)

#Radio button for running on health frame
running_radio = Radiobutton(health_frame,
                            text="Running",
                            font=("Verdana", 25),
                            fg="#A6DF05",
                            bg="#2C2A64",
                            variable=health_selected_var,
                            value=4,
                            padx=20,
                            pady=10,
                            borderwidth=0,
                            highlightthickness=0,
                            selectcolor="#2C2A64",
                            command=change_health_color)
#positioning of running button
running_radio.place(relx=0.2, rely=0.7, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button6 = Button(health_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_health_subgoal_frame)
next_button6.place(relx=0.8, rely=0.75, anchor=S)

######### The diff types of Health subgoals#####

#### Food frame ####
food_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label8 = Label(food_frame,
                    text="What Food goal would you like to focus on",
                    font=("Verdana", 30),
                    fg="#FBFF37",
                    bg="#2C2A64")
#Positioning of this text
text_label8.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label6 = Label(food_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label6.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
food_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
food_radio1 = Radiobutton(food_frame,
                          text="Have a more healthier diet",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=food_selected_var,
                          value=1,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_food_color)
#positioning of food button 1
food_radio1.place(relx=0.2, rely=0.4, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
food_radio2 = Radiobutton(food_frame,
                          text="Increase my intake of protein",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=food_selected_var,
                          value=2,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_food_color)
#positioning of food button 2
food_radio2.place(relx=0.2, rely=0.5, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
food_radio3 = Radiobutton(food_frame,
                          text="Increase intake of fruits and veggies",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=food_selected_var,
                          value=3,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_food_color)
#positioning of food button
food_radio3.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button7 = Button(food_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_time_frame)
next_button7.place(relx=0.8, rely=0.75, anchor=S)

###### Gym frame ######
gym_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label9 = Label(gym_frame,
                    text="What Gym goal would you like to focus on",
                    font=("Verdana", 30),
                    fg="#FBFF37",
                    bg="#2C2A64")
#Positioning of this text
text_label9.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label7 = Label(gym_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label7.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
gym_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
gym_radio1 = Radiobutton(gym_frame,
                         text="Begin going gym",
                         font=("Verdana", 25),
                         fg="#A6DF05",
                         bg="#2C2A64",
                         variable=gym_selected_var,
                         value=1,
                         padx=20,
                         pady=10,
                         borderwidth=0,
                         highlightthickness=0,
                         selectcolor="#2C2A64",
                         command=change_gym_color)
#positioning of gym button 1
gym_radio1.place(relx=0.2, rely=0.4, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
gym_radio2 = Radiobutton(gym_frame,
                         text="Hit a new Pr (personal record)",
                         font=("Verdana", 25),
                         fg="#A6DF05",
                         bg="#2C2A64",
                         variable=gym_selected_var,
                         value=2,
                         padx=20,
                         pady=10,
                         borderwidth=0,
                         highlightthickness=0,
                         selectcolor="#2C2A64",
                         command=change_gym_color)
#positioning of gym button 2
gym_radio2.place(relx=0.2, rely=0.5, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
gym_radio3 = Radiobutton(gym_frame,
                         text="Go more consistently",
                         font=("Verdana", 25),
                         fg="#A6DF05",
                         bg="#2C2A64",
                         variable=gym_selected_var,
                         value=3,
                         padx=20,
                         pady=10,
                         borderwidth=0,
                         highlightthickness=0,
                         selectcolor="#2C2A64",
                         command=change_gym_color)
#positioning of gym button
gym_radio3.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button8 = Button(gym_frame,
                      text="Next",
                      font=("Arial", 30),
                      bg='#A20202',
                      fg='white',
                      borderwidth=7,
                      command=go_to_time_frame)
next_button8.place(relx=0.8, rely=0.75, anchor=S)

##### Sport Frame ######
sport_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label10 = Label(sport_frame,
                     text="What Sport goal would you like to focus on",
                     font=("Verdana", 30),
                     fg="#FBFF37",
                     bg="#2C2A64")
#Positioning of this text
text_label10.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label8 = Label(sport_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label8.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
sport_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
sport_radio1 = Radiobutton(sport_frame,
                           text="Learn a new sport",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=sport_selected_var,
                           value=1,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_sport_color)
#positioning of sport button 1
sport_radio1.place(relx=0.2, rely=0.4, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
sport_radio2 = Radiobutton(sport_frame,
                           text="Master a sport skill",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=sport_selected_var,
                           value=2,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_sport_color)
#positioning of sport button 2
sport_radio2.place(relx=0.2, rely=0.5, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
sport_radio3 = Radiobutton(sport_frame,
                           text="Consistently play sport",
                           font=("Verdana", 25),
                           fg="#A6DF05",
                           bg="#2C2A64",
                           variable=sport_selected_var,
                           value=3,
                           padx=20,
                           pady=10,
                           borderwidth=0,
                           highlightthickness=0,
                           selectcolor="#2C2A64",
                           command=change_sport_color)
#positioning of sport button 3
sport_radio3.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button9 = Button(sport_frame,
                       text="Next",
                       font=("Arial", 30),
                       bg='#A20202',
                       fg='white',
                       borderwidth=7,
                       command=go_to_time_frame)
next_button9.place(relx=0.8, rely=0.75, anchor=S)

##### Running Frame #####
running_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label11 = Label(running_frame,
                     text="What Running goal would you like to focus on",
                     font=("Verdana", 30),
                     fg="#FBFF37",
                     bg="#2C2A64")
#Positioning of this text
text_label11.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label9 = Label(running_frame,
                    text="I want to...",
                    font=("Verdana", 20),
                    fg="white",
                    bg="#2C2A64")
#Positioning of this text
help_label9.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
running_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
running_radio1 = Radiobutton(running_frame,
                             text="Get into running",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=running_selected_var,
                             value=1,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_running_color)
#positioning of running button 1
running_radio1.place(relx=0.2, rely=0.4, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
running_radio2 = Radiobutton(running_frame,
                             text="Be more consistent with running",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=running_selected_var,
                             value=2,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_running_color)
#positioning of running button 2
running_radio2.place(relx=0.2, rely=0.5, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
running_radio3 = Radiobutton(running_frame,
                             text="Run 2 laps at the park",
                             font=("Verdana", 25),
                             fg="#A6DF05",
                             bg="#2C2A64",
                             variable=running_selected_var,
                             value=3,
                             padx=20,
                             pady=10,
                             borderwidth=0,
                             highlightthickness=0,
                             selectcolor="#2C2A64",
                             command=change_running_color)
#positioning of running button 3
running_radio3.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button10 = Button(running_frame,
                       text="Next",
                       font=("Arial", 30),
                       bg='#A20202',
                       fg='white',
                       borderwidth=7,
                       command=go_to_time_frame)
next_button10.place(relx=0.8, rely=0.75, anchor=S)

####### Time Frame ######
time_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label12 = Label(time_frame,
                     text="When would you like this achieve this goal by",
                     font=("Verdana", 30),
                     fg="#FBFF37",
                     bg="#2C2A64")
#Positioning of this text
text_label12.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the white text
help_label10 = Label(time_frame,
                     text="“I will achieve this goal by...”",
                     font=("Verdana", 20),
                     fg="white",
                     bg="#2C2A64")
#Positioning of this text
help_label10.place(relx=0.5, rely=0.25, anchor=CENTER)

# Defined productivity IntVar variable which stores the selected radio buttons
time_selected_var = IntVar()

# Creating radio buttons - ensures that only one box can be checked
time_radio1 = Radiobutton(time_frame,
                          text="End Of This Week",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=time_selected_var,
                          value=1,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_time_color)
#positioning of time button 1
time_radio1.place(relx=0.2, rely=0.4, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
time_radio2 = Radiobutton(time_frame,
                          text="End Of This Month",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=time_selected_var,
                          value=2,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_time_color)
#positioning of time button 2
time_radio2.place(relx=0.2, rely=0.5, anchor=W)

# Creating radio buttons - ensures that only one box can be checked
time_radio3 = Radiobutton(time_frame,
                          text="End Of This Year",
                          font=("Verdana", 25),
                          fg="#A6DF05",
                          bg="#2C2A64",
                          variable=time_selected_var,
                          value=3,
                          padx=20,
                          pady=10,
                          borderwidth=0,
                          highlightthickness=0,
                          selectcolor="#2C2A64",
                          command=change_time_color)
#positioning of time button 3
time_radio3.place(relx=0.2, rely=0.6, anchor=W)

#Created button that takes users to the next frame (based of their previous choice)
next_button11 = Button(time_frame,
                       text="Next",
                       font=("Arial", 30),
                       bg='#A20202',
                       fg='white',
                       borderwidth=7,
                       command=go_to_result_frame)
next_button11.place(relx=0.8, rely=0.75, anchor=S)

##### Result Frame ####
result_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
text_label13 = Label(result_frame,
                     text="This is your personalised goal!",
                     font=("Verdana", 30),
                     fg="#FBFF37",
                     bg="#2C2A64")
#Positioning of this text
text_label13.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the yellow text
text_label14 = Label(result_frame,
                     text="(Take a screenshot to remember)",
                     font=("Verdana", 18),
                     fg="#FBFF37",
                     bg="#2C2A64")
#Positioning of this text
text_label14.place(relx=0.5, rely=0.22, anchor=CENTER)

goal_message_label = Label(result_frame,
                           text="",
                           font=("Verdana", 20),
                           fg="white",
                           bg="#2C2A64", wraplength=500)
goal_message_label.place(relx=0.5, rely=0.39, anchor=CENTER)

email_help_label = Label(result_frame, text="Please enter your email to receive your results")
email_help_label.place(relx=0.5, rely=0.65, anchor=CENTER)


email_entry = Text(result_frame, width=25, height=2)
email_entry.place(relx=0.5, rely=0.75, anchor=CENTER)


window.mainloop()

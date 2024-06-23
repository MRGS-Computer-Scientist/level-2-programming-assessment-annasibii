from tkinter import *
import tkinter.messagebox as messagebox

window = Tk()

# Colour Palette (in order: Purple, Red, Green, Yellow)
radio_button_bg_color = '#2C2A64'
radio_button_bg1_color = '#A20202'
radio_button_fg_color = '#A6DF05'
radio_button_fg1_color = '#FBFF37'

radio_button_list = []

current_options = []
quiz_options = ["Productivity", "Health"]
productivity_options = ["Studying", "Reading", "Money"]
health_options = ["Food", "Gym", "Sport", "Running"]
studying_options = ["Study 2 hours each day", "Finish my homework"]
reading_options = ["Read 1 book", "Read 5 books", "Read 10 books"]
money_options = ["Make more money", "Get a job"]
food_options = ["Have a more healthier diet", "Increase my intake of protein","Increase my intake of fruits and veggies"]
gym_options = ["Begin going gym", "Hit a new Pr (personal record)", "Go more consistently"]
sport_options = ["Learn a new sport", "Master a sport skill", "Consistently play sport"]
running_options = ["Get into running", "Be more consistent with running", "Run 2 laps at the park"]
time_options = ["End of this week", "End of this month", "End of 6 months", "End of the year"]

                
# Defined IntVar variable which stores the selected radio buttons
selected_option = IntVar()
selected_goals = []

next_frame = "Quiz"  #Starts at the start_frame and goes to quiz
current_mode = "QUIZ MODE"  # Will change to RESULT MODE when user finished quiz


def go_to_next_frame():
  global next_frame, current_mode, selected_goals
  print("Going to", next_frame)

  start_frame.pack_forget()

  if next_frame not in selected_goals:
    selected_goals.append(next_frame)

  if current_mode == "QUIZ MODE":

    if next_frame == "Quiz":
      create_radio_buttons(quiz_options, quiz_frame)
    elif next_frame == "Productivity":
      create_radio_buttons(productivity_options, quiz_frame)
      update_frame(
          "What area in productivity would you like to have a goal for?")
    elif next_frame == "Studying":
      create_radio_buttons(studying_options, quiz_frame)
      update_frame("What studying goal would you like to focus on?")
      current_mode = "TIME MODE"

    elif next_frame == "Reading":
      create_radio_buttons(reading_options, quiz_frame)
      update_frame("What reading goal would you like to focus on?")
      current_mode = "TIME MODE"

    elif next_frame == "Money":
      create_radio_buttons(money_options, quiz_frame)
      update_frame("What money goal would you like to focus on?")
      current_mode = "TIME MODE"
    
    elif next_frame == "Health":
      create_radio_buttons(health_options, quiz_frame)
      update_frame("What area in health would you like to have a goal for?")
    elif next_frame == "Food":
      create_radio_buttons(food_options, quiz_frame)
      update_frame("What food goal would you like to focus on?")
      current_mode = "TIME MODE"

    elif next_frame == "Gym":
      create_radio_buttons(gym_options, quiz_frame)
      update_frame("What gym goal would you like to focus on?")
      current_mode = "TIME MODE"

    elif next_frame == "Sport":
      create_radio_buttons(sport_options, quiz_frame)
      update_frame("What sport goal would you like to focus on?")
      current_mode = "TIME MODE"
      
    elif next_frame == "Running":
      create_radio_buttons(running_options, quiz_frame)
      update_frame("What running goal would you like to focus on?")
      current_mode = "TIME MODE"
    
    quiz_frame.pack()
  elif current_mode == "TIME MODE":
    create_radio_buttons(time_options, quiz_frame)
    update_frame("When would you like to achieve this goal by?")
    current_mode = "RESULT MODE"
  elif current_mode == "RESULT MODE":

    print(selected_goals)
    quiz_frame.pack_forget()

    category = selected_goals[-3]
    specific_goal = selected_goals[-2]
    timeframe = selected_goals[-1]
    
    goal_message_label.config(
        text=
        f"My goal is focused on {category}, I want to {specific_goal}, and I want to achieve this goal by the {timeframe} " ,
    fg=radio_button_fg_color,) #Text colour
    result_frame.pack()


def hide_all_frames():
    quiz_frame.pack_forget()
    start_frame.pack_forget()
    result_frame.pack_forget()
    aboutus_frame.pack_forget()
    final_frame.pack_forget()

def show_start_frame():
  hide_all_frames()
  start_frame.pack()


def show_aboutus_frame():
  hide_all_frames()
  aboutus_frame.pack()

# Creating radio buttons - ensures that only one box can be checked
def create_radio_buttons(options_list, current_frame):
  global radio_button_list

  for radio_button in radio_button_list:
    radio_button.destroy()

  radio_button_list = [
  ]  # Initialise radio button list, removing previous radio buttons

  relative_y = 0.35  # Used for positioning the radio button. This is the starting y-axis position
  for index, option in enumerate(options_list):

    radio_button = Radiobutton(current_frame,
                               text=option,
                               font=("Verdana", 25),
                               fg=radio_button_fg_color,
                               bg=radio_button_bg_color,
                               variable=selected_option,
                               value=index,
                               padx=20,
                               pady=10,
                               borderwidth=0,
                               highlightthickness=0,
                               selectcolor="#2C2A64",
                               command=selected_radio_button)

    radio_button.place(relx=0.2, rely=relative_y, anchor=W)
    relative_y = relative_y + 0.13
    print("Creating", index, "radio button")
    radio_button_list.append(radio_button)


def selected_radio_button():
  global radio_button_list, next_frame

  for radio_button in radio_button_list:
    radio_button.config(fg=radio_button_fg_color, bg=radio_button_bg_color)

  radio_button_list[selected_option.get()].config(bg="grey", fg="black")
  next_frame = radio_button_list[selected_option.get()]['text']


def update_frame(text_label):
  goalarea_label.configure(text=text_label,fg=radio_button_fg_color )


#### Top Frame ####
top_frame = Frame(window, width=1280, height=85, bg=radio_button_bg_color)
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
                   bg=radio_button_bg_color)
#Positioning of this text
text_label.place(relx=0.09, rely=0.01, anchor=NW)

home_button = Button(
    top_frame,
    text="Home",
    font=("Arial", 15),
    bg='white',
    fg='black',
    borderwidth=2,
    command=show_start_frame
)
home_button.place(relx=0.8, rely=0.75, anchor=S)

aboutus_button = Button(
    top_frame,
    text="About us",
    font=("Arial", 15),
    bg='white',
    fg='black',
    borderwidth=2,
    command=show_aboutus_frame
)
aboutus_button.place(relx=0.9, rely=0.75, anchor=S)

##### Start Frame #####

#Creating a frame that holds all the widgets
start_frame = Frame(window, width=1280, height=700, background='#2C2A64')
start_frame.pack()
#Maintains frame size with specified width and height
start_frame.pack_propagate(0)

#Text displaying the yellow text
question_label = Label(
    start_frame,
    text="Are you curious to discover and work towards a personalised goal?",
    font=("Verdana", 25),
    fg=radio_button_fg1_color,
    bg=radio_button_bg_color)
#Positioning of this text
question_label.place(relx=0.5, rely=0.25, anchor=CENTER)

#Text displaying the green text
action_label = Label(
    start_frame,
    text="Take the quiz below to begin your journey towards success!",
    font=("Verdana", 20),
    fg=radio_button_fg_color,
    bg=radio_button_bg_color)
#Positioning of this text
action_label.place(relx=0.5, rely=0.45, anchor=CENTER)

#Created a button to take quiz + designed the appearance
quiz_button = Button(start_frame,
                     text="Take the Quiz",
                     font=("Arial", 37),
                     bg=radio_button_bg1_color,
                     fg='white',
                     borderwidth=7,
                     command=go_to_next_frame)
quiz_button.place(relx=0.5, rely=0.75, anchor=S)

#### About us Frame ####
aboutus_frame = Frame(window, width=1280, height=800, background='#2C2A64')
aboutus_frame.pack_propagate(0)

aboutus_label = Label(aboutus_frame,
  text="About Us",
  font=("Verdana", 30),
  fg="#FBFF37",
  bg=radio_button_bg_color)
#Positioning of this text
aboutus_label.place(relx=0.5, rely=0.15, anchor=CENTER)

img1 = PhotoImage(file="aboutuslogo.png")
#This resizes the original picture by a factor of 5
img1 = img1.subsample(7)
#This allows the gray border of the picture to disappear
label1 = Label(aboutus_frame, image=img1, borderwidth=0, highlightthickness=0)
label1.place(relx=0.32, rely=0.07, anchor=NW)


# Adding the description text
aboutus_description = Label(aboutus_frame,
                            text=("My Goalie is designed to help assist young people on their journey towards success. It enables young people to go through a questionnaire where they can select from various options which help form a personalised goal. By visually selecting a goal helps to deepen the understanding of what the user’s goal is and how to achieve it."),
                            font=("Verdana", 15),
                            fg="white",
                            bg=radio_button_bg_color,
                            wraplength=500,)
# Positioning of this text
aboutus_description.place(relx=0.95, rely=0.5, anchor=E)

img2 = PhotoImage(file="aboutus.png")
#This resizes the original picture by a factor of 5
img2 = img2.subsample(5)
#This allows the gray border of the picture to disappear
label2 = Label(aboutus_frame, image=img2, borderwidth=0, highlightthickness=0)
label2.place(relx=0.1, rely=0.3, anchor=NW)

######## Quiz Frame ########

quiz_frame = Frame(window, width=1280, height=800, background='#2C2A64')
quiz_frame.pack_propagate(False)

#Text displaying the yellow text
goalarea_label = Label(quiz_frame,
                       text="What area would you like your goal to focus on?",
                       font=("Verdana", 30),
                       fg=radio_button_fg1_color,
                       bg=radio_button_bg_color)
#Positioning of this text
goalarea_label.place(relx=0.5, rely=0.15, anchor=CENTER)

#Created a next button -> takes users to the next frame (based of their choice)
next_button = Button(quiz_frame,
                     text="Next",
                     font=("Arial", 30),
                     bg=radio_button_bg1_color,
                     fg='white',
                     borderwidth=7,
                     command=go_to_next_frame)
next_button.place(relx=0.8, rely=0.75, anchor=S)

##### RESULT FRAME #####

result_frame = Frame(window, width=1280, height=800, background='#2C2A64')

#Text displaying the yellow text
goalresult_label13 = Label(result_frame,
                     text="This is your personalised goal!",
                     font=("Verdana", 30),
                     fg=radio_button_fg1_color,
                     bg=radio_button_bg_color)
#Positioning of this text
goalresult_label13.place(relx=0.5, rely=0.15, anchor=CENTER)

#Text displaying the yellow text
screenshot_label14 = Label(result_frame,
                     text="(Take a screenshot to remember)",
                     font=("Verdana", 18),
                     fg=radio_button_fg1_color,
                     bg=radio_button_bg_color)
#Positioning of this text
screenshot_label14.place(relx=0.5, rely=0.22, anchor=CENTER)

goal_message_label = Label(result_frame,
                           text="",
                           font=("Verdana", 20),
                           fg="white",
                           bg=radio_button_bg_color,
                           wraplength=500)
goal_message_label.place(relx=0.5, rely=0.39, anchor=CENTER)

email_help_label = Label(
    result_frame, text="Please enter your email to receive your results")
email_help_label.place(relx=0.5, rely=0.65, anchor=CENTER)

email_entry = Text(result_frame, width=25, height=2)
email_entry.place(relx=0.5, rely=0.75, anchor=CENTER)

def validate_email():
  email = email_entry.get("1.0", "end").strip()
  
  if not email:
     messagebox.showerror("Error", "Please enter your email address")
     return false 

  if len(email) < 6 or len(email) > 50:
     messagebox.showerror("Error", "Email length must be between 6 and 50 characters")
     return false 

  if "@" not in email:
     messagebox.showerror("Error", "Please enter a valid email address (e.g., emilymay@gmail.com)")
     return false

  return True 

def send_email():
    if validate_email():
      result_frame.pack_forget()  # Hide the result_frame
      final_frame.pack()

send_button = Button(result_frame,
                     text="send",
                     font=("Arial", 30),
                     bg=radio_button_bg1_color,
                     fg='white',
                     borderwidth=7,
                     command=send_email
                     )
send_button.place(relx=0.8, rely=0.75, anchor=S)

##### FINAL FRAME #####
final_frame = Frame(window, width=1280, height=800, background='#2C2A64')

congrats_label = Label(final_frame,
                    text="Congratulations!",
                    font=("Verdana", 30),
                    fg=radio_button_fg_color,
                    bg=radio_button_bg_color)
congrats_label.place(relx=0.5, rely=0.15, anchor=CENTER)

final_label = Label(final_frame,
                    text="You've completed the process and have been emailed your goal!",
                    font=("Verdana", 25),
                    fg="white",
                    bg=radio_button_bg_color)
final_label.place(relx=0.5, rely=0.30, anchor=CENTER)

window.mainloop()

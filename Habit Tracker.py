#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Import json to allow saving
import json


# In[1]:


# Initializes habits dictionary
habits = {}


# In[19]:


# Ask for user. Cleans input
user = input("What is your name?").strip().title()

# If user isn't already being tracked, adds to dictionary of users
if user not in habits:
    habits[user] = {}


# In[46]:


def save_habits():
    with open("habits.json", "w") as saved_habits:
        json.dump(habits, saved_habits, indent = 4)


# In[41]:


def add_habit():
    # Asks user to input habit and frequency 
    new_habit = input("Please enter a habit you would like to track")
    new_habit = new_habit.title().strip() # gets rid of whitespace and fixes capitalization
    while new_habit.strip() == "":
        new_habit = input("Please enter a new habit").strip().title()
    if new_habit in habits[user]:
        print("Habit already exists.")
        yes_or_no = input("Do you want to log this habit?")
        yes_or_no = yes_or_no.strip().lower()
        if yes_or_no == "yes":
            log_habit(user, new_habit)
            return
        else:
            print("Habit not logged. Come back when you want to log a habit")
            return
    
    frequency = input("How often would you like to perform this habit per week")

    # Convert frequency to an integer
    frequency = int(frequency)

    # Adds new habit to habit list
    habits[user][new_habit] = {"frequency" : frequency, "count" : 0} # initialize counter

    # Save habit
    save_habits()

    # Print message and ask for yes or no
    yes_or_no = input("Habit has been saved. Do you want to view saved habits?")

    # Allows response to be whatever case inputted and strips whitespace
    yes_or_no = yes_or_no.lower().strip()
    
    # If yes, shows habits. If no gives a goodbye
    if yes_or_no == "yes":
        view_habits()
    else:
        print("Have a nice day")


# In[42]:


def log_habit(user, habit_name = None):

    # if no habit name previously inputted, asks for habit
    if habit_name is None:
        while True:
            habit_name = input("What habit would you like to log?").strip().title()
            if habit_name == "":
                print("Entry not valid. Please try again.")
            else:
                break # if given a valid input, break loop

    # If habit is under inputted user's habits, add one to count; if not, asks user if they want to add habit
    if habit_name in habits[user]:
        habits[user][habit_name]['count'] += 1
        print(f"{habit_name} count is {habits[user][habit_name]['count']}")
        save_habits()
    else: 
        yes_or_no = input("Habit has not been logged in my system. Would you like to add it?")
        yes_or_no = yes_or_no.strip().lower()
        if yes_or_no == "yes":
            add_habit(user) # Brings user back to add habit
        else: 
            print("Please add a valid habit and try again") # Exit statement telling user to try again


# In[5]:


def view_habits():
    for habit_name, info in habits[user].items():
        print(f"{user}: {habit_name} {info['count']}/{info['frequency']}")


# In[37]:


def view_stats(user):
    # Create standard bar size
    bar_size = 10

    # Print user stats for only current user
    print(f" Stats for {user}:")

    user_habits = habits.get(user, "User not found")
        
    for habit_name, info in user_habits.items():
        count = info['count']
        frequency = info['frequency']

    # Skip a habit with a count of 0
        if count == 0:
            continue

        # Create progress bar
        progress = float(count / frequency)
        filled_bar = int(progress * bar_size)
        progress_bar = (filled_bar * "▓") + (bar_size - filled_bar) * "░"

        # Print progress bar
        print(f"{habit_name:<15}[{progress_bar}] {count}/{frequency} {progress*100:.1f}%")   


# In[ ]:


# ASK USER WHAT THEY WANT TO DO


# In[43]:


print("Please select the number of what you would like to do: \n 1. Add a habit \n 2. Log habit \n 3. View habits \n 4. View stats \n 5. Exit")
selection = input("Select a number")


# In[ ]:


if selection == "1":
    add_habit()
elif selection == "2":
    log_habit(user, habit_name = None)
elif selection == "3":
    view_habits()
elif selection == "4": 
    view_stats(user)
else:
    print("Have a nice day")


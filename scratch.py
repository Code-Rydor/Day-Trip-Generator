import random
from tkinter import N

print("Welcome to your day trip generator! This will help you choose the perfect day trip for your interests!")

destinations = ["Katy, TX", "Conroe, TX", "Houston, TX", "Pearland, TX", "Galveston, TX"]
restaurants = ["Arbys", "Wendys", "Burger King", "Taco Bell", "Dominos"]
travel_modes = ["Plane", "Car", "Bike", "Train", "Boat"]
entertainment_types = ["Bowling", "Frisbee Golf", "Fishing", "Mini Golf", "Shopping"]

random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_travel = random.choice(travel_modes)
random_entertainment = random.choice(entertainment_types)

def moving_on():
    print("Great, I'm glad that's decided! Let's move on...")

def confirm_destination_selection():
    answer = input(f"We have selected {random_destination} as your destination. Does this sound good to you? Enter y/n: ")
    return answer

def confirm_travel_selection():
    answer = input(f"We have selected {random_travel} as your mode of transportation. Does this sound good to you? Enter y/n: ")
    return answer

def confirm_entertainment_selection():
    answer = input(f"We have selected {random_entertainment} as your form of entertainment for the day. Does this sound good to you? Enter y/n: ")
    return answer

def confirm_restaurant_selection():
    answer = input(f"We have selected {random_restaurant} as your restaurant. Does this sound good to you? Enter y/n: ")
    return answer

def finalize_trip():
    answer = input("Would you like to finalize this trip? Enter y or n: ")
    return answer

def finalize_trip2():
#    print("It looks like you may have made a typo... ")
    answer = input("Would you like to finalize this trip? Enter y or n: ")
    return answer

#1. This function does too many things for what the project requirements specify

#2. How would I call the value of variable random_destination later when confirming
#   the trip if the value is scoped locally to this function?

#3. How do I set the re roll of a new random specific element to a function if the 
#   user decides at the end of this that they want to change one element if the trip?

#4. Could I write this function so that line 11 is declared inside this function so that when the captured value is called to finalize
#   the trip, it still holds the value that was declared within the function or no because the value would be getting called outside 
#   the scope of the function?

def destination_loop():
    destination_confirmed = confirm_destination_selection()
    confirmed = False
    while confirmed is False:
        if destination_confirmed == "y":
            confirmed = True
            moving_on()
        else:
            random_destination = random.choice(destinations) #the new value is now unable to be recalled for confirming trip because its local to this function
            destination_confirmed = input(f"Oh, sorry you didn't like this choice. No worries, we can try something else! How about {random_destination}? Enter y or n: ")
            

destination_loop()

print(random_destination) #prints something different than what was selected because its now outside the function
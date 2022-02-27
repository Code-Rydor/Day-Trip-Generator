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

string_destination = "destination"
string_restaurant = "restaurant"
string_travel = "mode of transportation"
string_entertainment = "form of entertainment"

def moving_on():
    print("Great, I'm glad that's decided! Let's move on...")

def confirm_destination_selection():
    answer = input(f"We have selected {random_destination} as your destination. Does this sound good to you? Enter y/n: ")
    return answer

def oh_sorry_destination():
    answer = input(f"Oh, sorry you didnt like this choice. No worries, we can try something else! How about {random_destination}? Enter y or n: ")
    return answer

destination_confirmed = confirm_destination_selection()
travel_mode_confirmed = 
confirmed = False

while confirmed is False:
    if destination_confirmed == "y":
        confirmed = True
        moving_on()
    else:
        random_destination = random.choice(destinations)
        destination_confirmed = input(f"Oh, sorry you didnt like this choice. No worries, we can try something else! How about {random_destination}? Enter y or n: ")

print(random_destination)


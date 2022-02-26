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

def oh_sorry():
    print("Oh, sorry you didnt like this choice. No worries, we can try something else!")

def confirm_selection(choice_1, choice_2):
    answer = input(f"We have selected {choice_1} as your {choice_2}. Does this sound good to you? Enter y/n: ")
    return answer

destination_confirmed = confirm_selection(random.choice(destinations), string_destination)


if destination_confirmed == "y":
    moving_on()
elif destination_confirmed == "n":
    oh_sorry()
    destination_confirmed = confirm_selection(random.choice(destinations), string_destination)
    if destination_confirmed == "y":
        moving_on()
    elif destination_confirmed == "n":
        oh_sorry()
        destination_confirmed = confirm_selection(random.choice(destinations), string_destination)
        if destination_confirmed == "y":
            moving_on()
        elif destination_confirmed == "n":
            oh_sorry()
            destination_confirmed = confirm_selection(random.choice(destinations), string_destination)
            if destination_confirmed == "y":
                moving_on()
            elif destination_confirmed == "n":
                oh_sorry()
                destination_confirmed = confirm_selection(random.choice(destinations), string_destination)
                if destination_confirmed == "y":
                    moving_on()
                elif destination_confirmed == "n":
                    print(f"You seem to be indecisive, so let me choose for you! You're going to {random_destination}! How fun!")
                
print("Now lets decide on a how you're going to get there!")

transportation_confirmed = confirm_selection(random.choice(travel_modes), string_travel)

if transportation_confirmed == "y":
    moving_on()
elif transportation_confirmed == "n":
    oh_sorry()
    transportation_confirmed = confirm_selection(random.choice(travel_modes), string_travel)
    if transportation_confirmed == "y":
        moving_on()
    elif transportation_confirmed == "n":
        oh_sorry()
        transportation_confirmed = confirm_selection(random.choice(travel_modes), string_travel)
        if transportation_confirmed == "y":
            moving_on()
        elif transportation_confirmed == "n":
            oh_sorry()
            transportation_confirmed = confirm_selection(random.choice(travel_modes), string_travel)
            if transportation_confirmed == "y":
                moving_on()
            elif transportation_confirmed == "n":
                oh_sorry()
                transportation_confirmed = confirm_selection(random.choice(travel_modes), string_travel)
                if transportation_confirmed == "y":
                    moving_on()
                elif transportation_confirmed == "n":
                    oh_sorry()
                    print(f"You seem to be indecisive, so let me choose for you! You're going to {random_travel}! How fun!")
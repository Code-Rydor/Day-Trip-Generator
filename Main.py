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

destination_confirmed = confirm_destination_selection()
confirmed = False

while confirmed is False:
    if destination_confirmed == "y":
        confirmed = True
        moving_on()
    else:
        random_destination = random.choice(destinations)
        destination_confirmed = input(f"Oh, sorry you didn't like this choice. No worries, we can try something else! How about {random_destination}? Enter y or n: ")

transportation_confirmed = confirm_travel_selection()
confirmed = False

while confirmed is False:
    if transportation_confirmed == "y":
        confirmed = True
        moving_on()
    else:
        random_travel = random.choice(travel_modes)
        transportation_confirmed = input(f"Oh, sorry you didn't like this choice. No worries, we can try something else! How about {random_travel}? Enter y or n: ")

entertainment_confirmed = confirm_entertainment_selection()
confirmed = False

while confirmed is False:
    if entertainment_confirmed == "y":
        confirmed = True
        moving_on()
    else:
        random_entertainment = random.choice(entertainment_types)
        entertainment_confirmed = input(f"Oh, sorry you didn't like this choice. No worries, we can try something else! How about {random_entertainment}? Enter y or n: ")

restaurant_confirmed = confirm_restaurant_selection()
confirmed = False

while confirmed is False:
    if restaurant_confirmed == "y":
        confirmed = True
        moving_on()
    else:
        random_restaurant = random.choice(restaurants)
        restaurant_confirmed = input(f"Oh, sorry you didn't like this choice. No worries, we can try something else! How about {random_restaurant}? Enter y or n: ")

print("Congratulations! We have completed generating your day trip! Now let's confirm that this is the trip you want...")
print(f"Your destination is: {random_destination}")
print(f"Your mode of transportation is: {random_travel}")
print(f"Your form of entertainment is: {random_entertainment}")
print(f"Your going to eat dinner at: {random_restaurant}")

is_trip_good = finalize_trip()
confirmed = False
typo = "It looks like you may have made a typo..."

while confirmed is False:
    if is_trip_good == "y":
        print(f"Prepare for your dream vacation to come alive! You will be arriving in {random_destination} by {random_travel}, where you will spend the day doing {random_entertainment}. You will end the day eating at your favorite restaurant, {random_restaurant}!")
        print("Enjoy your trip! (PS... We do accept tips!)")
        confirmed = True
    else:
        is_trip_good = finalize_trip2()
        

import random

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


#def moving_on():
    #print("Great, I'm glad that's decided! Let's move on...")

#def oh_sorry(choice):
    #input(f"Oh, sorry you didnt like this choice. No worries, we can try something else! How about {choice}? Enter y/n: ")

def confirm_selection(choice_1, choice_2):
    answer = input(f"We have selected {choice_1} as your {choice_2}. Does this sound good to you? Enter y/n: ")
    return answer


destination_happy = confirm_selection(random_destination, string_destination)
# if y, move on, if no, rerun randomization
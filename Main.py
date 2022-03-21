import random

destinations = ["Katy, TX", "Conroe, TX", "Houston, TX", "Pearland, TX", "Galveston, TX"]
restaurants = ["Arbys", "Wendys", "Burger King", "Taco Bell", "Dominos"]
travel_modes = ["Plane", "Car", "Bike", "Train", "Boat"]
entertainment_types = ["Bowling", "Frisbee Golf", "Fishing", "Mini Golf", "Shopping"]
   
def run_generator():
    random_trip = [random.choice(destinations), random.choice(restaurants), random.choice(travel_modes), random.choice(entertainment_types)]

    display_greeting()
    while True:
        display_trip(random_trip)
        user_input = input('\n Are you satisfied with this trip? y for Yes, n for No\n')
        if user_input == 'y':
            break
        elif user_input == 'n':
            random_trip = reselect_features(random_trip)
        else:
            print('That is not a valid selection...')

    display_ending()

    display_trip(random_trip)

def display_greeting():
    print('')
    print(f'Welcome to the Day Trip Generator! Here is a randomly generated trip!')

def display_trip(list_of_features):
    trip_string = ''
    trip_labels = ['Destination', 'Restaurant', 'Transportation', 'Entertainment']
    for index in range(len(list_of_features)):
        trip_string += f' {trip_labels[index]}: {list_of_features[index]} \n'

    print(trip_string)
def display_ending():
    print(f'Perfect! Enjoy your fun filled day! Here is the final trip itinerary:\n')

def reselect_features(list_of_features):
    user_input = input('Which feature would you like to change?\n 1 for Destination\n 2 for Restaurant\n 3 for Transportation\n 4 for Entertainment\n ')

    if user_input == "1":  
        list_of_features[0] = random.choice(destinations)        
    elif user_input == "2":
        list_of_features[1] = random.choice(restaurants)
    elif user_input == "3":  
        list_of_features[2] = random.choice(travel_modes)        
    elif user_input == "4":
        list_of_features[3] = random.choice(entertainment_types)

    return list_of_features

run_generator()
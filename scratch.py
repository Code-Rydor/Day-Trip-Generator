import random

'''def generate_destination(answer):
    if answer == y:
        print("Great! Moving on...")
    else:


print(random.choice(mylist))

dest_1 = destinations[] # make a copy of the input list
random.shuffle (dest_1)
for i in range(1):
    print(dest_1.pop())

    dest_1 = destinations # make a copy of the input list
random.shuffle (dest_1)
for i in range(1):
    print(dest_1.pop())

#JJ's rework of my practice funtion calling a function

def add_two_numbers(number_one, number_two):
    sum = int(number_one) + int(number_two)
    return sum
def words(word_to_print, number_of_cycles):
    for count in range(number_of_cycles):
        print(count)
        print(word_to_print)
first_number = input("Please enter the first number!")
second_number = input("Please enter the second number!")
other_result = add_two_numbers(first_number, second_number)
my_word = input("What's your favorite word?")
words(my_word, other_result)
'''

destinations = ["Katy, TX", "Conroe, TX", "Houston, TX", "Pearland, TX", "Galveston, TX"]
restaurants = ["Arbys", "Wendys", "Burger King", "Taco Bell", "Dominos"]
travel_modes = ["Plane", "Car", "Bike", "Train", "Boat"]
entertainment_types = ["Bowling", "Frisbee Golf", "Fishing", "Mini Golf", "Shopping"]

'''dest_1 = destinations[0]
dest_2 = destinations[1]
dest_3 = destinations[2]
dest_4 = destinations[3]
dest_5 = destinations[4]
res_1 = restaurants[0]
res_2 = restaurants[1]
res_3 = restaurants[2]
res_4 = restaurants[3]
res_5 = restaurants[4]
trav_1 = travel_modes[0]
trav_2 = travel_modes[1]
trav_3 = travel_modes[2]
trav_4 = travel_modes[3]
trav_5 = travel_modes[4]
ent_1 = entertainment_types[0]
ent_2 = entertainment_types[1]
ent_3 = entertainment_types[2]
ent_4 = entertainment_types[3]
ent_5 = entertainment_types[4]

def restart():
    random_selection()

def random_selection(choice_1, choice_2):
    answer1 = input(f"We have selected {choice_1} as your {choice_2}. Does this sound good to you? Enter y/n: ")
    if answer1 == "y":
        moving_on()
    else:
        oh_sorry(dest_2)
        if answer1 == "y":
            moving_on()
        else:
            oh_sorry(dest_3)
            if answer1 == "y":
                 moving_on()
            else:
                oh_sorry(dest_4)
                if answer1 == "y":
                    moving_on()
                else:
                    oh_sorry(dest_5)
                    if answer1 == "y":
                        moving_on()
                    else:
                        print("It seems we have run out of options, let's try again!")
                        restart()
random_selection()



random.choice(list)

def random_destination():
    print(random.choice(destinations))

def random_restaurant():
    print(random.choice(restaurants))

def random_travel_mode():
    print(random.choice(travel_modes))

def random_entertainment_types():
    print(random.choice(entertainment_types))


#def random_selection(choice_1, choice_2):
#    print(input(f"We have selected {choice_1} as your {choice_2}. Does this sound good to you? Enter y/n: "))

#random_selection()

def random_destination():
    print(random.choice(destinations))

def random_restaurant():
    print(random.choice(restaurants))

def random_travel_mode():
    print(random.choice(travel_modes))

def random_entertainment_types():
    print(random.choice(entertainment_types))

    '''

random_destination()
random_restaurant()
random_travel_mode()
random_entertainment_types()

answer1 = input(f"We have selected {random_destination} as your destination. Does this sound good to you? Enter y/n: ")

if answer1 == "y":
    moving_on()
else:
    oh_sorry(random_destination)
    

def random_selection(choice_1, choice_2, y_or_n):
    print(f"We have selected {choice_1} as your {choice_2}. Does this sound good to you? Enter {y_or_n} ")
    
yes_or_no = print("Enter y or n: ")
random_selection(random_selection, "thing", yes_or_no)    
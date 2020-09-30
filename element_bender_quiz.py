import time

# First, we make a scoreboard for the elements.

element_dictionary = {"Water": 0, "Earth": 0, "Fire": 0, "Air": 0}

print("Water.")
time.sleep(.6)
print("Earth.")
time.sleep(.6)
print("Fire.")
time.sleep(.6)
print("Air.")
time.sleep(.8)
input("Ready to find out which type of bender you'd be?\n")
time.sleep(.6)
print("Yes? Okay!")
time.sleep(.8)

water_A = 0
earth_B = 0
fire_C = 0
air_D = 0

print("These questions will determine your element.")
time.sleep(1.2)

print("\n1. You are forced into a fight. Your enemy charges at you. What do you do?\n")
time.sleep(2)
print("A) Manuever yourself around them, using the environment to your advantage.")
print("B) Stand your ground and prepare to fight them head-on.")
print("C) Charge at them with rage as your weapon.")
question_one = input("D) Run away from/around your opponent, not letting them catch you.\n")
if question_one.upper() == "A":
	element_dictionary["Water"] += 1.6
elif question_one.upper() == "B":
	element_dictionary["Earth"] += 1.6
elif question_one.upper() == "C":
	element_dictionary["Fire"] += 1.6
elif question_one.upper() == "D":
	element_dictionary["Air"] += 1.6

print("\n2. How would you describe your ideal weekend?\n")
time.sleep(2)
print("A) Spending a lot of time in a hot tub.")
print("B) Doing some resistance training.")
print("C) Eating tons of spicy food.")
question_two = input("D) Anything is fine, as long as the fan or air conditioner is on.\n")
if question_two.upper() == "A":
	element_dictionary["Water"] += 1.3
elif question_two.upper() == "B":
	element_dictionary["Earth"] += 1.3
elif question_two.upper() == "C":
	element_dictionary["Fire"] += 1.3
elif question_two.upper() == "D":
	element_dictionary["Air"] += 1.3

print("\n3. Which of these snacks would you choose?\n")
time.sleep(2)
print("A) Taffy.")
print("B) Chocolate.")
print("C) Hotdog.")
question_three = input("D) Cotton candy.\n")
if question_three.upper() == "A":
	element_dictionary["Water"] += 1
elif question_three.upper() == "B":
	element_dictionary["Earth"] += 1
elif question_three.upper() == "C":
	element_dictionary["Fire"] += 1
elif question_three.upper() == "D":
	element_dictionary["Air"] += 1

print("\n4. Which of these colors is your favorite?\n")
time.sleep(2)
print("A) Blue.")
print("B) Green.")
print("C) Red.")
question_four = input("D) Yellow.\n")
if question_four.upper() == "A":
	element_dictionary["Water"] += 1.5
elif question_four.upper() == "B":
	element_dictionary["Earth"] += 1.5
elif question_four.upper() == "C":
	element_dictionary["Fire"] += 1.5
elif question_four.upper() == "D":
	element_dictionary["Air"] += 1.5

print("\n5. Which one of these situations sounds the most difficult to you?\n")
time.sleep(2)
print("A) Walking on hot coals.")
print("B) Dealing with a tropical storm.")
print("C) Swimming in the deep end.")
question_five = input("D) Pushing a boulder.\n")
if question_five.upper() == "A":
	element_dictionary["Water"] += 1.75
elif question_five.upper() == "B":
	element_dictionary["Earth"] += 1.75
elif question_five.upper() == "C":
	element_dictionary["Fire"] += 1.75
elif question_five.upper() == "D":
	element_dictionary["Air"] += 1.75

# Now to sort the dictionary by highest value to lowest value and reverse it.

element_dictionary_sorted = {key: val for key, val in sorted(element_dictionary.items(), key=lambda ele: ele[1], reverse=True)}

# Turn it into a list.

element_list = list(element_dictionary_sorted)

# Select the first item (the one with the most points).

element_max = element_list[0]

# Make the element lowercase and check if it begins with a vowel.

bender_type = element_max.lower()
first_letter = bender_type[0]
if first_letter == "a" or first_letter == "e":
	bender_type_article = "an " + bender_type
else:
	bender_type_article = "a " + bender_type

time.sleep(1.5)
print(f"You would be {bender_type_article}bender!")
time.sleep(1.5)
print(f"Final Score: {element_dictionary}")

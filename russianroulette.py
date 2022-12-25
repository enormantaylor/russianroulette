import random

names = input("enter the names and seperate them with a comma: ")
new_names = names.split(",")

length = len(new_names)

random_choice = random.randint(0,length-1)
payer = new_names[random_choice]

print("The person who has to pay is: ", payer)


print("CodeLagos Python Batch 5")
print("Name: George Chima")
print("Phone: 0806 708 8949")
print("email: george.chima@gmail.com")
print("How to Survive a wrong landing in Mars")


    
items = [
"A: 5 liters of water",
"B: Shampoo",
"C: An extra Spacesuit",
"D: A shovel",
"E: A 10 day Oxygen supply",
"F: Solar Panels",
"G: The seeds for your mission",
"H: The soil for your mission",
"I: A 5 days food supply",
]


print("It is 2019. You are on a solo mission to explore the planet Mars for a Month while using soil samples brought with you to test if the seeds can grow in Mars atmosphere.")
print("You have just landed but you are in trouble. You have landed 300 kilometers from the base!")
print("You can get to the base in 5 days on the Mars Rover")
print("The Mars Rover can only fit you in your spacesuit and 4 other items")
print("Of all the items below, which would you bring? \n")

for objects in items:
    print(objects)

print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces \nEx: A,B,C,D")
user_choice =input("Enter your choice: ").lower()
#print(user_choice)

user_list = list(user_choice.split(','))
print(user_list)

if "a" not in user_list:
    print("Without a liter of water a day, you will dehydrate")

if "e" not in user_list:
    print("Without Oxygen, you will not have air to breathe!")

if "f" not in user_list:
    print("Without Solar Panels, your Mars Rover will not have enough power to make it to the base")

if "i" not in user_list:
    print("You will not make it to the Mars Base without food. You will need energy to drive the rover")


if "a" in user_list and "e" in user_list and "f" in user_list and "i" in user_list:
    print("YAY! You picked the 4 items needed for the rest of the trip. You will make it to the Mars Base safely.")
else:
    print("BUST! You did not pick the 4 items needed for survival. You will not make it safely to the Mars Base.")

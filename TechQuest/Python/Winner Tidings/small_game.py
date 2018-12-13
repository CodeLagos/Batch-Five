name = input("What is your name: ")
num = int(input("How old are you " + name + " : "))
if num < 16:
    print("You should be in High School")
elif num == 16:
    print("You are ripe for University")
elif num>16<25:
    print("You are an undergraduate")
else:
    print("You should be preparing for grad or graduated long ago")

print("YOU ARE WELCOME TO OPEYEMI PHARMACY STORE")
print("HOW MAY WE HELP U!!!")
client = input("Are you here with a doctor's prescription? (y/n):")
if client == 'n':
    print("Please go the next room on your RIGHT to make see the pharmacist")
else:
    print("Put your doctor's prescription in the box on your LEFT.")
    print("See the cashier to by and collect your drugs.")



print("Please answer the following questions correctly!!!")
score = 0
question1 = input("Are you having headaches? (y/n):")
if question1 == 'y':
    score = score + 1
else:
    score = score
question2 = input("Are you having body pain? (y/n):")
if question2 == 'y':
    score = score + 1
else:
    score = score
question3 = input("Are you having increase in body temperatue? (y/n):")
if question3 == 'y':
    score = score + 1
else:
    score = score
question4 = input("Are you purging? (y/n):")
if question4 == 'y':
    score = score + 1
else:
    score = score
question5 = input("Are you coughing? (y/n):")
if question5 == 'y':
    score = score + 1
else:
    score = score
question6 = input("Are you sneezing? (y/n):")
if question6 == 'y':
    score = score + 1
else:
    score = score
question7 = input("Have you used any malaria drugs during the last two months? (y/n):")
if question7 == 'y':
    score >= 4
    if question7 == client:
        client = "malaria drugs used in the last two month"
else:
     client = "malaria drugs have not been used the last two months"
if score >= 4:
    print("Four or more minior conditions have been meet" + client)
else:
    print("less than three conditions have been meet" + client)
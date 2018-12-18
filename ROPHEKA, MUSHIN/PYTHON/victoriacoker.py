#Emotion checker for individual student in Great Brains School of poise
#This is to help each teacher to have an idea of their student's feeling per moment of check in order to notify the school pschologist
#Instructions, from a scale of 1 to 4 pick the one that best describes your feelings

#My name is Victoria Marsha Coker
#Course of study Python
#08035534935

while True:
    print(" ")
    
    print("Emotion checker for Basic 8 to 9 students")
    Basic8=["Shawn","Anthony","Jude","Kayode","Fin","Hassan"]
    Basic9=["Amos","Joseph","Laurel","Hope","Tope","Obed","Etuk"]
    print("Please, choose your emotional symbol based on your mood this morning from the options available")
    print("Note: input the correct spelling of your name to gain access to this options")
    name=input("Enter your name:")
    if(name in Basic8):
        print("Welcome to Class Champ!",name,"hope your night was great?")
        print("Select from 1 to 4, the emotion that best describes you now\n 1.very happy\n 2.angry\n 3.sad\n 4.I am not too sure:")
        ans=input("Enter your Choice:")
        if(ans=="1"):
            print("Awesome!,have a great day ahead",name, "pls, stay good and make sure you spread love to others")
            print("Thank you for taking this emotion check test, and for being honest")
            continue
        elif(ans=="2"):
                print("Welcome to Class Champ!",name,"hope your night was great?")
                print("awww...,do you feel like talking about it?, when you are up to it, can you meet with me during breaktime for lunch?, it's a date!")
                print("Thank you for taking this emotion check test, and for being honest")

        elif(ans=="3"):
            print("sad???...would you want to talk about it?",name,"if yes, kindly see me in my office")
            print("Thank you for taking this emotion check test, and for being honest")

        elif(ans=="4"):
            print("on a scale of 1 to 3, do you feel like smiling or frowning right now?",name,"if smiling is your choice, that means you are in a better place but if frowning is your choice that means you will have to see me after school for further talks") 
            print("Thank you for taking this emotion check test, and for being honest")

    if(name in Basic9):
        print("Welcome to Class Great Achiever!",name,"I trust you had an awesome day?")
        print("select from 1 to 4, the emotion that best suit you right now\n 1.disgusted\n 2.joyful\n 3.afraid\n 4.sad:")
        ans=input("Enter your choice:")
        if(ans=="1"):
            print("oh dear!, guess, we should look for a way of letting disgust varnish?")
            print("thanks for being honest")
        elif(ans=="2"):
            print("this is beautiful",name,"I pray you can share some of it to your class mates") 
            print("Thank you for taking this emotion check test, and for being honest")
        elif(ans=="3"):
            print("My dear, you have to try and calm down",name,"I know you don't feel like, but give it a thought, do you know you can overcome fear?") 
            print("Thank you for taking this emotion check test, and for being honest")
        elif(ans=="4"):
            print("what is making you sad?",name,"don't you feel like talking about it? a problem shared is half solved") 
            print("Thank you for taking this emotion check test, and for being honest")
            print("I look forward to seeing a better you!")
        else:
            break
            


            
            
              
    


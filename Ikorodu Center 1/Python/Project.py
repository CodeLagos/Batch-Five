#welcome to DANNYMENTRY counselling unit
#Ogunsanmi Daniel Ayomide /08077061877 /danielogunsanmi11@gmail.com/@danny_mentry on Twitter and Instagram.
#Please don't criticise me too much oo..

#Begining..
#Introduction
print ("\n \n \n WELCOME to DANNYMENTRY COUNSELLING UNIT on Career Choice.")
name=raw_input('What\'s your name please?:-\n')
print("Hello %s, We welcome you once again to our counselling unit \n" %name )
print("Please %s ensure you answer all questions sincerely \n \n" %name)

#questionare..
print("Let's get started!! \n \n")
q1= raw_input('%s, do you love reading?:- \n' %name).lower()
if q1 == 'yes':
    print('Hmmm, that\'s nice!\n You must be a scholar!! \n ')
    book = raw_input('What kind of books do you love reading amongst these?\n Fictions \n Science \n Novels \n  Finance \n \n \n').lower()
   
    #fiction 
    if book == 'fictions':
        print("So you do like Fictional books? That's nice!")
        print("Since you love reading fictions,you could consider venturing into WRITING \n Writing:- There is a saying that goes \"Reader are leader\" but I say \"Writers of books are leaders to the Readers\" \n You could also venture into:\n Story telling")
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
   #End of fiction..
   
    #science..
    elif book == 'science':
         sc = raw_input("Hmm, Okay\nWhat science book do you love reading? \n Physics \ Chemistry \ Biology \ Mathematics \n").lower()
         if sc == 'physics': 
             print ("Since you like reading Physics \n You could make a very detail research on these and choose the one that sooth you \n Mechanical Engineering \n Computer Engineering \n Electrical Engineering \n Chemical Engineering \n Or anyother Engineering careers")
         elif sc == "chemistry":
             print(" Hmmm, Twale!! \n That's great \n You consider these careers \n Chemical Engineering \n Pharmacist \n Chemistry teacher or any other chemistry related careers you can find")
         elif sc == "biology":
             print(" Hmm, Efiwe!! \n There are various career you could choose if you're to look in the biological field, such as : \n Destistry \n Pharmacy \n Medical Scientist \n Medical Doctor (Please you have to rethink before venturing into this) \n Psychiatrist etc \n You could make your own research for more \n \n \n")
         elif sc == "mathematics":
             print("Hmm, Jackitophyta!! \n That's great!! \n Mathematical field has a lot of career you could select from, ranging from \n A mathematics Lecturer \n Data Analyst \n Engineerings \n You could you personal research on this to know more.")
         else:
             print("You enter a one of the Science book type mentioned")
             print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
      
    elif book == 'novels': 
         print("Hmmm\n That means you love stories a lot.  \n \n Have you ever thought of:\n Mass communication \n News Casting \n News Paper Editor \n Writing \n If you haven\'t you probably should check them.\n These are not all, there are more you could research on. \n \n GOOD LUCK!!")
         print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    
    elif book == 'finance':
        print('You\'ll like money oo \n \n Okay,You know Finace has to do with a little mathematics.You have to learn a little Mathematics \n \n Now, Careers in Finace are too much that all can\'t be mentioned here, you have to make your own research \n \n These are the ones you could choose and make sure you make research on them. \n Accountant \n Banker \n Record Keeper \n CBN Governor(*winks) etc')
        print('Make sure you research on them before choosing')
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    else:
        print("Opps!\n You didn't enter the words given or the word you entered was misspelt")
        
         
elif q1 == 'no':
    print("Reading sucks right??!! I totally understand")
    no =raw_input("What do love doing best amongst these??:- \n Drawing \n Building creative things \n Cooking \n Playing Games \n Eating \n Fashion \n").lower()
    if no == 'drawing':
        print('I\'m guessing you\'re very good at drawing. \n Well, There are various career you could choose from if you want to purse your passion:- \n Architecture \n Artist \n You could research more if you are not satisfied with the ones above. GOODD LUCK!!')
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    elif no == 'building creative things':
        print("I believe you're a very good at imaginating things 'cus that would be highly needed.\n Okay, These are the courses you could look at:\n Capentry \n Computer Programming \n Brick Laying \n Shoe COBBLER /nAny many more,you could always research more on these. Good luck!!")
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    elif no == 'cooking':
        print("You could consider anyone of the following:\n Catering \nBakering \n You could also start-up a business where you could sell foods to people\n If you aren't satisfied with this you could always research for more.Good luck!!")
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    elif no == 'playing games':
        print("\n You could be a professional Gamer \n A game developer \n Or any other ones you find during your research.")
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    elif no == 'eating':
        print("You should be a farmer.My brother go to the farm, NO FOOD FOR LAZY MAN")
    elif no == 'talking':
        print("You could look into: \n Interpreter \n Religious leader \n Musician \n Search more if you aren't satisfied with the above. Good luck!!")
        print("Thanks for using DANNYMENTRY COUNSELLING APP, I hope we were able to help you.\n \n \n If there are any complaint you can always go to www.dannymentry.com to comment your complaint. \n \n Thank you")
    else:
        print("Opps!! \n You should enter any of the suggestions listed above or you should research more if you aren't satisfied with the one listed")
else:
        print("Opps! \n Something went wrong \nYou should enter a Yes or No answer")
   
 
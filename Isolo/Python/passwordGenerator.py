# import the random module.
import random 
print("ENOW TABI CLINTON  \n clintonenow1@gmail.com \n 07063716388 \n code lagos python class Batch 5 \n project: password generator")



#Creating a list of characters
chars = 'abcdefghijklmnopqrstuvwxyz0123456789.!,ABCDEFGHIJ'
#asking the number of passwords the user wants. only whole numbers will be recognized 
num = int(input(' number of passwords? ' ) )


#ask user for the lenght of  password
length = int(input(' password lenght? ') )


#for loop ensures the num of passwords are created instantly
for p in range(num):  
 #initializing password to an empty box
    password = ""
    
#choosing a random character thruout the lenght of password
    for c in range(length):
        
# += ensure new character is being added to the password each time.  
      password += random.choice(chars) 
    
 #print results 
    print(password) 

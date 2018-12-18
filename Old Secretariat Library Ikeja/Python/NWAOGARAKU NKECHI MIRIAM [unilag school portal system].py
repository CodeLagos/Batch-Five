# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:47:28 2018

@author: Onyinye
"""


#my project is about unilag student portal
message= "WELCOME TO UNILAG STUDENT PORTAL"
print("Name:NWAOGARAKU NKECHI MIRIAM")
print("Email:nwaogarakunnkechi@gmail.com")
print("Centre:ikeja old secretariat")

print(message)
username=input("USERNAME:")
#print("enter your password")
password=(input("PASSWORD:"))
#default password is your username
if password==username:
    print("succesful log in")
else:
    print("password not correct")
    #choose an option
print("CHOOSE AN OPTION")
#select 
print("DASHBOARD")

options=("1)Course registration\n2)Accommodation\n3)Biodata\n4)Results\n5)Payment\n6)Application\n7)Documents\n8)Election")
print(options)
option1=input("choose an option:")
#print("choose an option")
if option1 in options:
   print("view")
else:
    print("choose an option")
    
print("PAYMENT")
choose=("1)Generate/Regenerate fees\n2)View payadvice\n3)Remita\n4)Print receipt\n5)Referral application")
print(choose)
payin=input("select pay:")
if payin in choose:
    print("Receipt for 2018/2019 Academic session ")
    print("proceed to register your courses")
else:
    print("wrong selection")
option2=input("choose an option:")
if option2 in options:
    print("Register courses")
else:
    print("choose an option")
print("you are eligible to ballot")
print("ACCOMMODATION")
hostel=("1)New hall\n2)Moremi\n3)Down school")
print(hostel)
option3=input("choose an option:")
if option3 in hostel:
    print("Ballot in progress")
else:
    print("choose an option")
print("congratulations,room assigned,proceed to your hostel to complete your registration")
    




""" School Student Pick up Registration.
The program helps to generate a pick up card to assist te School in tracking who picks a child, the time and saves the data for future reference 

ALGORITHM
-Get the information of Parent/Guardian
-Generate a pick up card 
-It also saves the data of the Parent such that it can be accessed when required"""

print ("")
print("         ROYAL INTERNATIONAL SCHOOLS\n12, THOMAS CRESCENT, VICTORIA ISLAND, LAGOS, NIGERIA")
print ("")
print ("                PICK UP CARD")
print ("            ENTER YOUR DETAILS\n")
from datetime import datetime
now= datetime.now()
import datetime

import random
DATA= {}
def parent_data():
      title= input('Title(Mr/Mrs/Master/Miss): ')
      surname= input('Surname: ')
      firstname= input('Firstname: ')
      othername=input('Middlename: ')
      address= input('Permanent Address: ')
      sex= input('Gender: ')
      phoneno= input('Phone Number: ')
      child= input('Childs name: ')
      level= input('Childs class: ')
      time= input('Time of pickup: ')
      relationship= input('Your relationship to the child: ')
      occupation= input('Occupation: ')
      email= input('Email Address: ')
      password= input('Enter password: ')
            
      validinput= False
      while not validinput:
            try:
                  year=int(input('enter birth year:'))
                  month= int(input('enter birth month(where,May=5):'))
                  day= int(input('enter birth day:'))
                  validinput=True
            except:
                  print("please Enter number for your birth month,day and year")
      MONTH= str(month)
      DAY= str(day)
      YEAR= str(year)
      birthday= (MONTH + '/' + DAY + '/' + YEAR)
      DOB=datetime.datetime(year,month,day)
      age=(datetime.datetime.now()-DOB)
      convertdays= int(age.days)
      ageyears= convertdays/365
      Age= int(ageyears)
      if(Age>=18):
            pass
      else:
        print('YOU ARE NOT ELIGIBLE TO PICK UP A CHILD')
      DATA[password]=surname,firstname,othername,address,sex,birthday,Age,phoneno,child,level,time,relationship,occupation,password
def vin():
      num=str(random.randint(1000000,9999999))
      a=[chr(i) for i in range(65,123) if chr(i).isalpha()]
      a=random.sample(a,4)
      a=''.join(a)
      no= a+num
      return no
FTN= vin()
def database():
      user= input('Re-Enter your Password: ')
      print("*****************************************************************************")
      print("       *************************************************************    ")
      print("*******                                                             *******")
      theme= '{:^40}'.format('ROYAL INTERNATIONAL SCHOOLS')
      print(theme)
      inec= '{:^30}'.format('IKEJA, LAGOS, NIGERIA')
      print(inec)
      card='{:^50}'.format("SCHOOL PICKUP CARD")
      print(card)
      date='{:>50}'.format('DATE OF ISSUE:')
      print("-------------------------------------------------------------------------------")
      
      print(date,now)
      user_data=DATA[user]
      det0= user_data[0]
      print ("SURNAME: ",det0)
      det1= user_data[1]
      print ("FIRSTNAME: ",det1)
      det2= user_data[2]
      print ("OTHERNAME: ",det2)
      det3= user_data[3]
      print ("PERMANENT ADDRESS: ",det3)
      det4= user_data[4]
      print ("SEX: ",det4)
      det5= user_data[5]
      print ("DATE OF BIRTH: ",det5)
      det6= user_data[6]
      print ("AGE: ",det6)
      det8= user_data[8]
      print ("CHILD: ",det8)
      det9= user_data[9]
      print ("LEVEL: ",det9)
      det10= user_data[10]
      print ("PICK UP TIME: ",det10)
      det11= user_data[11]
      print ("RELATIONSHIP WITH CHILD: ",det11)
      det12= user_data[12]
      print ("OCCUPATION: ",det12)
      print("\n")
      print("                         Royal International School Pickup Card\n")
      print("SCHOOL PICK UP CARD NO. ISUUED: ",FTN)
      print ("******                                                                ********")
      print ("       ****************************************************************       ")
      print ("*******************************************************************************")

while True:
      parent_data()
      ext= input("Type 'PRINT' to continue: ")
      if (ext.upper()=='PRINT'):
            database()
            break

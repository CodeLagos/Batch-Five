print("PROGRAM TITLE: AIR FLIGHT TICKET REGISTRATION")
print("STUDENT NAME: MR ADEWOLE OLUSOLA ADEDIPE")
print("EMAIL: OLUSOLAHERO@GMAIL.COM")


print("\nThis is a program written after a comprenhensive CodeLagos Python Tutorial organised by the Lagos State Government. The program helps to generate an Air Flight Ticket for Air Boarders")

print("\n FUNCTIONALITY OF PROGRAM: -Get the information of applicant -Calculate the Age and check for the eligibility of the applicant to travel,-Generate Applicant's flight ticket and slip-It also saves the data of the Applicant such that it can be accessed when required")

print("MURITALA MOHAMMED INTERNATIONAL AIRPORT\nIKEJA, LAGOS, NIGERIA\nFLIGHT TICKET\n")
from datetime import datetime
now= datetime.now()
import datetime

import random
DATA= {}
def flight_data():
      title= input('Title(Mr/Mrs/Master/Miss): ')
      surname= input('Surname: ')
      firstname= input('Firstname: ')
      othername=input('Middlename: ')
      address= input('Permanent Address: ')
      sex= input('Gender: ')
      phoneno= input('Phone Number: ')
      citizenship= input('Nationality: ')
      state= input('State of Origin: ')
      lga= input('Local Government Area: ')
      occupation= input('Occupation: ')
      purpose= input('What is your purpose of travelling: ')
      period= input('How long do you intend spending: ')
      email= input('Email Address: ')
      password= input('Enter password: ')
      
      validinput= False
      while not validinput:
            try:
                  year=int(input('enter birth year:'))
                  month= int(input('enter birth month(where,April=4):'))
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
        print('YOU ARE NOT ELIGIBLE TO TRAVEL\nPLS TRY AGAIN WHEN YOU ARE 18YEARS')
      DATA[password]=surname,firstname,othername,address,sex,birthday,Age,phoneno,citizenship,state,occupation,password,purpose,period
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
      theme= '{:^40}'.format('MURITALA MOHAMMED INTERNATIONAL AIRPORT')
      print(theme)
      inec= '{:^30}'.format('IKEJA, LAGOS, NIGERIA')
      print(inec)
      card='{:^50}'.format("FLIGHT TICKET/ SLIP")
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
      det10= user_data[10]
      print ("OCCUPATION: ",det10)
      det12= user_data[12]
      print ("PURPOSE OF TRAVELLING: ",det12)
      det13= user_data[13]
      print ("TIME PERIOD OF TRAVELLING: ",det13)
      print("\n")
      print("                         One Ticket Obodo Oyinbo\n")
      print("FLIGHT TICKET NO. ISUUED: ",FTN)
      print ("******                                                                ********")
      print ("       ****************************************************************       ")
      print ("*******************************************************************************")

while True:
      flight_data()
      ext= input("Type 'FLY' to continue: ")
      if (ext.upper()=='FLY'):
            database()
            break

#Emmanuel Akpode
#08066151507
class hotelbusiness:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',sex='', address='',cindate='',coutdate='',rno=1):
        #self here is an attribute of class
        #rt, s, p, r, t, a are parameters chosen to work with. Any letter can be used.
        #cindate is check in date, coutdate is check out date, rno is room number.

        print ("\n\n***** THIS IS LAGOS SUPER HOTEL*****\n")
        print ("\n\n*****WELCOME! WELCOME!! WELCOME!!!*****\n")


        #Turning the parameters into attributes
        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.sex=sex
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
        
    def inputdata(self):
        self.name=input("\nEnter your name: ")
        self.sex=input("\nEnter your sex: ")
        self.address=input("\nEnter your address: ")
        self.cindate=input("\nEnter your check in date: ")
        self.coutdate=input("\nEnter your checkout date: ")
        print ("  ")
        print (" CUSTOMER DETAILS ")
        #Print out the inputed details and room number
        print("Name            : ", self.name)
        print("Address         : ", self.address)
        print("Check in date   : ", self.cindate)
        print("Check out date  : ", self.coutdate)
        print("Your room number: ", self.rno,"\n")
        
    def roomrent(self):

        print ("The following rooms are available:-")

        print ("1.  Presidential Suit ----> N300000 ")

        print ("2.  Executive Suite   ----> N200000 ")

        print ("3.  Single Room       ----> N20000 ")

        print ("4.  Double Room       ----> N50000 ")
        
        print ("5.  King Bedroom      ----> N150000 ")
        
        print ("6.  Queen Bedroom     ----> N100000 ")

        x=int(input("Please enter your choice: "))

        n=int(input("How many nights do you intend to stay: "))

        if(x==1):

            print ("You have choosen Presidential Suite")

            self.s=300000*n

        elif (x==2):

            print ("You have choosen Executive Suite")

            self.s=200000*n

        elif (x==3):

            print ("You have choosen Single Room")

            self.s=20000*n

        elif (x==4):
            print ("You have choosen Double Room")

            self.s=50000*n

        elif (x==5):
            print ("You have choosen King Bedroom")

            self.s=150000*n

        elif (x==6):
            print ("You have choosen Queen Bedroom")

            self.s=100000*n

        else:

            print ("please choose a room")

        print ("Your Room rent is =",self.s,"\n")

    def restaurantbill(self):

        print("*****RESTAURANT MENU*****")

        print("1. Pizza                  ----> N5000 \n2. Coldstone              ----> N3500 \n3. Barbecue               ----> N7000 \n4. Eba and Egusi Soup     ----> N10000 \n5. Fried Rice and Chicken ----> N15000 \n6. Exit")

        #Using the while loop
        while (1):

            c=int(input("Enter your choice: "))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+5000*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+3500*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+7000*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10000*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+15000*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost = N",self.r,"\n")

    def	laundrybill(self):
        print ("******LAUNDRY MENU*******")

        print ("1. Trousers           ----> N2000 \n2. T-Shirt            ----> N1000 \n3. Long Sleeve        ----> N3000 \n4. Jeans              ----> N5000 \n5. Ankara and Wrapper ----> N4000 \n6. Exit")

        while (1):
            #brought to you by code-projects.org

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+2000*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+1000*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3000*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5000*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4000*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print ("Total Laundary Cost = N",self.t,"\n")

    def gamebill(self):
        print ("******GAME MENU*******")

        #Print out the different games and the amount they cost
        print ("1. Table tennis ----> N2000 \n2. Swimming     ----> N3000 \n3. Snooker      ----> N6000 \n4. Video games  ----> N1000 \n5. Card games   ----> N4000 \n6. Exit")



        while (1):

            
            g=int(input("Enter your choice: "))


            if (g==1):
                h=int(input("No. of hours: "))
                self.p=self.p+2000*h

            elif (g==2):
                h=int(input("No. of hours: "))
                self.p=self.p+3000*h

            elif (g==3):
                h=int(input("No. of hours: "))
                self.p=self.p+6000*h

            elif (g==4):
                h=int(input("No. of hours: "))
                self.p=self.p+1000*h

            elif (g==5):
                h=int(input("No. of hours: "))
                self.p=self.p+4000*h
            elif (g==6):
                break;

            else:

                print ("Invalid option")


        print ("Total Game Bill = N",self.p,"\n")

    #Displaying Customer details, all bills and total bill
    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details and Total bill ")
        print ("Customer name        : ",self.name)
        print ("Customer sex         : ",self.sex)
        print ("Customer address     : ",self.address)
        print ("Check in date        : ",self.cindate)
        print ("Check out date       : ",self.coutdate)
        print ("Room number          : ",self.rno)
        print ("Your Room rent is    : ",self.s)
        print ("Your Food bill is    : ",self.r)
        print ("Your Laundary bill is: ",self.t)
        print ("Your Game bill is    : ",self.p)

        #Calculate the sub total
        self.rt=self.s+self.t+self.p+self.r
        #Print out the sub total bill
        print ("Your Sub total bill is: ",self.rt)
        print ("Additional Service Charges is ",self.a)
        #Print out the grand total bill
        print ("Your Grand total bill is: ",self.rt+self.a,"\n")
        #This increase the number of the room taking the next customer to the next number room.
        self.rno+=1

            

        

        

def main():

    a=hotelbusiness()
    #calling the class
    

    while (1):
        print("1. Enter Customer Details")
        
        print("2. Calculate Room rent")

        print("3. Calculate Restaurant bill")

        print("4. Calculate Laundry bill")

        print("5. Calculate Game bill")

        print("6. Show Total cost")

        print("7. Exit")

        b=int(input("\nEnter your choice: "))
        #calling the different function for each conditional statement
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurantbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()


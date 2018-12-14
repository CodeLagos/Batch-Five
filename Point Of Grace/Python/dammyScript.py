print("AKINOLA TOHEEBAT OLUWADAMILOLA")
#Contact:oreayo30@gmail.com
print("oreayo30@gmail.com")
print("================================================================================")
#Welcome the user
print("Welcome to Percentage Calculator")
print("================================================================================")
#Description:This code help to calculate the percentage of a student score
print("This code help to calculate the Percentage of a student score")
print("The total marks for each subject is 100")
#Print out the instructions
stop = 1
while (stop != 0):
    print("\nEnter your scores")
    English=int(input("Enter your English score: "))
    Mathematics=int(input("Enter your Mathematics score: "))
    Biology=int(input("Enter your Biology score: "))
    Chemistry=int(input("Enter your Chemistry score: "))
    Physics=int(input("Enter your Physics score: "))
    #Print out the percentage
    Percentage=((English/100*100)+(Mathematics/100*100)+(Biology/100*100)+(Chemistry/100*100)+(Physics/100*100))/5
    print("Your percentage score is %d%s" %(Percentage,'%'))
    stop = int(input("\nEnter 0 to stop: "))

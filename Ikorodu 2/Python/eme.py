##Name:jegede temitayo oluwatosin
##center name:rotary vocational center igbogbo
##year 2018
##lectures:Rex Ben
## project name: emergency help
##welcome user
def emergency():
 print("welcome to lagos state emergency")
 ##emergency type
 print("press 1 fire emergency:\npress 2 water emergency:\npress 3 acciedent emergency:\npress 4 ambulance emergency:\npress 5 robbery emergency:\n")
 response = input("Response:")
 ##response input
 if(response =="1"):
    print("welcome to fire emergency")
    relpy=input("were are you call from,press 1 for mainland press 2 island")
    if(relpy=="1"):
        print("the bus is coming for ikeja")
        print("thank you,the bus we be there in 1 hour")
        print("thank you for calling")
    elif relpy =="2":
         print("the bus is coming for V.I")
         print("thank you,the bus we be there in 1 hour")
         print("thank you for calling")
 elif(response =="2"):
    print("welcome to water emergency")
    relpy=input("were are you call from,press 1 for mainland press 2 island")
    if(relpy=="2"):
        print("the bus is coming for lekki")
        print("thank you,the bus we be there in 56 min")
        print("thank you for calling")
    elif relpy =="1":
         print("the bus is coming for abula")
         print("thank you,the bus we be there in 1 hour")
         print("thank you for calling")
 elif(response =="3"):
    print("welcome to acciedent emergency")
    relpy=input("were are you call from,press 1 for mainland press 2 island")
    if(relpy=="2"):
        print("the bus is coming for banana island ")
        print("thank you,the bus we be there in  1 hour")
        print("thank you for calling")
    elif relpy =="1":
         print("the bus is coming for 3th mainland brige")
         print("thank you,the bus we be there in 1 hour")
         print("thank you for calling")

 elif(response =="4"):
    print("welcome to ambulance emergency")
    relpy=input("were are you call from,press 1 for mainland press 2 island")
    if(relpy=="1"):
        print("the bus is coming for ikorodu")
        print("thank you,the bus we be there in  1 hour")
        print("thank you for calling")
    elif relpy =="2":
         print("the bus is coming for PZ")
         print("thank you,the bus we be there in 1 hour")
         print("thank you for calling")

 elif(response =="5"):
    print("welcome to robbery emergency")
    relpy=input("were are you call from,press 1 for mainland press 2 island")
    if(relpy=="1"):
        print("the bus is coming for lekki ajah island ")
        print("thank you,the bus we be there in  1 hour")
        print("thank you for calling")
    elif relpy =="2":
         print("the bus is coming for apple village")
         print("thank you,the bus we be there in 1 hour")
         print("thank you for calling")
 else:
    print("you have enter wrong number")
    print()
    emergency()
 
emergency()

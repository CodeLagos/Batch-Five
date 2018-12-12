#Calculator For Weekly Register
print ("CALCULATOR FOR WEEKLY REGISTER")

print ("Coded by Ogunsanwo Oreyemi Sunday \n 08067472164 \n ogunsanwooreyemisunday@gmail.com")
print("===========================================================================================================================================")
print("Instruction: Please enter Mtotoal,Atotal,Nroll,NDSO to calculate your register for the week. Note the full meaning of the following acronym: \n Mtotal = Morning Total, \n Atotal= Afternoon Total, \n Nroll= Total number of students in the class \n NDSO= Numbers of Days School Open")  

print ("PLEASE ENTER YOUR DATA BELOW")
Mtotal=float(input("Enter MTotal: "))
Atotal=float(input("Enter ATotal: "))
Nroll=float(input("Enter No On Roll: "))
NDSO= float(input("Enter No of Days School Open: "))
Average = ((Mtotal + Atotal)/(Nroll * NDSO)) * 100
print (Average)
print(round(Average, 2))
if (Average>50):
    print("Above average")
if (Average <50):
    print("Below average")
    print:("Below average")

    
print ("Thank you for using the calculator")

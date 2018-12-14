#Author: Olakun P Osho
#This project is design to determine the Square Meter and give the Number of Floor Packet Tiles for given Area

#for w range(1,5):
print("*"*80)
print("\t\t\t\t\t Tiler Calculator")
print("*"*80)

#Ask user to select a choice 
var =input("Seclect an option \n a) Centimeter \n b) Millimeter \n c) Meter \n d) Feet \n e) Inches \n....:")

#code get the meter square and print
if (var.lower()=="a"):
    var= "Centimeter"
    ln=float(input("Enter Lenght value in Cenetimeter :"))
    wd=float(input("Enter Width value in Cenetimeter : "))
    mln=ln/100
    mwd=wd/100
    sqm=mln*mwd
    print("The Sqaure Meter is :",sqm)
    
    
elif (var.lower()=="b"):
    var= "Millimeter"
    ln=float(input("Enter Lenght value in Milimeter :"))
    wd=float(input("Enter Width value in Milimeter : "))
    mln=ln/1000
    mwd=wd/1000
    sqm=mln*mwd
    print("The Sqaure Meter is :",round(sqm,2))
    

elif (var.lower()=="c"):
    var= "Meter"
    ln=float(input("Enter Lenght value in Meter :"))
    wd=float(input("Enter Width value in Meter : "))
    sqm=ln*wd
    print("The Sqaure Meter is :",round(sqm,2))
    

elif (var.lower()=="d"):
    var= "Feet"
    ln=float(input("Enter Lenght value in Feet :"))
    wd=float(input("Enter Width value in Feet : "))
    mln=ln/3.281
    mwd=wd/3.281
    sqm=mln*mwd
    print("The Sqaure Meter is :",round(sqm,2))

elif (var.lower()=="e"):
    var= "Inches"
    n=float(input("Enter Lenght value in Feet :"))
    wd=float(input("Enter Width value in Feet : "))
    mln=ln/39.37
    mwd=wd/39.37
    sqm=mln*mwd
    print("The Sqaure Meter is :",round(sqm,2))
else:
    print("Invalid Option")
    exit()
    
#Ask user to select a choice of Tiles size    
print("\n"*4)
print("*"*80)
print("Seclect an option for Tiles size \n a) 400mm x400mm \n b) 400mm x250mm \n c) 300mm x 300mm \n d) 250mm x 250mm ")
print("*"*80)
var=input("....:")


#code get the size of tiles packets
if(var.lower()=="a"):
    ts=1.92*sqm
    print("The Packet of Floor Tiles to fill",round(sqm,2),"Meter square is: ",round(ts,0),"packets")

elif (var.lower()=="b"):
    ts=1.2*sqm
    print("The Packet of Floor Tiles to fill",round(sqm,2),"Meter square is: ",round(ts,0),"packets")

elif (var.lower()=="c"):
    ts=1.08*sqm
    print("The Packet of Floor Tiles to fill",round(sqm,2),"Meter square is: ",round(ts,0),"packets")

elif (var.lower()=="d"):
    ts=0.75*sqm
    print("The Packet of Floor Tiles to fill",round(sqm,2),"Meter square is: ",round(ts,0),"packets")

else:
    #(var!="b")
    print("Enter the Right Value")   


    

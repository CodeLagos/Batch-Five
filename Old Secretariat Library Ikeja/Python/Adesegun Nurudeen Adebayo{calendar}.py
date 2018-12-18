#CALENDAR TO DISPLAY THE GIVEN MONTH OF THE YEAR

#Import module
import calendar

#Print Welcome
print("Project Title : Calendar")
print("Name : Adesegun Nurudeen Adedayo")
print("Email : Adesegunana@gmail.com")
print("Centre : Old Secreteriat Library Ikeja")


#Enter in format - 2011, 2014, 1994, 2018

year = int(input("Enter Year: "))

#Enter in format - 01, 08, 12

month = int(input("Enter Month: "))

print(calendar.month(year, month))

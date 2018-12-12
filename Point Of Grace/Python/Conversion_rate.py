# OLUWAYINKA OGUNBODE


# Display the purpose of the program
print("This program is to help in conversion rate varying from different units")
# Display the instructions to the users
print("Please select the option of your conversion from the option below and enter the value to be converted")

conversion_rate = input("Select your conversion rate \n(A) seconds to minutes \n(B) minutes to hours \n(C) hours to days \n(D) days to weeks \n(E) weeks to month \n(F) months to years \n(G) metres to kilometres  \n(H) millimetres to metres \n(I) grammes to kilogrammes \n Answer:")
if (conversion_rate.lower()=='a'):
    seconds = eval(input("Enter the seconds to be converted: "))
    minutes = seconds/60
    minutes = round(minutes, 1)
    print("Your conversion result is", minutes)


if (conversion_rate.lower()=='b'):
    minutes = eval(input("Enter the minutes to be converted: "))
    hours = minutes/60
    hours = round(hours, 1)
    print("Your conversion result is", hours)


if (conversion_rate.lower()=='c'):
    hours = eval(input("Enter the hours to be converted: "))
    days = hours/24
    days = round(days, 1)
    print("Your conversion result is", days)


if (conversion_rate.lower()=='d'):
    days = eval(input("Enter the days to be converted: "))
    weeks = days/7
    weeks = round(weeks, 1)
    print("Your conversion result is", weeks)


if (conversion_rate.lower()=='e'):
    weeks = eval(input("Enter the weeks to be converted: "))
    months = weeks/4
    months = round(months, 1)
    print("Your conversion result is", months)


if (conversion_rate.lower()=='f'):
    months = eval(input("Enter the months to be converted: "))
    years = months/12
    years = round(years, 1)
    print("Your conversion result is", years)


if (conversion_rate.lower()=='g'):
    metres = eval(input("Enter the metres to be converted: "))
    kilometres = metres/1000
    kilometres = round(kilometres, 1)
    print("Your conversion result is", kilometres)


if (conversion_rate.lower()=='h'):
    millimetres = eval(input("Enter the millimetres to be converted: "))
    metres = millimetres/1000
    metres = round(metres, 1)
    print("Your conversion result is", meters)


if (conversion_rate.lower()=='i'):
    grammes = eval(input("Enter the grammes to be converted: "))
    kilogrammes = grammes/1000
    kilogrammes = round(kilogrammes, 1)
    print("Your conversion result is", kilogrammes)


print("THANK YOU")


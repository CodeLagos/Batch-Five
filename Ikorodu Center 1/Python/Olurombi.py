while True:
    #Prints out the purpose of this program.
    print("\n\n\n\n\nThis is a CUMULATIVE GRADE POINT AVERAGE CALCULATOR")
    #Olurombi Anuoluwapo, 07055625874, omomurewale@gmail.com, oluronbianu@gmail.com

    #Prints out instructions for the user.
    print("The number of courses done so far must be positive.")
    print("The unit of course must be positive.")

    #Ask the user to input the number of courses done so far.
    courses_no = int(input("Enter the number of courses done so far: "))

    #If the number of courses is a negative number, it should print out these block of code.
    if (courses_no <= 0):
        print("Invalid input")


    else:
        #Initializing these variables.
        z = 0
        total_units = 0

        #It should do the following block of codes within these range.
        for i in range(0,courses_no):
            #Ask the user to input the score and the unit of the courses.
            score = float(input("Enter your percentage score in course {0}: " .format(i + 1)))
            unit = int(input("Enter the unit of course {0}: " .format(i + 1)))

            #Initializing the grade variable.
            grade = 0
            if score <= 100 and score >= 70 :
                grade += 5
            elif score < 70 and score >= 60:
                grade += 4
            elif score < 60 and score >= 50:
                grade += 3
            elif score < 50 and score >= 45:
                grade += 2
            elif score < 45 and score >= 40:
                grade += 1
            elif score < 40:
                grade += 0

            #This sums up all the unit of each courses done so far. 
            total_units =  total_units + unit 
    
            i = grade * unit
            #This sums up all the i's.
            z = z + i
        #This prints out the cgpa
        print("Your current cgpa is ",round(z / total_units , 2))    

#NAME: HUSSAYN ABDULRAHMON
#PHONE_NUM: 08094855657, 07030916234
#EMAIL: haroworld91@gmail.com

def start():
    restart = 'y'
    totalcredit = 0.0
    totalcal = 0.0
    finalgpa = 0.0
    course_per_score = {}
    course_per_unit = {}
    grade_per_course = {}
    total_credit = {}
    total_grade = {}
    final_gpa = {}
    while True:
        #course name
        course = input('\nENTER COURSE NAME: ')
        #course unit
        print('ENTER',course,'UNIT')
        credit = input('\nENTER COURSE UNIT: ')
        #Student score
        score = int(input('\nENTER YOUR SCORE: ' ))
        #course and unit update
        course_per_score.update({course:score})
        course_per_unit.update({course:credit})
        if score >= 75:
            grade = 4.0
            caltimes = float(credit) * grade
        elif score >= 70:
            grade = 3.5
            caltimes = float(credit) * grade
        elif score >= 65:
            grade = 3.25
            caltimes = float(credit) * grade
        elif score >= 60:
            grade = 3.0
            caltimes = float(credit) * grade
        elif score >= 55:
            grade = 2.5
            caltimes = float(credit) * grade
        elif score >= 50:
            grade = 2.25
            caltimes = float(credit) * grade
        elif score >= 45:
            grade = 2.0
            caltimes = float(credit) * grade
        elif score >= 40:
            grade = 1.5
            caltimes = float(credit) * grade
        elif score <= 39:
            grade = 0.0
            caltimes = float(credit) * grade
        grade_per_course.update({course:caltimes})
        totalcredit = totalcredit + float(credit)
        totalcal = totalcal + caltimes
        total_credit.update({'TOTAL UNIT':totalcredit})
        total_grade.update({'TOTAL GRADE':totalcal})
        restart = input('WOULD YOU LIKE TO ADD ANOTHER COURSE: Yes or No ')
        if restart in ('yes','y','YES','Y'):
            print('\nADD COURSE')
        else:
            break
    print('\nCOURSE UNIT',course_per_unit)
    print('SCORE',course_per_score)
    print('GRADE',grade_per_course)
    print(total_credit)
    print(total_grade)
    finalgpa = round(totalcal/totalcredit,2)
    final_gpa.update({'FINAL GPA':finalgpa})
    print(final_gpa)
    print('\nGPA'+ str(finalgpa))
restart = 'y'
while True:
    GPA = start()
    restart = input('CHECK ANOTHER GPA? Yes or No ')
    if restart in ('yes','y','YES','Y'):
        print('CHECK GPA')
    else:
        break


    


            
        
    
    
    

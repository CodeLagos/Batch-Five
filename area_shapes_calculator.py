#DOSU EVANS CHUKWUDI

#THE PURPOSE OF THE PROGRAM
print('PROGRAM TO CALCULATE AREA OF ANY CHOOSEN SHAPE')
print('****************************************************************')

#INSTRUCTIONS TO FOLLOW
print('PLEASE ADHERE TO THE INSTRUCTION')
print('-----------------------------------')

#INPUT STATEMENTS
for i in range(4):
    print('*' * 8)
print('SQUARE')
print('\n')

for i in range(4):
    print('*' * 11)
print('RECTANGLE')
print('\n')

for i in range(5):
    print('*' * (i + 1))
print('TRIANGLE')
print('\n')


#SELECT OPTION FOR CALCULATION
select_area = input('Select The Shape To Calculate Its Area? \n(a) Triangle \n(b) Square \n(c) Rectangle \n(d) Circle \n(e) Cylinder \n Answer: ')

#WAIT FOR THE ANSWER
                     
#IF THE SHAPE SELECTED IS TRIANGLE
if (select_area.lower()=='a'):
    print('Triangle')
    base = eval(input('Enter the base: '))
    height = eval(input('Enter the height: '))
    area = 0.5 * base * height
    print('Area of Triangle = %dcm2' %area)
    
                     
#IF THE SHAPE SELECTED IS SQUARE
if (select_area.lower()=='b'):
    print('Square')
    lenght = eval(input('Enter the lenght: '))
    area = lenght * lenght
    print('Area of Square = %dcm2' %area)
    
                     
#IF THE SHAPE SELECTED IS RECTANGLE
if (select_area.lower()=='c'):
    print('Rectangle')
    lenght = eval(input('Enter the lenght: '))
    breath = eval(input('Enter the breath: '))
    area = lenght * breath
    print('Area of Rectangle = %dcm2' %area)

#IF THE SHAPE SELECTED IS CIRCLE
if (select_area.lower()=='d'):
    print('Circle')
    radius = eval(input('Enter the radius: '))
    area = 3.14 * (radius **2)
    print('Area of Cirle = %dcm2' %area)

#IF THE SHAPE SELECTED IS CYLINDER
if (select_area.lower()=='e'):
    print('Cylinder')
    radius = eval(input('Enter the radius: '))
    height = eval(input('Enter the height: '))
    area = 2 * 3.14 * (radius **2) * height
    print('Area of Cylinder = %dcm2' %area)

print('Thank You')
input('Press Enter to Exit')
    



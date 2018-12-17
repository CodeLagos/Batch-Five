'''weight converter program
code made by Fadipe Paul
08079934243
fadipepaul@gamil.com
program that help to convert weight from one unit to another
it requires the unit to be selected from the options displayed'''
print('You can convert your weight to any unit you want')
while True:
    #prompt the user to input the weight to be converted
    weight=float(input("Enter your weight:"))
    #prompt the user to select the unit to be converted
    unit=input('select the unit of the weight.\na.kilogram\nb.pounce\nc.ounce\nd.tonnes\n')
    if unit.lower()=='a':
        #prompt the user to select the unit of the converted weight
        convert_weight_1=input('Enter the unit to convert to.\na.pounce\nb.ounce\nc.tonnes\n')
        if convert_weight_1.lower()=='a':
            converted_weight=weight*2.2046
        elif convert_weight_1.lower()=='b':
            converted_weight=weight*35.274
        elif convert_weight_1.lower()=='c':
            converted_weight=weight/1000
    elif unit.lower()=='b':
        #prompt the user to select the unit of the converted weight
        convert_weight_2=input('Enter the unit to convert to.\na.kilograms\nb.ounce\nc.tonnes\n')
        if convert_weight_2.lower()=='a':
            converted_weight=weight/2.2046
        elif convert_weight_2.lower()=='b':
            converted_weight=weight*16
        elif convert_weight_2=='c':
            converted_weight=weight*0.00045
    elif unit.lower()=='c':
        #prompt the user to select the unit of the converted weight
        convert_weight_3=input('Enter the weight to be converted to.\na.kilogram\nb.pounce\nc.tonnes\n')
        if convert_weight_3=='a':
            converted_weight=weight/35.274
        elif convert_weight_3=='b':
            converted_weight=weight/16
        elif convert_weight_3=='c':
            converted_weight=weight*0.00002835
    elif unit.lower()=='d':
        #prompt the user to select the unit of the converted weight
        convert_weight_4=input('Enter the weight to convert to.\na.kilogram\nb.pounce\nc.ounce\n')
        if convert_weight_4=='a':
            converted_weight=(weight*1000)
        if convert_weight_4=='b':
            converted_weight=(weight/0.00045)
        if convert_weight_4=='c':
            converted_weight=(weight/0.00002835)
    #print out the converted weight
    print(round(converted_weight,2))
